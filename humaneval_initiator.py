import os
import re
import unittest
import importlib.util
from datasets import load_dataset
from mutator import mutate_code

import os
import re
import unittest
import importlib.util
from datasets import load_dataset
from openai import OpenAI
os.environ["OPENAI_API_KEY"] = "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"

# Initialize OpenAI client
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")  # Explicitly pass the API key
)

# Load HumanEval dataset
dataset = load_dataset("openai_humaneval")
examples = dataset["test"]

# Directory setup
os.makedirs("humaneval_files/solutions", exist_ok=True)
os.makedirs("humaneval_files/tests", exist_ok=True)
os.makedirs("humaneval_files/generated_solutions", exist_ok=True)

# Process examples
for idx, example in enumerate(examples):
    prompt = example["prompt"]
    canonical_solution = example["canonical_solution"]
    test_code = example["test"]

    # Save files
    with open(f"humaneval_files/solutions/solution_{idx + 1}.py", "w", encoding="utf-8") as solution_file:
        solution_file.write(prompt + canonical_solution)

    with open(f"humaneval_files/tests/test_{idx + 1}.py", "w", encoding="utf-8") as test_file:
        test_file.write(test_code)

    os.makedirs(f"humaneval_files/generated_solutions/solutions_{idx+1}", exist_ok=True)

    # Generate 5 different solutions using GPT-4O
    for version in range(1, 6):
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
            generated_solution_path = f"humaneval_files/generated_solutions/solutions_{idx+1}/version_{version}.py"
            with open(generated_solution_path, "w", encoding="utf-8") as generated_solution_file:
                generated_solution_file.write(f"# Generated Solution\n{generated_code}\n")
        except Exception as e:
            print(f"Error generating solution for example {idx + 1}, version {version}: {e}")

print(
    f"Solutions, tests, and generated solutions have been saved in 'humaneval_files/solutions', 'humaneval_files/tests', and 'humaneval_files/generated_solutions' directories.")
