#!/usr/bin/python3.6
## Description  Advent of Code
## Link:        https://adventofcode.com/2023

import utils

seed_info = {
    'seedid'        : int(),
    'fertilizer'    : int(),
    'water'         : int(),
    'light'         : int(),
    'temperature'   : int(),
    'humidity'      : int(),
    'location'      : int(), }

def get_seed_ids() -> list:
    seed_ids = list()
    for seed_id in input_data[0].split()[1:]:
        seed_ids.append(int(seed_id))
    return seed_ids

def generate_translation(map: str) -> list:
    read_data = False
    translation = dict()
    for row in input_data:
        if row.endswith(map + ' map:'):
            read_data = True
        elif row == '':
            read_data = False
        elif read_data:
            dest_start = int(row.split()[0])
            source_start = int(row.split()[1])
            range_length = int(row.split()[2])
            for i in range(range_length):
                translation[source_start+i] = dest_start+i
    return translation

def translate_seed2soil(seed_id: int) -> int:
    soild_id = int()
    return soild_id

global input_data
results = list()
for data_file in ['day5.example.txt', 'day5.txt']:
    input_data = utils.read_file('input_data/' + data_file)
    translation_maps = dict()
    location = int()
    for translation_type in ['soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity', 'location']:
        translation_maps[translation_type] = generate_translation(translation_type)
    for seed_id in get_seed_ids():
        source_value = seed_id
        for translation_type in translation_maps:
            try:
                dest_value = translation_maps[translation_type][source_value]
            except KeyError:
                dest_value = source_value
            if translation_type == 'location' and (location == 0 or location > dest_value):
                location = dest_value
            source_value = dest_value
    results.append(location)
utils.print_results(results)
