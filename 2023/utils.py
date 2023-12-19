#!/usr/bin/python3.6

def read_file(path_file: str) -> list:
    input_data = list()
    file_input = open(path_file, 'r')
    for line in file_input.readlines():
        input_data.append(line)
    file_input.close()
    return input_data

def calc_sum(numbers: list) -> int:
    sum = int()
    for number in numbers:
        sum += number
    return sum
