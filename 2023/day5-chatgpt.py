#!/usr/bin/python3.6
## Description  Advent of Code
## Link:        https://adventofcode.com/2023
## Day5 after running my code through ChatGPT
## Doesnt get part1 right...

import utils

def get_seed_ids1(data: list) -> list:
    return [int(seed_id) for seed_id in data.split()[1:]]

def get_seed_ids2(data: list) -> list:
    seed_ids = list()
    seed_row = data.split()[1:]
    for start, length in zip(map(int, seed_row[::2]), map(int, seed_row[1::2])):
        seed_ids.extend(range(start, start + length))
    return seed_ids

def generate_translation_map(map_type: str, data: list) -> list:
    read_data = False
    translation_map = list()
    for row in data:
        if row.endswith(map_type + ' map:'): read_data = True
        elif row == '': read_data = False
        elif read_data:
            dest_start, source_start, range_length = map(int, row.split()[:3])
            source_end = source_start + range_length
            diff = source_start - dest_start
            translation_map.append([source_start, source_end, diff])
    return translation_map

def translate(map_type: str, value: int, translation_map: list) -> int:
    translated_value = value
    for translation in translation_map:
        if value in range(translation[0], translation[1]):
            translated_value = value - translation[2]
    return translated_value

def get_lowest_location(seed_ids: list, translation_map: list) -> int:
    location = float('inf')
    for seed_id in seed_ids:
        source_value = seed_id
        for translation_type in ['soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity', 'location']:
            dest_value = translate(translation_type, source_value, translation_map)
            if translation_type == 'location' and dest_value < location:
                location = dest_value
            source_value = dest_value
    return location

results = list()
for data_file in ['day5.example.txt', 'day5.txt']:
    input_data = utils.read_file('input_data/' + data_file)
    seed_ids1 = get_seed_ids1(input_data[0])
    seed_ids2 = get_seed_ids1(input_data[0])
    translation_map = generate_translation_map('location', input_data)
    results.extend([get_lowest_location(seed_ids1, translation_map), get_lowest_location(seed_ids2, translation_map)])

utils.print_results(results)
