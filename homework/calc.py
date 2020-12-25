# calculator
import operator
from pathlib import Path
import datetime

x = '9' #input('enter single input containing the expression in polish notation')


def valid_operations(j):

    operations = {'add', '+', 'sub', '-', 'mul', '*', 'div', '/'}

    for i in operations:
        if j[0] == i:
            return True
    return False


def check_value(y):
    for i in range(1, len(y)):
        if not y[i].replace('.', '', 1).isdigit():
            return False
    return True


def calculate_result(r):
    t = r.split()
    if len(t) < 3:
        return 'Error: Not completed'
    if valid_operations(t) and check_value(t):
        operator_converted = {'add': operator.add,
                              '+': operator.add,
                              'sub': operator.sub,
                              '-': operator.sub,
                              'mul': operator.mul,
                              '*': operator.mul,
                              'div': operator.truediv,
                              '/': operator.truediv}

        result = operator_converted[t[0]](float(t[1]), float(t[2]))
        if result.is_integer():
            return f'Result: {int(result)}'

        return f'Result{result}'
    elif not valid_operations(r):
        return 'Error: Entered not valid operator'
    else:
        return 'Error: Entered not valid operands'


def write_to_log(d):
    work_dir = Path.home().joinpath('Desktop/python_test')

    with open(work_dir.joinpath('log.txt'), 'w+') as endFile:
        endFile.write(f'Expression: {x}\n'
                      f'{d}\n'
                      f'System Time: {datetime.datetime.now()}')


write_to_log((calculate_result(x)))