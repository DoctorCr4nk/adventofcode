#!/usr/bin/python3.6
## Description  Advent of Code 2023
## Link:        https://adventofcode.com/2023

import utils


def check_adjacent(input_data: list, end_x: int, start_y: int, length: int) -> bool:
    start_x = end_x - length
    number = input_data[start_y][start_x:end_x]
    searchradius_x = 1
    searchradius_y = 1
    for y in range(start_y - searchradius_y , start_y + searchradius_y +1):
        if y < 0 or y > size['y']: continue
        for x in range(start_x - searchradius_x, end_x + searchradius_x):
            if x < 0 or x > size['x']: continue
            char = input_data[y][x]
            if not (char.isdigit() or char == '.'):
                return True
    return False

def get_valid_partnumbers(input_data: list) -> list:
    partnumber = str()
    valid_partnumbers = list()
    y = 0
    for line in input_data:
        x = 0
        for char in line:
            if char.isdigit():
                partnumber += char
            elif not len(partnumber) == 0:
                if check_adjacent(input_data, x, y, len(partnumber)):
                    valid_partnumbers.append(partnumber)
                partnumber = ''
            x += 1
        if not len(partnumber) == 0 and check_adjacent(input_data, x-1, y, len(partnumber)):
            valid_partnumbers.append(partnumber)
        partnumber = ''
        y += 1
    return valid_partnumbers

def get_size(input_data: dict):
    global size
    size = {
        'x' : len(input_data[0]),
        'y' : len(input_data) }

input_example = utils.read_file('input_data/day3.example.txt')
input_data = utils.read_file('input_data/day3.txt')
get_size(input_example)
result1_e = utils.calc_sum(get_valid_partnumbers(input_example))
result2_e = 0
get_size(input_data)
result1 = utils.calc_sum(get_valid_partnumbers(input_data))
result2 = 0
utils.print_results(str(result1_e),
                    str(result1),
                    str(result2_e),
                    str(result2))
