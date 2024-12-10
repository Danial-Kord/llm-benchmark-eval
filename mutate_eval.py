import os
import importlib.util
import traceback
import re
from multiprocessing import Process, Queue
from typing import Any

# Directories
TESTS_DIR = "humaneval_files/tests"
SOLUTIONS_DIR = "mutants/humaneval_files/solutions"
OLD_SOLUTIONS_DIR = "humaneval_files/solutions"  # Directory with original solutions
TIMEOUT = 10  # Time limit in seconds for each test case


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


def run_test_in_process(candidate_function, check_function, queue):
    """Run the test in a separate process and send the result to a queue."""
    try:
        check_function(candidate_function)
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

    for test_file, solution_file, old_solution_file in zip(test_files, solution_files, old_solution_files):
        test_path = os.path.join(TESTS_DIR, test_file)
        solution_path = os.path.join(SOLUTIONS_DIR, solution_file)
        old_solution_path = os.path.join(OLD_SOLUTIONS_DIR, old_solution_file)

        print(f"\nRunning tests for: {test_file} and {solution_file}")

        try:
            # Load the test module
            test_module = load_module(test_path)

            # Extract base function name from the old solution
            base_function_name = extract_base_function_name(old_solution_path)

            # Extract mutant function names from the mutated solution
            mutant_function_names = extract_mutant_function_names(solution_path)

            # Load the solution module
            solution_module = load_module(solution_path)

            total_mutants = len(mutant_function_names)
            passed_mutants = 0

            # Run tests for each mutant function
            for mutant_function_name in mutant_function_names:
                candidate_function = getattr(solution_module, mutant_function_name)
                queue = Queue()
                process = Process(target=run_test_in_process, args=(candidate_function, test_module.check, queue))
                process.start()
                process.join(TIMEOUT)

                if process.is_alive():
                    process.terminate()
                    process.join()
                    print(f"⏰ Mutant {mutant_function_name} timed out.")
                else:
                    result = queue.get()
                    if result == "pass":
                        print(f"✅ Mutant {mutant_function_name} passed.")
                        passed_mutants += 1
                    else:
                        print(f"❌ Mutant {mutant_function_name} failed.")

            # Calculate and display percentage of passed mutants
            pass_percentage = (passed_mutants / total_mutants) * 100
            print(f"\nSummary for {solution_file}:")
            print(f"Total Mutants: {total_mutants}")
            print(f"Passed Mutants: {passed_mutants}")
            print(f"Pass Percentage: {pass_percentage:.2f}%")
            if passed_mutants > 0:
                failed_mutant_patch += 1
        except Exception as e:
            print(f"❌ Error processing {solution_file}: {str(e)}")
            print(traceback.format_exc())
        print("Number of failed patches: ", failed_mutant_patch)

    # Calculate mutation score
    detected_mutants = len(solution_files) - failed_mutant_patch
    mutation_score = (detected_mutants / len(solution_files)) * 100

    # Final Summary
    print("\n=== Final Summary ===")
    print(f"Total Solutions: {len(solution_files)}")
    print(f"Failed Patches: {failed_mutant_patch}")
    print(f"Detected Patches: {detected_mutants}")
    print(f"Mutation Score: {mutation_score:.2f}%")

if __name__ == "__main__":
    run_tests()
