# check if the expression contains only numbers, operators: + - * /, parenthesis and spaces

import re

def is_valid_expression(exp):
    return bool(re.match('[0-9/*-+ ()]', exp))