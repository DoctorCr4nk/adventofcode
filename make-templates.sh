#!/bin/bash

year=2023

for day in {4..24}
do
    echo '#!/usr/bin/python3.6
## Description  Advent of Code
## Link:        https://adventofcode.com/2023/' > "${year}/day${day}.py"
    touch "${year}/day${day}.example.txt"
    touch "${year}/day${day}.txt"
done
