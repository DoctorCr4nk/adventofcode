#!/usr/bin/python3.6
## Description  Advent of Code
## Link:        https://adventofcode.com/2023/

import utils

def calculate_wins(card_game: dict) -> int:
    wins = int()
    for pulled_number in card_game['pulled']:
        if pulled_number in card_game['winning']:
            wins += 1
    return wins

def calculate_cards(card_data: dict) -> int:
    sum_won_cards = 0
    won_cards = list()
    for card in card_data.keys():
        sum_won_cards += 1
        won_cards = calculate_wins(card_data[card])
        for win in range(1, won_cards + 1):
            card_data[card + win]['count'] += card_data[card]['count']
            sum_won_cards += card_data[card]['count']
    return sum_won_cards

def calculate_points(card_data: dict) -> int:
    points = 0
    for card in card_data.keys():
        exponent = -1
        for pulled_number in card_data[card]['pulled']:
            if pulled_number in card_data[card]['winning']:
                exponent += 1
        points += int(pow(2, exponent))
    return points

def format_numbers(card_data_raw: list) -> dict:
    formatted_numbers = dict()
    for line in card_data_raw:
        card_id = utils.get_id(line)
        formatted_numbers[card_id] = {
            'winning' : list(),
            'pulled'  : list(),
            'count'   : 1 }
        for number in line.split(':')[1].split('|')[0].split():
            formatted_numbers[card_id]['winning'].append(number)
        for number in line.split(':')[1].split('|')[1].split():
            formatted_numbers[card_id]['pulled'].append(number)
    return formatted_numbers

card_data_raw = utils.read_file('day4.txt')
card_data = format_numbers(card_data_raw)
part1_result = str(calculate_points(card_data))
part2_result = str(calculate_cards(card_data))
print('Part 1: ' + part1_result)
print('Part 2: ' + part2_result)
