import os
import importlib.util
import sys

TESTS_DIR = "humaneval_files/tests"
SOLUTIONS_DIR = "humaneval_files/solutions"

# SOLUTIONS_DIR = "./mutants/humaneval_files/solutions"
def run_tests():
    # List all test files
    test_files = sorted([f for f in os.listdir(TESTS_DIR) if f.endswith(".py")])
    solution_files = sorted([f for f in os.listdir(SOLUTIONS_DIR) if f.endswith(".py")])

    if len(test_files) != len(solution_files):
        print("Mismatch between number of test and solution files!")
        sys.exit(1)

    # Iterate over all test and solution files
    for test_file, solution_file in zip(test_files, solution_files):
        print(f"Running test for: {test_file}")
        print(f"Solution file: {solution_file}")

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
            exec(test_code, solution_module.__dict__)
        except Exception as e:
            print(f"Test {test_file} FAILED! Error: {e}")
            sys.exit(1)  # Exit with an error code to indicate test failure

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
