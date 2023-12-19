#!/usr/bin/python3
## Description  Advent of Code Day 1-2
## Link:        https://adventofcode.com/2023/day/1

def convert_text(path_file_input: str) -> list:
    converted_text = list()
    digit_names = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    file_input = open(path_file_input, 'r')
    raw_text = file_input.readlines()
    file_input.close()
    for line in raw_text:
        end_position = 1
        line = line.replace('\n', '')
        line_last = str()
        while end_position <= len(line):
            digit_count = 1
            short_line = line[:end_position]
            for digit in digit_names:
                if digit in short_line:
                    line = short_line.replace(digit, str(digit_count)) + line[end_position:]
                    end_position = 1
                else:
                    digit_count += 1
            end_position += 1

            if not line == line_last:
                #print(line, end=', ')
                line_last = line
        #print()
        converted_text.append(line)
    return converted_text

def convert_text2(path_file_input: str) -> list:
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
        'nine'  : 'n9e'
    }
    file_input = open(path_file_input, 'r')
    raw_text = file_input.readlines()
    file_input.close()
    for line in raw_text:
        line = line.replace('\n', '')
        for digit in digits.keys():
            if digit in line:
                line = line.replace(digit, digits[digit])
        converted_text.append(line)
    return converted_text

def calc_digit_sum(custom_input) -> int:
    digit_sum = list()
    secret_total = 0
    for line in custom_input:
        tmp_char = str()
        tmp_secret = ''
        for char in line:
            if char.isdigit():
                if len(tmp_secret) == 0:
                    tmp_secret = char
                tmp_char = char
        if not len(tmp_secret) == 0:
            #print(tmp_secret + tmp_char)
            digit_sum.append(int(tmp_secret + tmp_char))
    return digit_sum

def print_text_digit(path_file_input: str, digit_sum: list):
    file_input = open(path_file_input, 'r')
    digit_sum_counter = 0
    total_sum = 0
    for line in file_input:
        line = line.replace('\n', '')
        if digit_sum_counter > len(digit_sum):
            print('No digit sum: ' + ':\t' + line)
        else:
            print(str(digit_sum[digit_sum_counter]) + ':\t' + line)
            total_sum += digit_sum[digit_sum_counter]
        digit_sum_counter += 1
    print('Total sum: ' + str(total_sum))
    file_input.close()

def calculate_sum(digit_sums: list) -> int:
    total_sum = 0
    for digit_sum in digit_sums:
        total_sum += digit_sum
    return total_sum

def compare_results(digit_sums_wrong: list, digit_sums_rigth: list, path_file_input: str):
    file_input = open(path_file_input, 'r')
    line_list = list()
    for line in file_input.readlines():
        line_list.append(line.replace('\n', ''))
    file_input.close()
    for i in range(0, len(digit_sums)):
        if digit_sums_wrong[i] != digit_sums_rigth[i]:
            print('Zeile ' + str(i) + ': ' + str(digit_sums_wrong[i]) + '-' + str(digit_sums_rigth[i]) + ' ' + line_list[i])
    #print(line_list)

#file_name = 'day1-test.txt'
file_name = 'day1.txt'
clean_text = convert_text(file_name)
clean_text2 = convert_text2(file_name)
digit_sums = calc_digit_sum(clean_text)
digit_sums2 = calc_digit_sum(clean_text2)
print(calculate_sum(digit_sums))
print(calculate_sum(digit_sums2))
compare_results(digit_sums, digit_sums2, file_name)

#print_text_digit(file_name, digit_sums)
#clean_text = convert_text('day1.txt')
#print(calc_digit_sum(clean_text))
