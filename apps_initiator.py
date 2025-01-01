import os
from datasets import load_dataset

# Load the APS dataset
dataset = load_dataset("codeparrot/apps", split="all")

# Directories for test and solution files
test_dir = "aps_files/tests"
solution_dir = "aps_files/solutions"

# Create directories if they don't exist
os.makedirs(test_dir, exist_ok=True)
os.makedirs(solution_dir, exist_ok=True)


input(dataset[0]['solutions'][0])

# Process the dataset
for idx, entry in enumerate(dataset):
    # Extract solution code and test cases
    solution_code = entry.get("code", "")
    test_cases = entry.get("test_list", [])
    task_description = entry.get("text", "")  # Task description (problem statement)

    print(f"Processing example {idx} with {len(test_cases)} test cases.")

    # Save solution data to a file
    solution_file_path = os.path.join(solution_dir, f"solution_{idx}.py")
    with open(solution_file_path, "w") as solution_file:
        solution_file.write(f"""# Task Description\n{task_description}\n\n# Solution Code\n{solution_code}\n""")