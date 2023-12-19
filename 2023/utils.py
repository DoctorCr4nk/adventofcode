#!/usr/bin/python3.6

def read_file(path_file: str) -> list:
    input_data = list()
    file_input = open(path_file, 'r')
    for line in file_input.readlines():
        input_data.append(line.replace('\n', ''))
    file_input.close()
    return input_data

def calc_sum(numbers: list) -> int:
    sum = int()
    for number in numbers:
        sum += int(number)
    return sum

def get_id(line: str) -> str:
    return int(line.split(':')[0].split(' ')[-1])
