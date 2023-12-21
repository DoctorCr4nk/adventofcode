#!/usr/bin/python3.6
## Description  Advent of Code
## Link:        https://adventofcode.com/2023

import utils

def get_seed_ids() -> list:
    seed_ids = list()
    for seed_id in input_data[0].split()[1:]:
        seed_ids.append(int(seed_id))
    return seed_ids

def generate_translation_map(map_type: str) -> list:
    read_data = False
    translation_map = list()
    for row in input_data:
        if row.endswith(map_type + ' map:'): read_data = True
        elif row == '': read_data = False
        elif read_data:
            dest_start = int(row.split()[0])
            source_start = int(row.split()[1])
            range_length = int(row.split()[2])
            source_end = (source_start + range_length)
            diff = (source_start - dest_start)
            translation_map.append([source_start, source_end, diff])
    return translation_map

def translate(map_type: str, value: int) -> int:
    translated_value = value
    translation_map = generate_translation_map(map_type)
    for translation in translation_map:
        if value in range(translation[0], translation[1]):
            translated_value = value - translation[2]
    return translated_value

global input_data
results = list()
for data_file in ['day5.example.txt', 'day5.txt']:
    input_data = utils.read_file('input_data/' + data_file)
    location = int()
    seed_id = int()
    seeds =  get_seed_ids()
    for seed in seeds:
        print(str(seed_id+1) + '/' + str(len(seeds)), end=': ')
        source_value = seed
        for translation_type in ['soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity', 'location']:
            print(end='.')
            dest_value = translate(translation_type, source_value)
            if translation_type == 'location' and (location == 0 or location > dest_value):
                location = dest_value
            source_value = dest_value
        seed_id += 1
        print()
    results.append(location)
utils.print_results(results)
