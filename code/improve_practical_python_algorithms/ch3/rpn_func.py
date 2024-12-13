import math

RPN_FUNCTIONS = {
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
}

RPN_OPERATORS = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
    "%": lambda a, b: a % b,
}

RPN_CONSTANTS = {"pi": math.pi}


def calc_rpn(src):
    stack = []
    tokens = src.split(" ")
    for t in tokens:
        if t in RPN_FUNCTIONS:
            a = stack.pop()
            stack.append(RPN_FUNCTIONS[t](a))
        elif t in RPN_OPERATORS:
            b = stack.pop()
            a = stack.pop()
            stack.append(RPN_OPERATORS[t](a, b))
        elif t in RPN_CONSTANTS:
            stack.append(RPN_CONSTANTS[t])
        else:
            stack.append(float(t))
    return stack.pop()


# テスト
def test_rpn_func():
    assert calc_rpn("0 sin") == 0
    assert calc_rpn("pi 2 / sin") == 1.0
    assert calc_rpn("pi 3 / cos") == math.cos(math.pi / 3)
