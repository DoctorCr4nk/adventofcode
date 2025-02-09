#!/bin/bash

year=2024

for day in {3..25}
do
    aoc_url="https://adventofcode.com/${year}/day/${day}"
    echo \
"#!/usr/bin/python3.12
## Description  Advent of Code ${year}
## Link:        ${aoc_url}" \
> "${year}/day${day}.py"
    touch "${year}/input_data/day${day}.example"
    touch "${year}/input_data/day${day}.data"
done
