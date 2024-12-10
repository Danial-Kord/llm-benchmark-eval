import os
import importlib.util
from datetime import datetime

# Directories for tests and solutions
TESTS_DIR = "humaneval_files/tests"
SOLUTIONS_DIR = "humaneval_files/solutions"
LOG_FILE = "test_results.log"



def run_tests():
    total_tests = 0
    passed_tests = 0

    # Open the log file for writing
    with open(LOG_FILE, "w") as log:
        # Write the header to the log file
        log.write(f"Test Run - {datetime.now()}\n")
        log.write("=" * 50 + "\n")

        # List all test files
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
            result_message = f"Running test for: {test_file}\n"
            print(result_message, end="")
            log.write(result_message)

            # Load the solution module
            solution_path = os.path.join(SOLUTIONS_DIR, solution_file)
            solution_spec = importlib.util.spec_from_file_location("solution", solution_path)
            solution_module = importlib.util.module_from_spec(solution_spec)
            solution_spec.loader.exec_module(solution_module)

            # Load the test code
            test_path = os.path.join(TESTS_DIR, test_file)
            with open(test_path, "r") as f:
                test_code = f.read()

            # Execute the test
            try:
                # Make the solution functions available to the test code
                exec(test_code, solution_module.__dict__)
                passed_tests += 1
                result_message = f"Test {test_file} PASSED!\n"
                print(result_message, end="")
                log.write(result_message)
            except Exception as e:
                result_message = f"Test {test_file} FAILED! Error: {e}\n"
                print(result_message, end="")
                log.write(result_message)

        # Calculate and log the pass percentage
        pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0
        summary_message = (
            f"\nSummary:\n"
            f"Total Tests: {total_tests}\n"
            f"Passed Tests: {passed_tests}\n"
            f"Failed Tests: {total_tests - passed_tests}\n"
            f"Pass Percentage: {pass_percentage:.2f}%\n"
        )
        print(summary_message)
        log.write("=" * 50 + "\n")
        log.write(summary_message)
        log.write(f"Test Run Completed - {datetime.now()}\n")

if __name__ == "__main__":
    run_tests()
