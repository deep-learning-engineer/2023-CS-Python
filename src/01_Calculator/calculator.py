from operator import add, mul, sub, truediv
from typing import List, Optional, Union

ops = {"+": add, "-": sub, "*": mul, "/": truediv}

operators = {"+": add, "-": sub, "*": mul, "/": truediv}


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
    pass

def _split_if_string(string_or_list: Union[List[str], str]) -> List[str]:
    return string_or_list.split() if isinstance(string_or_list, str) else string_or_list


def prefix_evaluate(prefix_equation: Union[List[str], str]) -> Optional[int]:
    if not prefix_equation:
        return None
    prefix_equation = _split_if_string(prefix_equation)
    value_stack = []
    while prefix_equation:
        el = prefix_equation.pop()
        if el not in ops:
            value_stack.append(int(el))
        else:
            r_val = value_stack.pop()
            l_val = value_stack.pop()
            operation = ops[el]
            value_stack.append(operation(r_val, l_val))

    return value_stack[0]

def to_prefix(equation: str) -> str:
    op_stack = []
    prefix = []

    for el in equation.split()[::-1]:
        if el.isdigit():
            prefix.append(el)
        elif el == ")" or el in operators:
            op_stack.append(el)
        elif el == "(":
            while op_stack and op_stack[-1] != ")":
                prefix.append(op_stack.pop())
            op_stack.pop()

            if ")" not in op_stack:
                while op_stack:
                    if op_stack[-1] == ")":
                        op_stack.pop()
                    else:
                        prefix.append(op_stack.pop())
        pass

    while op_stack:
        prefix.append(op_stack.pop())

    return prefix[::-1]

def calculate(equation: str) -> int:
    return prefix_evaluate(to_prefix(equation))
