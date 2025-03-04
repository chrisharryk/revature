import sys
from datetime import datetime
import logging
from utils import validator
from utils import calculator

logging.basicConfig(filename='logs/app.log', level=logging.DEBUG)

try:
    today = datetime.today()
    print('Chris\'s Mathematical Expression Validator &')
    print('Enter your expression or \'exit\' to quit > ', end='')
    expr = input()
    is_valid = validator.is_valid_expression(expr)
    if is_valid:
        ans = calculator.calculator(expr)
        logging.info(f'{today} - INFO - Valid expression: {expr}')
        print(f'The result is: {ans}')
        logging.info(f'{today} - INFO - Result of the expression is: {ans}')
        logging.info(f'{today} - INFO - Exiting program')
    elif not is_valid:
        logging.error(f'{today} - ERROR - Invalid expression!')
        logging.info(f'{today} - INFO - Exiting program')
        print('Invalid expression')
    elif expr == 'exit':
        print('bye bye!')
        logging.info(f'{today} - INFO - Exiting program')
        sys.exit(0)
    else:
        print('The expression is not valid.')
except:
    print('Error calculating the expression')