import os
import importlib.util
import random
from datetime import datetime

# Directories for tests and solutions
TESTS_DIR = "humaneval_files/tests"
SOLUTIONS_DIR = "humaneval_files/solutions"
LOG_FILE = "mutation_testing_results.log"

def mutate_code(code):
    """
    Perform a simple mutation on the given code. For demonstration, we'll:
    - Replace `+` with `-` or vice versa
    - Replace `>` with `<` or vice versa
    """
    mutations = [
        (" + ", " - "),
        (" - ", " + "),
        (" > ", " < "),
        (" < ", " > "),

    ]
    mutation = random.choice(mutations)
    mutated_code = code.replace(*mutation)
    return mutated_code, mutation

def run_tests_with_solution(test_code, solution_code):
    """
    Run the test code against the provided solution code.
    Returns True if the test passes, False if it fails.
    """
    try:
        # Execute the test code in the solution's namespace
        exec(test_code, solution_code)
        return True  # Test passed
    except Exception:
        return False  # Test failed

def perform_mutation_testing():
    total_tests = 0
    killed_mutations = 0

    # Open the log file for writing
    with open(LOG_FILE, "w") as log:
        # Write the header to the log file
        log.write(f"Mutation Testing - {datetime.now()}\n")
        log.write("=" * 50 + "\n")

        # List all test and solution files
        test_files = sorted([f for f in os.listdir(TESTS_DIR) if f.endswith(".py")])
        solution_files = sorted([f for f in os.listdir(SOLUTIONS_DIR) if f.endswith(".py")])

        if len(test_files) != len(solution_files):
            message = "Mismatch between number of test and solution files!"
            print(message)
            log.write(message + "\n")
            return

        # Iterate over all test and solution files
        for test_file, solution_file in zip(test_files, solution_files):
            total_tests += 1
            log.write(f"Running mutation testing for: {test_file}\n")

            # Load the solution module
            solution_path = os.path.join(SOLUTIONS_DIR, solution_file)
            with open(solution_path, "r") as sf:
                original_solution_code = sf.read()

            # Load the test code
            test_path = os.path.join(TESTS_DIR, test_file)
            with open(test_path, "r") as tf:
                test_code = tf.read()

            # Apply mutation to the solution
            mutated_solution_code, mutation = mutate_code(original_solution_code)

            # Test the mutated solution
            solution_namespace = {}
            try:
                exec(mutated_solution_code, solution_namespace)
                test_result = run_tests_with_solution(test_code, solution_namespace)
                if not test_result:
                    killed_mutations += 1
                    log.write(f"Mutation {mutation} KILLED by test {test_file}\n")
                else:
                    log.write(f"Mutation {mutation} SURVIVED in test {test_file}\n")
            except Exception as e:
                log.write(f"Error in mutated solution {solution_file}: {e}\n")

        # Calculate mutation score
        mutation_score = (killed_mutations / total_tests) * 100 if total_tests > 0 else 0
        summary_message = (
            f"\nSummary:\n"
            f"Total Tests: {total_tests}\n"
            f"Killed Mutations: {killed_mutations}\n"
            f"Survived Mutations: {total_tests - killed_mutations}\n"
            f"Mutation Score: {mutation_score:.2f}%\n"
        )
        print(summary_message)
        log.write("=" * 50 + "\n")
        log.write(summary_message)
        log.write(f"Mutation Testing Completed - {datetime.now()}\n")

if __name__ == "__main__":
    perform_mutation_testing()
