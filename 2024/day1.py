#!/usr/bin/python3.12
## Description  Advent of Code 2024
## Link:        https://adventofcode.com/2024/day/1

import argparse

def load_input_file(task_day: str='1', type: str='data'):
    file1 = open('2024/input_data/day' + task_day + '.' + type, 'r')
    return file1.readlines()

def get_diff(number1_str: str, number2_str: str) -> int:
    number1 = int(number1_str)
    number2 = int(number2_str)
    if number1 > number2:
        return int(number1 - number2)
    elif number1 < number2:
        return int(number2 - number1)
    else:
        return 0

parser = argparse.ArgumentParser()
parser.add_argument('-e', '--example', action='store_true', help="Use example input data")
parser.add_argument('-d', '--day', default='1', help="Use input data of this day")
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
    column_left.append(line.split()[0])
    column_right.append(line.split()[1])

column_left.sort()
column_right.sort()

for number in range(0,len(column_left)):
    result_1 = result_1 + get_diff(column_left[number], column_right[number])

multiply_table = dict()
i = 0
while i < len(column_right):
    j = 0
    while i+j < len(column_right) and column_right[i] == column_right[i+j]:
        j += 1
    multiply_table[column_right[i]] = j
    i += j

similarity = 0
for number in column_left:
    if number in multiply_table.keys():
        result_2 += int(number) * multiply_table[number]

print('Result 1.0: ' + str(result_1))
print('Result 1.1: ' + str(result_2))
