import re

def mutate_code(code):
    """
    Introduce mutations into the canonical solution.
    Example: Change '+' to '-'
    """
    mutations = [
        (r'\+', '-'),  # Change '+' to '-'
        (r'\-', '+'),  # Change '-' to '+'
        (r'>', '<'),  # Change '>' to '<'
        (r'<', '>'),  # Change '<' to '>'
        (r'if ', 'if not '),  # Negate conditions

    ]

    mutated_code = code
    for pattern, replacement in mutations:
        mutated_code = re.sub(pattern, replacement, mutated_code)
    # print(mutated_code == code)
    # print(mutated_code)
    # print("==========")
    # print(code)
    # input()
    return mutated_code


