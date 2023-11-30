from operator import add, mul, sub
from operator import truediv as div
from typing import List

operators = {'+': add, '-': sub, '*': mul, '/': div}


def prefix_evaluate(prefix_evaluation: List[str]) -> int:
    digits = []

    for el in prefix_evaluation.split()[::-1]:
        if el in operators:
            a, b = digits.pop(), digits.pop()
            digits.append(operators[el](a, b))
        else:
            digits.append(int(el))

    return digits[0]


def to_prefix(equation: str) -> List[str]:
    opstack = []
    prefix = []

    for el in equation.split()[::-1]:
        if el.isdigit():
            prefix.append(el)
        elif el == ')' or el in operators:
            opstack.append(el)
        elif el == '(':
            while opstack and opstack[-1] != ')':
                prefix.append(opstack.pop())
            opstack.pop()

            if ')' not in opstack:
                while opstack:
                    if opstack[-1] == ')':
                        opstack.pop()
                    else:
                        prefix.append(opstack.pop())

    while opstack:
        prefix.append(opstack.pop())

    return prefix[::-1]


def calculate(equation: str) -> int:
    return prefix_evaluate(to_prefix(equation))
