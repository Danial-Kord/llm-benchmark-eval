from datasets import load_dataset
from mumut import Mutator
from mumut.reports import MutationTestingReport

# Load the HumanEval dataset from Hugging Face
print("Loading HumanEval dataset...")
dataset = load_dataset("openai_humaneval")

# Function to run mutation tests on a single problem
def run_mutation_test(problem_id, code):
    print(f"\nRunning mutation tests on problem ID: {problem_id}")

    # Save code to a temporary Python file
    temp_file = f"{problem_id}.py"
    with open(temp_file, "w") as f:
        f.write(code)

    try:
        # Initialize the mutator
        mutator = Mutator(source_code_path=temp_file)

        # Generate mutants
        mutants = mutator.generate_mutants()

        print(f"Generated {len(mutants)} mutants for {problem_id}.")

        # Run tests on mutants
        test_results = mutator.run_tests(mutants)

        # Generate report
        report = MutationTestingReport(test_results)
        report_summary = report.generate_summary()

        # Print report summary
        print(f"Mutation Testing Report for problem ID: {problem_id}")
        print(report_summary)

        # Save report to a file
        report.save_to_file(f"{problem_id}_mutation_report.txt")
    finally:
        # Clean up temporary file
        import os
        if os.path.exists(temp_file):
            os.remove(temp_file)


# Run mutation tests on each problem in the dataset
for idx, entry in enumerate(dataset["test"]):  # Use the "test" split
    problem_id = f"problem_{idx + 1}"
    code = entry["prompt"] + entry["canonical_solution"]  # Combine prompt and solution
    run_mutation_test(problem_id, code)
