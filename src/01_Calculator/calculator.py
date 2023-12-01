from operator import add, mul, sub
from operator import truediv as div
from typing import List

operators = {'+': add, '-': sub, '*': mul, '/': div}


def prefix_evaluate(prefix_evaluation: List[str]) -> int:
    digits = []

    for el in prefix_evaluation[::-1]:
        if el in operators:
            a, b = digits.pop(), digits.pop()
            digits.append(operators[el](a, b))
        else:
            digits.append(int(el))

    return digits[0]


def to_prefix(equation: str) -> List[str]:
    op_stack = []
    prefix = []

    for el in equation.split()[::-1]:
        if el.isdigit():
            prefix.append(el)
        elif el == ')' or el in operators:
            op_stack.append(el)
        elif el == '(':
            while op_stack and op_stack[-1] != ')':
                prefix.append(op_stack.pop())
            op_stack.pop()

            if ')' not in op_stack:
                while op_stack:
                    if op_stack[-1] == ')':
                        op_stack.pop()
                    else:
                        prefix.append(op_stack.pop())

    while op_stack:
        prefix.append(op_stack.pop())

    return prefix[::-1]


def calculate(equation: str) -> int:
    return prefix_evaluate(to_prefix(equation))
