#!/usr/bin/python3.12
## Description  Advent of Code 2024
## Link:        https://adventofcode.com/2024/day/3

import argparse
import re

def load_input_file(task_day: str, type: str='data'):
    file1 = open('input_data/day' + task_day + '.' + type, 'r')
    return file1.readlines()

def check_if_zahl(zahl_string: str) -> bool:
    is_zahl = False
    if len(zahl_string) <= 3:
        try:
            int(zahl_string)
        except ValueError:
            return False
        return True
    else:
        return False


parser = argparse.ArgumentParser()
parser.add_argument('-e', '--example', action='store_true', help="Use example input data")
parser.add_argument('-d', '--day', default='3', help="Use input data of this day")
args = vars(parser.parse_args())

column_left = list()
column_right = list()
result_1 = 0
result_2 = 0

if args['example']:
    data_type = 'example'
else:
    data_type = 'data'

for line in load_input_file(args['day'], data_type):
    for mulop in line.split('mul(')[1:]:

        if len(mulop.split(')')) < 2:
            continue
        else:
            mulop = mulop.split(')')[0]

        if len(mulop.split(',')) != 2:
            continue
        else:
            mulop = mulop.split(',')

        if len(mulop) > 7:
            continue

        if check_if_zahl(mulop[0]) and check_if_zahl(mulop[1]):
            result_1 += int(mulop[0]) * int(mulop[1])
        else:
            print("Issue with: " + str(mulop))

print('Result 1.0: ' + str(result_1))
print('Result 1.1: ' + str(result_2))
