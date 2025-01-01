import os
import importlib.util
import traceback
import re
from multiprocessing import Process, Queue
from typing import Any
from datetime import datetime
from metrics.cyclomatic_complexity import calculate_cyclomatic_complexity, calculate_function_lengths, calculate_comment_ratio,calculate_naming_compliance
import csv


# Directories
TESTS_DIR = "mbpp_files/tests"
SOLUTIONS_DIR = "mutants/mbpp_files/solutions"
OLD_SOLUTIONS_DIR = "mbpp_files/solutions"  # Directory with original solutions
TIMEOUT = 10  # Time limit in seconds for each test case
THRESHOLD = 0  # Threshold for the number of allowed passed mutants percent
DATASET = "mbpp"  # Name of the dataset





def load_module(filepath):
    """Load a Python module from a given file path."""
    module_name = os.path.basename(filepath).replace(".py", "")
    spec = importlib.util.spec_from_file_location(module_name, filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def extract_base_function_name(filepath):
    """Extract the base function name from the old solution."""
    with open(filepath, "r") as file:
        content = file.read()
    match = re.search(r"def\s+(\w+)\s*\(", content)
    if match:
        return match.group(1)
    raise ValueError(f"Base function name not found in {filepath}")


def extract_mutant_function_names(filepath):
    """Extract all mutant function names from the mutated solution file."""
    with open(filepath, "r") as file:
        content = file.read()
    matches = re.findall(r"def\s+(x_\w+__mutmut_\d+)\s*\(", content)
    return matches


def run_test_in_process(solution_path, test_path, function_name, queue):
    """Run the test in a separate process and send the result to a queue."""
    try:
        # Load the test module
        test_module = load_module(test_path)

        # Load the solution module
        solution_module = load_module(solution_path)

        # Get the candidate function
        candidate_function = getattr(solution_module, function_name)

        # Run the test
        test_module.check(candidate_function)
        queue.put("pass")
    except Exception:
        queue.put("fail")


def run_tests():
    """Run tests for all mutants and calculate pass percentage for each."""
    failed_mutant_patch = 0
    test_files = sorted([f for f in os.listdir(TESTS_DIR) if f.startswith("test_") and f.endswith(".py")])
    solution_files = sorted([f for f in os.listdir(SOLUTIONS_DIR) if f.startswith("solution_") and f.endswith(".py")])
    old_solution_files = sorted(
        [f for f in os.listdir(OLD_SOLUTIONS_DIR) if f.startswith("solution_") and f.endswith(".py")])

    if not (len(test_files) == len(solution_files) == len(old_solution_files)):
        print("Error: Mismatched number of test, solution, and old solution files.")
        return

    # Create a log file
    date_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_filename = f"{DATASET}_{THRESHOLD}_{date_str}.log"
    csv_filename = f"{DATASET}_{THRESHOLD}_{date_str}.csv"
    with open(csv_filename, mode="a", newline="") as file:
        writer = csv.writer(file)
        header = ["Solution", "Total Mutants", "Passed Mutants", "Pass Percentage",
                  "Average Cyclomatic Complexity (Mutated)", "Average Cyclomatic Complexity (Original)",
                  "Average Function Length (Mutated)", "Average Function Length (Original)",
                  "Average Comment Ratio (Mutated)", "Average Comment Ratio (Original)",
                  "Average Naming Compliance (Mutated)", "Average Naming Compliance (Original)",
                  "Failed Patch"]
        writer.writerow(header)
    with open(log_filename, "w", encoding="utf-8") as log_file:

        for test_file, solution_file, old_solution_file in zip(test_files, solution_files, old_solution_files):
            test_path = os.path.join(TESTS_DIR, test_file)
            solution_path = os.path.join(SOLUTIONS_DIR, solution_file)
            old_solution_path = os.path.join(OLD_SOLUTIONS_DIR, old_solution_file)

            log_file.write(f"\nRunning tests for: {test_file} and {solution_file}\n")
            print(f"\nRunning tests for: {test_file} and {solution_file}")

            try:
                # Extract mutant function names from the mutated solution
                mutant_function_names = extract_mutant_function_names(solution_path)

                total_mutants = len(mutant_function_names)
                passed_mutants = 0

                # Run tests for each mutant function
                for mutant_function_name in mutant_function_names:
                    queue = Queue()
                    process = Process(
                        target=run_test_in_process,
                        args=(solution_path, test_path, mutant_function_name, queue),
                    )
                    process.start()
                    process.join(TIMEOUT)

                    if process.is_alive():
                        process.terminate()
                        process.join()
                        log_file.write(f"⏰ Mutant {mutant_function_name} timed out.\n")
                        print(f"⏰ Mutant {mutant_function_name} timed out.")
                    else:
                        result = queue.get()
                        if result == "pass":
                            log_file.write(f"✅ Mutant {mutant_function_name} passed.\n")
                            print(f"✅ Mutant {mutant_function_name} passed.")
                            passed_mutants += 1
                        else:
                            log_file.write(f"❌ Mutant {mutant_function_name} failed.\n")
                            print(f"❌ Mutant {mutant_function_name} failed.")

                # Calculate and display percentage of passed mutants
                pass_percentage = (passed_mutants / total_mutants) * 100
                log_file.write(f"\nSummary for {solution_file}:\n")
                log_file.write(f"Total Mutants: {total_mutants}\n")
                log_file.write(f"Passed Mutants: {passed_mutants}\n")
                log_file.write(f"Pass Percentage: {pass_percentage:.2f}%\n")
                print(f"\nSummary for {solution_file}:")
                print(f"Total Mutants: {total_mutants}")
                print(f"Passed Mutants: {passed_mutants}")
                print(f"Pass Percentage: {pass_percentage:.2f}%")

                if pass_percentage > THRESHOLD:
                    failed_mutant_patch += 1
            except Exception as e:
                error_msg = f"❌ Error processing {solution_file}: {str(e)}\n"
                log_file.write(error_msg)
                print(error_msg)
                log_file.write(traceback.format_exc())
            log_file.write(f"Number of failed patches so far: {failed_mutant_patch}\n")
            print(f"Number of failed patches so far: {failed_mutant_patch}")

            # Calculate metrics and write to csv
            with open(csv_filename, mode="a", newline="") as file:
                with open(solution_path, mode="r") as src_code:
                    mutate_code_content = src_code.read()
                with open(old_solution_path, mode="r") as target_code:
                    trg_code_content = target_code.read()
                    # input(trg_code_content)
                writer = csv.writer(file)

                mutate_function_length = calculate_function_lengths(mutate_code_content, mutant_function_names)
                trg_function_length = calculate_function_lengths(trg_code_content)

                mutate_comment_ratio = calculate_comment_ratio(mutate_code_content, mutant_function_names)
                trg_comment_ratio = calculate_comment_ratio(trg_code_content)

                mutate_naming_compliance = calculate_naming_compliance(mutate_code_content)
                trg_naming_compliance = calculate_naming_compliance(trg_code_content)

                row_contents = [solution_file, total_mutants, passed_mutants, pass_percentage,
                                calculate_cyclomatic_complexity(mutate_code_content)/float(len(mutant_function_names)),
                                calculate_cyclomatic_complexity(trg_code_content),
                                mutate_function_length, trg_function_length,
                                mutate_comment_ratio, trg_comment_ratio,
                                mutate_naming_compliance, trg_naming_compliance,
                                pass_percentage <= THRESHOLD]
                input(row_contents)
                writer.writerow(row_contents)

        # Calculate mutation score
        detected_mutants = len(solution_files) - failed_mutant_patch
        mutation_score = (detected_mutants / len(solution_files)) * 100

        # Final Summary
        final_summary = (
            f"\n=== Final Summary ===\n"
            f"Dataset: {DATASET}\n"
            f"Threshold: {THRESHOLD}\n"
            f"Total Solutions: {len(solution_files)}\n"
            f"Failed Patches: {failed_mutant_patch}\n"
            f"Detected Patches: {detected_mutants}\n"
            f"Mutation Score: {mutation_score:.2f}%\n"
        )
        log_file.write(final_summary)
        print(final_summary)


if __name__ == "__main__":
    run_tests()
