#!/usr/bin/python3
## Description  Advent of Code Day 1-1
## Link:        https://adventofcode.com/2023/day/1

secret_code = list()
secret_total = 0
file_input = open('day1.txt', 'r')

for line in file_input.readlines():
    tmp_char = str()
    tmp_secret = str()
    for char in line:
        if char.isdigit():
            if len(tmp_secret) == 0:
                tmp_secret = char
            tmp_char = char
    tmp_secret += tmp_char
    if not len(tmp_secret) == 0:
        secret_code.append(tmp_secret)
for sum in secret_code:
    secret_total += int(sum)
print(secret_total)
