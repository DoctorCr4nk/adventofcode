#!/usr/bin/python3.6
## Description  Advent of Code 2023
## Link:        https://adventofcode.com/2023

import utils

def check_adjacent(input_data: list, end_x: int, start_y: int, length: int) -> bool:
    start_x = end_x - length
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

def get_adjacent_numbers(input_data: list, gear_x: int, gear_y: int) -> int:
    adjacent_numbers = []
    searchradius_x = 1
    searchradius_y = 1
    for y in range(gear_y - searchradius_y , gear_y + searchradius_y +1):
        if y < 0 or y > size['y']: continue
        for x in range(gear_x - searchradius_x, gear_x + searchradius_x +1):
            if x < 0 or x > size['x']: continue
            char = input_data[y][x]
            if char.isdigit():
                print('Go left: ', end='')
                for current_x in range(x, 0, -1):
                    char = input_data[y][current_x]
                    if char.isdigit():
                        print(char, end='')
                        left_x = current_x
                    else: break
                print('\nGo right: ', end='')
                for current_x in range(x, size['x']):
                    char = input_data[y][current_x]
                    if char.isdigit():
                        print(char, end='')
                        right_x = current_x
                    else: break
                print('\nNumber: ' + str(input_data[y][left_x:right_x]))
                adjacent_numbers.append(int(input_data[y][left_x:right_x]))

    if len(adjacent_numbers) == 2:
        print(adjacent_numbers)
        return adjacent_numbers[0] * adjacent_numbers[1]
    else:
        print('------')
        return 0

def get_gear_ratios(input_data: list) -> list:
    gear_ratios = list()
    y = 0
    for line in input_data:
        x = 0
        for char in line:
            if char == '*':
                gear_ratios.append(get_adjacent_numbers(input_data, x, y))
            x += 1
        y += 1
    return gear_ratios

def get_size(input_data: list):
    global size
    size = {
        'x' : len(input_data[0]),
        'y' : len(input_data) }

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

input_example = utils.read_file('input_data/day3.example.txt')
input_data = utils.read_file('input_data/day3.txt')
get_size(input_example)
result1_e = utils.calc_sum(get_valid_partnumbers(input_example))
result2_e = utils.calc_sum(get_gear_ratios(input_example))
get_size(input_data)
result1 = utils.calc_sum(get_valid_partnumbers(input_data))
result2 = 0 #utils.calc_sum(get_gear_ratios(input_data))
utils.print_results(str(result1_e),
                    str(result1),
                    str(result2_e),
                    str(result2))
