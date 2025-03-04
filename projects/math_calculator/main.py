import sys
from utils import validator
from utils import calculator

print('Chris\'s Mathematical Expression Validator &')
print('Enter your expression or \'exit\' to quit > ', end='')
expr = input()
if validator.is_valid_expression(expr):
    print(f'The result is: {calculator.calculator(expr)}')
elif expr == 'exit':
    print('bye bye!')
    sys.exit(0)
else:
    print('The expression is not valid.')