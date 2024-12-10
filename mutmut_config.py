import os
import subprocess

# Path to your tests and solutions
TESTS_DIR = "humaneval_files/tests"
SOLUTIONS_DIR = "humaneval_files/solutions"

def run_mutation_test(mutation_filename):
    """
    Runs the test suite to verify the mutation.
    Returns True if the test suite fails (mutation killed).
    Returns False if the test suite passes (mutation survived).
    """
    try:
        # Execute all test files
        for test_file in os.listdir(TESTS_DIR):
            if test_file.endswith(".py"):
                subprocess.run(
                    ["python", os.path.join(TESTS_DIR, test_file)],
                    check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
                )
        return False  # Mutation survived
    except subprocess.CalledProcessError:
        return True  # Mutation killed
