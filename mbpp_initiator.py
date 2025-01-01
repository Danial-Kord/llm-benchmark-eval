import os
from openai import OpenAI

# Set your OpenAI API key directly in the code (if not already set in the environment)
os.environ["OPENAI_API_KEY"] = "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"

# Initialize OpenAI client
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")  # Explicitly pass the API key
)
from datasets import load_dataset

# Set up your OpenAI API key
# client.api_key = "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"



# Load the dataset
dataset = load_dataset("google-research-datasets/mbpp", "full")

# Directories for test and solution files
test_dir = "mbpp_files/tests"
solution_dir = "mbpp_files/solutions"
generated_solutions_dir = "mbpp_files/generated_solutions"

# Create directories if they don't exist
os.makedirs(test_dir, exist_ok=True)
os.makedirs(solution_dir, exist_ok=True)
os.makedirs(generated_solutions_dir, exist_ok=True)

# Process the dataset
for idx, entry in enumerate(dataset['test']):
    # Extract prompt and test cases
    prompt = entry.get("text", "")
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
    continue
    # Generate solution using GPT-4
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "developer",
                    "content": f"Write a Python solution for the following problem. Note that just write the main function and no example by the generated output:\n{prompt}\n",
                }
            ],
            model="gpt-4o",
        )
        generated_code = chat_completion.choices[0].message.content
        # Extract content from ```python to ```
        if "```python" in generated_code and "```" in generated_code:
            start = generated_code.index("```python") + len("```python")
            end = generated_code.index("```", start)
            generated_code = generated_code[start:end].strip()
        # Save the generated solution to a file
        generated_solution_path = os.path.join(generated_solutions_dir, f"generated_solution_{idx}.py")
        with open(generated_solution_path, "w") as generated_solution_file:
            generated_solution_file.write(f"# Generated Solution\n{generated_code}\n")
    except Exception as e:
        print(f"Error generating solution for example {idx}: {e}")

print(
    f"Test, solution, and generated solution files have been saved in '{test_dir}', '{solution_dir}', and '{generated_solutions_dir}' directories.")
