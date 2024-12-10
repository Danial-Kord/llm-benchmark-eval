import os
import importlib.util
import traceback

# Directories
TESTS_DIR = "humaneval_files/tests"
SOLUTIONS_DIR = "humaneval_files/solutions"

def load_module(filepath):
    """Load a Python module from a given file path."""
    module_name = os.path.basename(filepath).replace(".py", "")
    spec = importlib.util.spec_from_file_location(module_name, filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def get_first_function_name(module):
    """Retrieve the first function name defined in a module."""
    for attr_name in dir(module):
        attr = getattr(module, attr_name)
        if callable(attr) and attr.__module__ == module.__name__:
            return attr_name
    raise ValueError("No callable function found in the solution module.")

def run_tests():
    indexs_to_remove = []
    """Run all test-solution pairs and calculate pass percentage."""
    test_files = sorted([f for f in os.listdir(TESTS_DIR) if f.startswith("test_") and f.endswith(".py")])
    solution_files = sorted([f for f in os.listdir(SOLUTIONS_DIR) if f.startswith("solution_") and f.endswith(".py")])

    if len(test_files) != len(solution_files):
        print("Error: Mismatched number of test and solution files.")
        return

    total_tests = len(test_files)
    passed_tests = 0

    for test_file, solution_file in zip(test_files, solution_files):
        test_path = os.path.join(TESTS_DIR, test_file)
        solution_path = os.path.join(SOLUTIONS_DIR, solution_file)


        try:
            # Load modules
            test_module = load_module(test_path)
            solution_module = load_module(solution_path)

            # Dynamically get the function name from the solution module
            function_name = get_first_function_name(solution_module)
            candidate_function = getattr(solution_module, function_name)

            # Run the test
            test_module.check(candidate_function)
            # print(f"✅ {test_file} passed.")
            passed_tests += 1
        except Exception as e:
            indexs_to_remove.append(test_path)
            indexs_to_remove.append(solution_path)
            print(f"Running test for: {test_file} and {solution_file}")
            print(f"❌ {test_file} failed.")
            print(traceback.format_exc())

    # Calculate and display percentage of passed tests
    pass_percentage = (passed_tests / total_tests) * 100
    print(f"\nSummary:")
    print(f"Total Tests: {total_tests}")
    print(f"Passed Tests: {passed_tests}")
    print(f"Pass Percentage: {pass_percentage:.2f}%")
    for index in indexs_to_remove:
        os.remove(index)

if __name__ == "__main__":
    run_tests()
