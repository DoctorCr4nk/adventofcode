#!/usr/bin/python3.6
## Description  Advent of Code 2023
## Link:        https://adventofcode.com/2023

import utils

def check_adjacent_symbols(input_data: list, start_x: int, end_x: int, start_y: int) -> bool:
    searchradius_x = 1
    searchradius_y = 1
    for y in range(start_y - searchradius_y , start_y + searchradius_y +1):
        if y < 0 or y > size['y']: continue
        for x in range(start_x - searchradius_x, end_x + searchradius_x +1):
            if x < 0 or x > size['x']: continue
            try: char = input_data[y][x]
            except IndexError: char = '.' # I do not understand
            if not (char.isdigit() or char == '.'):
                return True
    return False

def get_adjacent_numbers(input_data: list, gear_x: int, gear_y: int) -> int:
    adjacent_numbers = []
    searchradius_x = 1
    searchradius_y = 1
    y = gear_y - searchradius_y
    while y <= (gear_y + searchradius_y):
        if y < 0 or y > size['y']: continue
        x = gear_x - searchradius_x
        while x <= (gear_x + searchradius_x):
            if x < 0 or x > size['x']: continue
            char = input_data[y][x]
            if char.isdigit():
                number = get_full_number(input_data, x, y)
                adjacent_numbers.append(int(number['value']))
                x = number['x'][-1]
            x += 1
        y += 1
    if len(adjacent_numbers) == 2:
        return adjacent_numbers[0] * adjacent_numbers[1]
    else:
        return 0

def get_full_number(input_data: list, digit_x: int, digit_y: int) -> dict:
    number_data = {
        'value' : str(),
        'x'     : list(),
        'y'     : digit_y }
    if not input_data[digit_y][digit_x].isdigit():
        print('Given coordinates is not a digit')
        exit(1)
    for x in range(0, len(input_data[digit_y])):
        char = input_data[digit_y][x]
        if char.isdigit():
            number_data['x'].append(x)
            number_data['value'] += char
        else:
            if digit_x in number_data['x']: break
            else:
                number_data['x'] = list()
                number_data['value'] = str()
    return number_data

def get_gear_ratios(input_data: list) -> list:
    gear_ratios = list()
    y = 0
    while y < len(input_data):
        x = 0
        while x < len(input_data[y]):
            char = input_data[y][x]
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

def get_partnumbers(input_data: list) -> list:
    partnumber = str()
    valid_partnumbers = list()
    y = 0
    while y < size['y']:
        x = 0
        while x < size['x']:
            char = input_data[y][x]
            if char.isdigit():
                partnumber = get_full_number(input_data, x, y)
                x = partnumber['x'][-1]
                if check_adjacent_symbols(input_data, partnumber['x'][0], partnumber['x'][-1], y):
                    valid_partnumbers.append(partnumber['value'])
            x += 1
        y += 1
    return valid_partnumbers

results = list()
for data_file in ['day3.example.txt', 'day3.txt']:
    input_data = utils.read_file('input_data/' + data_file)
    get_size(input_data)
    results.append(utils.calc_sum(get_partnumbers(input_data)))
    results.append(utils.calc_sum(get_gear_ratios(input_data)))
utils.print_results(results)
