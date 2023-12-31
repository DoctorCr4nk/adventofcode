#!/usr/bin/python3.6
## Description  Advent of Code
## Link:        https://adventofcode.com/2023

import multiprocessing
import utils

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

def get_location(seed_id: int) -> int:
    source_value = seed_id
    for translation_type in ['soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity', 'location']:
        dest_value = translate(translation_type, source_value)
        source_value = dest_value
    return dest_value

def get_lowest_location(seed_ids: list) -> int:
    locations = list()
    process_pool = multiprocessing.Pool()
    locations = process_pool.map(get_location, seed_ids)
    process_pool.close()
    return min(locations)

def get_lowest_location2(seed_id_ranges: list) -> int:
    lowest_locations = list()
    for seed_ids in seed_id_ranges:
        lowest_locations.append(get_lowest_location(seed_ids))
    return min(lowest_locations)

def get_seed_ids() -> list:
    seed_ids = list()
    for seed_id in input_data[0].split()[1:]:
        seed_ids.append(int(seed_id))
    return seed_ids

def get_seed_id_ranges() -> list:
    seed_counter = int()
    seed_id_ranges = list()
    seed_row = input_data[0].split()[1:]
    seed_count = len(seed_row)
    while seed_counter < seed_count:
        start_seed = int(seed_row[seed_counter])
        end_seed =   int(seed_row[seed_counter]) + int(seed_row[seed_counter+1]) - 1
        seed_id_ranges.append(range(start_seed, end_seed))
        seed_counter += 2
    return seed_id_ranges

def translate(map_type: str, value: int) -> int:
    translated_value = value
    translation_map = generate_translation_map(map_type)
    for translation in translation_map:
        if value in range(translation[0], translation[1]):
            translated_value = value - translation[2]
    return translated_value

if __name__== '__main__':
    global input_data
    results = list()
    for data_file in ['day5.example.txt', 'day5.txt']:
        input_data = utils.read_file('input_data/' + data_file)
        results.append(get_lowest_location(get_seed_ids()))
        results.append(get_lowest_location2(get_seed_id_ranges()))
    utils.print_results(results)
