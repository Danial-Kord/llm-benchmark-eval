from datasets import load_dataset
import os

# Load HumanEval dataset
dataset = load_dataset("openai_humaneval")["test"]

# Create directories for storing solutions and tests
os.makedirs("humaneval_solutions", exist_ok=True)
os.makedirs("humaneval_tests", exist_ok=True)

# Save each example's solution and test cases
for idx, example in enumerate(dataset):
    prompt = example["prompt"]
    canonical_solution = example["canonical_solution"]
    test_code = example["test"]

    # Save the solution
    with open(f"humaneval_solutions/solution_{idx}.py", "w") as solution_file:
        solution_file.write(prompt + canonical_solution)

    # Save the test cases
    with open(f"humaneval_tests/test_solution_{idx}.py", "w") as test_file:
        test_file.write(test_code)
