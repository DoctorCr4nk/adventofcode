#!/usr/bin/python3.12
## Description  Advent of Code 2024
## Link:        https://adventofcode.com/2024/day/2

import argparse

def load_input_file(task_day: str='2', type: str='data'):
    file1 = open('2024/input_data/day' + task_day + '.' + type, 'r')
    return file1.readlines()

def clean_data(dirty_data: list) -> list:
    clean_data = list()
    for dirty_data_set in dirty_data:
        clean_data_set = list()
        for entry in dirty_data_set.replace('\n','').split(' '):
            clean_data_set.append(int(entry))
        clean_data.append(clean_data_set)
    return clean_data

parser = argparse.ArgumentParser()
parser.add_argument('-e', '--example', action='store_true', help="Use example input data")
parser.add_argument('-d', '--day', default='2', help="Use input data of this day")
args = vars(parser.parse_args())

column_left = list()
column_right = list()
result_1 = 0
result_2 = 0

if args['example']:
    data_type = 'example'
else:
    data_type = 'data'

clean_data_list = clean_data(load_input_file(args['day'], data_type))
for report in clean_data_list:
    is_safe = True

    for index in range(1,len(report)-1):
        if abs(report[index - 1] - report[index]) > 3 \
            or abs(report[index] - report[index + 1]) > 3:
            is_safe = False
            break
        if not ((report[index - 1] > report[index] > report[index + 1]) \
            or (report[index - 1] < report[index] < report[index + 1])):
            is_safe = False
            break
    if is_safe:
        result_1 += 1

print('Result 2.0: ' + str(result_1))
print('Result 2.1: ' + str(result_2))
