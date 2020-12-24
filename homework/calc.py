# calculator
import operator
from pathlib import Path
import datetime

x = input('enter single input containing the expression in polish notation')
t = x.split()


def valid_operations(j):
    if len(j) < 3:
        return 'Not completed'
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
    if valid_operations(r) and check_value(r):
        operator_converted = {'add': operator.add,
                              '+': operator.add,
                              'sub': operator.sub,
                              '-': operator.sub,
                              'mul': operator.mul,
                              '*': operator.mul,
                              'div': operator.truediv,
                              '/': operator.truediv}

        result = operator_converted[r[0]](float(r[1]), float(r[2]))
        if result.is_integer():
            return f'Result: {int(result)}'

        return f'Result{result}'
    elif not valid_operations(r):
        return 'Error: Entered not valid operator'
    else:
        return 'Error: Entered not valid operands'


def write_to_log(d):
    work_dir = Path.home().joinpath('Desktop/python')

    with open(work_dir.joinpath('log.txt'), 'w+') as endFile:
        endFile.write(f'Expression: {x}\n'
                      f'{d}\n'
                      f'System Time: {datetime.datetime.now()}')


write_to_log((calculate_result(t)))
