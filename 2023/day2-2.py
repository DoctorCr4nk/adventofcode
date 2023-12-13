#!/usr/bin/python3.6
# https://adventofcode.com/2023/day/2#part2

def get_game_info(file_info) -> dict:
    game_info = dict()
    for line in file_info.readlines():
        pull_count = 0
        gameid = line.split(':')[0].split(' ')[1]
        pulls = line.split(':')[1].split(';')
        game_info[gameid] = dict()
        for pull in pulls:
            cubes = pull.replace(',','').replace('\n', '').split(' ')[1:]
            game_info[gameid][pull_count] = dict()
            for i in range(0, len(cubes)):
                if i % 2 == 0: game_info[gameid][pull_count][cubes[i+1]] = cubes[i]
            pull_count += 1
    return game_info

def get_possible_games(game_info: dict()) -> list:
    possible_games = list()
    requirements = {
        'red'   : 12,
        'green' : 13,
        'blue'  : 14 }
    for gameid in game_info:
        is_possible = True
        for pullid in game_info[gameid]:
            for color in game_info[gameid][pullid]:
                if not int(game_info[gameid][pullid][color]) <= requirements[color]:
                    is_possible = False
        if is_possible: possible_games.append(gameid)
    return possible_games

def get_fewest_cubes(game_info: dict()) -> dict:
    fewest_cubes = dict()
    for gameid in game_info:
        fewest_cubes[gameid] = {
            'red'   : 0,
            'green' : 0,
            'blue'  : 0 }
        for pullid in game_info[gameid]:
            for color in game_info[gameid][pullid]:
                if int(game_info[gameid][pullid][color]) > fewest_cubes[gameid][color]:
                    fewest_cubes[gameid][color] = int(game_info[gameid][pullid][color])
    return fewest_cubes

sum = 0
game_info = get_game_info(file_info = open('day2.txt', 'r'))
possible_games = get_possible_games(game_info)
for gameid in possible_games:
    sum += int(gameid)
print('Sum of possible gameids: ' + str(sum))
power = 0
sum = 0
fewest_cubes = get_fewest_cubes(game_info)
for gameid in fewest_cubes:
    sum += fewest_cubes[gameid]['red'] * fewest_cubes[gameid]['green'] * fewest_cubes[gameid]['blue']
print('Power of sets: ' + str(sum))
