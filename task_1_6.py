# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.

import re

operations = {
    "*": lambda x, y: str(float(x) * float(y)),
    "/": lambda x, y: str(float(x) / float(y)),
    "+": lambda x, y: str(float(x) + float(y)),
    "-": lambda x, y: str(float(x) - float(y))
}

prior_reg_exp = r"\((.+?)\)"
operations_reg_exp = r"(-?\d+(?:\.\d+)?)\s*\{}\s*(-?\d+(?:\.\d+)?)"


def eval_function(exp: str) -> str:
    while match := re.search(prior_reg_exp, exp):
        exp: str = exp.replace(match.group(0), eval_function(match.group(1)))

    for symbol, action in operations.items():
        while match := re.search(operations_reg_exp.format(symbol), exp):
            exp: str = exp.replace(match.group(0), action(*match.groups()))

    return exp


task = "1+2*3"

print(eval_function(task), eval(task), sep = ' <- my try      eval -> ')