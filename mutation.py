from datasets import load_dataset

# Load the dataset
dataset = load_dataset("openai_humaneval")

# Access the test split
examples = dataset["test"]

# Extract a specific example
example = examples[0]
prompt = example["prompt"]
canonical_solution = example["canonical_solution"]
test_cases = example["test"]

# Save these to files for mutation testing (optional)
with open("solution.py", "w") as f:
    f.write(prompt)
    f.write(canonical_solution)
with open("test_solution.py", "w") as f:
    f.write(test_cases)
