import os
import re
import unittest
import importlib.util
from datasets import load_dataset
from mutator import mutate_code


# Load HumanEval dataset
dataset = load_dataset("openai_humaneval")
examples = dataset["test"]

# Directory setup
os.makedirs("humaneval_files/solutions", exist_ok=True)
os.makedirs("humaneval_files/tests", exist_ok=True)

# Process examples
for idx, example in enumerate(examples):
    prompt = example["prompt"]
    canonical_solution = example["canonical_solution"]
    test_code = example["test"]

    # Save files
    with open(f"humaneval_files/solutions/solution_{idx+1}.py", "w", encoding="utf-8") as solution_file:
        solution_file.write(prompt + canonical_solution)

    with open(f"humaneval_files/tests/test_{idx+1}.py", "w", encoding="utf-8") as test_file:
        test_file.write(test_code)

