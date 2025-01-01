import ast
import re


class CyclomaticComplexityVisitor(ast.NodeVisitor):
    def __init__(self):
        self.complexity = 1  # Starts at 1 (baseline complexity)

    def visit_If(self, node):
        self.complexity += 1
        self.generic_visit(node)

    def visit_For(self, node):
        self.complexity += 1
        self.generic_visit(node)

    def visit_While(self, node):
        self.complexity += 1
        self.generic_visit(node)

    def visit_Try(self, node):
        self.complexity += 1
        self.generic_visit(node)

    def visit_ExceptHandler(self, node):
        self.complexity += 1
        self.generic_visit(node)

    def visit_BoolOp(self, node):
        # Logical operators like "and" and "or"
        if isinstance(node.op, (ast.And, ast.Or)):
            self.complexity += 1
        self.generic_visit(node)


def calculate_cyclomatic_complexity(source_code):
    """Calculate the Cyclomatic Complexity of the given Python source code."""
    try:
        tree = ast.parse(source_code)
        visitor = CyclomaticComplexityVisitor()
        visitor.visit(tree)
        return visitor.complexity
    except SyntaxError as e:
        print(f"Syntax error in code: {e}")
        return None


def calculate_comment_ratio(source_code, function_base_names=None):
    """
    Calculate the comment ratio for specific functions in the given Python source code.

    :param source_code: The full Python source code as a string.
    :param function_base_names: A list of function names to focus on, or None to include all.
    :return: The average comment ratio for the specified functions.
    """
    try:
        tree = ast.parse(source_code)
        comment_ratios = []

        class FunctionCommentVisitor(ast.NodeVisitor):
            def __init__(self):
                self.function_code_lines = []

            def visit_FunctionDef(self, node):
                if function_base_names is None or node.name in function_base_names:
                    start_line = node.lineno - 1
                    end_line = max(
                        getattr(child, 'lineno', start_line) - 1 for child in ast.walk(node)
                    )
                    self.function_code_lines.append((start_line, end_line))
                self.generic_visit(node)

        # Extract lines for specified functions
        visitor = FunctionCommentVisitor()
        visitor.visit(tree)

        lines = source_code.splitlines()

        for start, end in visitor.function_code_lines:
            function_lines = lines[start:end + 1]
            total_lines = len(function_lines)
            comment_lines = sum(1 for line in function_lines if line.strip().startswith('#'))
            if total_lines > 0:
                comment_ratios.append(comment_lines / total_lines)

        # Return the average comment ratio for specified functions
        return sum(comment_ratios) / len(comment_ratios) if comment_ratios else 0

    except SyntaxError as e:
        print(f"Syntax error in code: {e}")
        return None


def calculate_function_lengths(source_code, function_base_names=None):
    """Calculate the lengths of all functions in the given Python source code."""
    try:
        tree = ast.parse(source_code)
        function_lengths = {}

        class FunctionLengthVisitor(ast.NodeVisitor):
            def visit_FunctionDef(self, node):
                start_line = node.lineno
                end_line = max(getattr(child, 'lineno', start_line) for child in ast.walk(node))
                if function_base_names is None or node.name in function_base_names:
                    function_lengths[node.name] = end_line - start_line + 1
                self.generic_visit(node)

        visitor = FunctionLengthVisitor()
        visitor.visit(tree)
        sum = 0
        for key in function_lengths:
            sum += function_lengths[key]
        return sum / float(len(function_lengths))
    except SyntaxError as e:
        print(f"Syntax error in code: {e}")
        return None


def calculate_naming_compliance(source_code, naming_pattern="^[a-z_][a-z0-9_]*$"):
    """Calculate the naming compliance of variables, functions, and classes in the given source code.

    :param source_code: The Python source code to analyze.
    :param naming_pattern: A regex pattern for compliant names.
    :return: The ratio of compliant names to total names found.
    """
    try:
        tree = ast.parse(source_code)
        compliant_count = 0
        total_count = 0
        pattern = re.compile(naming_pattern)

        class NamingVisitor(ast.NodeVisitor):
            def visit_FunctionDef(self, node):
                nonlocal compliant_count, total_count
                total_count += 1
                if pattern.match(node.name):
                    compliant_count += 1
                self.generic_visit(node)

            def visit_ClassDef(self, node):
                nonlocal compliant_count, total_count
                total_count += 1
                if pattern.match(node.name):
                    compliant_count += 1
                self.generic_visit(node)

            def visit_Name(self, node):
                nonlocal compliant_count, total_count
                total_count += 1
                if pattern.match(node.id):
                    compliant_count += 1

        visitor = NamingVisitor()
        visitor.visit(tree)

        return compliant_count / total_count if total_count > 0 else 1
    except SyntaxError as e:
        print(f"Syntax error in code: {e}")
        return None


# Example Usage:
if __name__ == "__main__":
    code = """
# This is an example function
# It calculates cyclomatic complexity
def example_function(x):
    if x > 10:
        print("x is greater than 10")
    elif x == 10:
        print("x is equal to 10")
    else:
        for i in range(5):
            print(i)
    return x

def AnotherFunction():
    # This is another function
    print("This is another function.")
    for i in range(3):
        print(i)
    """
    specific_functions = ["example_function", "another_function"]
    complexity = calculate_cyclomatic_complexity(code)
    comment_ratio = calculate_comment_ratio(code, specific_functions)
    function_lengths = calculate_function_lengths(code, specific_functions)
    naming_compliance = calculate_naming_compliance(code)

    print(f"Cyclomatic Complexity: {complexity}")
    print(f"Comment Ratio: {comment_ratio:.2f}")
    print(f"Function Lengths: {function_lengths}")
    print(f"Naming Compliance: {naming_compliance:.2f}")
