#!/usr/bin/python3.6
## Description  Advent of Code 2023
## Link:        https://adventofcode.com/2023

import utils

def convert_text(input_data: list) -> list:
    converted_text = list()
    digits = {
        'one'   : 'o1e',
        'two'   : 't2o',
        'three' : 't3e',
        'four'  : 'f4r',
        'five'  : 'f5e',
        'six'   : 's6x',
        'seven' : 's7n',
        'eight' : 'e8t',
        'nine'  : 'n9e' }
    for line in input_data:
        line = line.replace('\n', '')
        for digit in digits.keys():
            if digit in line:
                line = line.replace(digit, digits[digit])
        converted_text.append(line)
    return converted_text

def get_numbers(input_data: list) -> list:
    numbers = list()
    for line in input_data:
        first_number = str()
        last_number = str()
        for char in line:
            if char.isdigit():
                first_number = char
                break
        for char in reversed(line):
            if char.isdigit():
                last_number = char
                break
        try:
            numbers.append(int(first_number + last_number))
        except ValueError:
            pass
    return numbers

results = list()
for data_file in ['day1.example1.txt','day1.example2.txt', 'day1.txt']:
    input_data = utils.read_file('input_data/' + data_file)
    results.append(utils.calc_sum(get_numbers(input_data)))
    results.append(utils.calc_sum(get_numbers(convert_text(input_data))))
utils.print_results(results)
