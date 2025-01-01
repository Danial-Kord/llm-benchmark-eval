import os
import re
import unittest
import importlib.util
from datasets import load_dataset
from mutator import mutate_code

def run_tests(solution_file, test_file):
    try:
        spec = importlib.util.spec_from_file_location("solution", solution_file)
        solution = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(solution)

        spec = importlib.util.spec_from_file_location("test_solution", test_file)
        test_solution = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(test_solution)

        loader = unittest.TestLoader()
        suite = loader.loadTestsFromModule(test_solution)
        runner = unittest.TextTestRunner()
        result = runner.run(suite)
        return result.wasSuccessful()
    except Exception as e:
        print(f"Error running tests: {e}")
        return False


# Load HumanEval dataset
dataset = load_dataset("openai_humaneval")
examples = dataset["test"]

# Directory setup
os.makedirs("solutions", exist_ok=True)
os.makedirs("tests", exist_ok=True)

# Process examples
for idx, example in enumerate(examples):
    prompt = example["prompt"]
    canonical_solution = example["canonical_solution"]
    test_code = example["test"]

    # Save files
    with open(f"solutions/solution_{idx}.py", "w", encoding="utf-8") as solution_file:
        solution_file.write(prompt + canonical_solution)

    with open(f"tests/test_solution_{idx}.py", "w", encoding="utf-8") as test_file:
        test_file.write(test_code)

    # Mutate code
    mutated_solution = mutate_code(canonical_solution)
    with open(f"solutions/mutated_solution_{idx}.py", "w", encoding="utf-8") as mutated_file:
        mutated_file.write(prompt + mutated_solution)

# Run tests
total_mutations = len(examples)
mutations_killed = 0

for idx in range(total_mutations):
    original_success = run_tests(f"solutions/solution_{idx}.py", f"tests/test_solution_{idx}.py")
    mutated_success = run_tests(f"solutions/mutated_solution_{idx}.py", f"tests/test_solution_{idx}.py")

    if not mutated_success:
        mutations_killed += 1

    print(f"Test {idx}:")
    print(f"  Original Solution Passed: {original_success}")
    print(f"  Mutated Solution Passed: {mutated_success}")

mutation_score = (mutations_killed / total_mutations) * 100
print(f"Mutation Score: {mutation_score:.2f}%")


with open("mutation_results.log", "w") as log_file:
    for idx in range(len(examples)):
        original_success = run_tests(f"solutions/solution_{idx}.py", f"tests/test_solution_{idx}.py")
        mutated_success = run_tests(f"solutions/mutated_solution_{idx}.py", f"tests/test_solution_{idx}.py")

        log_file.write(f"Test {idx}:\n")
        log_file.write(f"  Original Solution Passed: {original_success}\n")
        log_file.write(f"  Mutated Solution Passed: {mutated_success}\n")

    log_file.write(f"Mutation Score: {mutation_score:.2f}%\n")
