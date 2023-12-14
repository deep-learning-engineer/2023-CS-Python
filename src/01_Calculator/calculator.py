from operator import add, mul, sub, truediv
from typing import List

ops = {"+": add, "-": sub, "*": mul, "/": truediv}


def prefix_evaluate(prefix_evaluation):
    if not prefix_evaluation:
        return None

    stack = []
    prefix_evaluation = prefix_evaluation.split() \
        if isinstance(prefix_evaluation, str) \
        else prefix_evaluation

    for token in reversed(prefix_evaluation):
        if token.isdigit():
            stack.append(int(token))
        elif token in ops:
            operand1 = stack.pop()
            operand2 = stack.pop()

            result = ops[token](operand1, operand2)
            stack.append(result)

    return stack[0]


def to_prefix(equation: str) -> List[str]:
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2}
    operators = set("+*-/")
    output = []
    stack: List[object] = []

    for token in reversed(equation.split()):
        if token.isdigit():
            output.append(token)
        elif token in operators:
            while stack and stack[-1] != ")" and precedence[token] <= precedence.get(stack[-1], 0):
                output.append(stack.pop())
            stack.append(token)
        elif token == ")":
            stack.append(token)
        elif token == "(":
            while stack and stack[-1] != ")":
                output.append(stack.pop())
            stack.pop()

    while stack:
        output.append(stack.pop())

    return list(reversed(output))


def calculate(equation: str) -> int:
    return prefix_evaluate(to_prefix(equation))
