# check if the expression contains only numbers, operators: + - * /, parenthesis and spaces

def is_valid_expression(exp):
    valid = ('+', '-', '*', '/', '(', ')', ' ')
    for x in exp:
        if x not in valid and not x.isdigit():
            return False
    return True