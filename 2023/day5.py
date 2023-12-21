#!/usr/bin/python3.6
## Description  Advent of Code
## Link:        https://adventofcode.com/2023

import utils

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

global input_data
results = list()
for data_file in ['day5.example.txt']:
    input_data = utils.read_file('input_data/' + data_file)
    location = int()
    seed_id = int()
    seeds =  get_seed_ids()
    for seed in seeds:
        source_value = seed
        for translation_type in ['soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity', 'location']:
            translation_map = generate_translation(translation_type)
            try:
                dest_value = translation_map[source_value]
            except KeyError:
                dest_value = source_value
            if translation_type == 'location' and (location == 0 or location > dest_value):
                location = dest_value
            source_value = dest_value
        seed_id += 1
    results.append(location)
utils.print_results(results)
