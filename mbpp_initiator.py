import os
from datasets import load_dataset

# Load the dataset
dataset = load_dataset("google-research-datasets/mbpp", "full")

# Directories for test and solution files
test_dir = "mbpp_files/tests"
solution_dir = "mbpp_files/solutions"

# Create directories if they don't exist
os.makedirs(test_dir, exist_ok=True)
os.makedirs(solution_dir, exist_ok=True)

# Process the dataset
for idx, entry in enumerate(dataset['test']):
    # Extract solution code and test cases
    solution_code = entry.get("code", "")
    test_cases = entry.get("test_list", [])
    print(f"Processing example {idx} with {len(test_cases)} test cases.")

    # Save solution data to a file
    solution_file_path = os.path.join(solution_dir, f"solution_{idx}.py")
    with open(solution_file_path, "w") as solution_file:
        solution_file.write(f"# Solution Code\n{solution_code}\n")

    # Create a `check` function for the test cases
    check_function = "def check(candidate):\n"
    for case in test_cases:
        # Replace explicit function calls with `candidate`
        generalized_case = case.replace(case.split("(")[0], "candidate", 1)
        check_function += f"    assert {generalized_case}\n"

    # Save the `check` function to a file
    test_file_path = os.path.join(test_dir, f"test_{idx}.py")
    with open(test_file_path, "w") as test_file:
        test_file.write(f"# Test Cases\n{check_function}\n")

print(f"Test and solution files have been saved in '{test_dir}' and '{solution_dir}' directories.")
