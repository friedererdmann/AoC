with open("day_2.txt", "r") as fh:
    lines = fh.readlines()

import re

maximum = {"red": 12, "blue": 14, "green": 13 }

game_sum = 0
for line in lines:
    #matches = re.findall(r"Game ([0-9]*): (?:([0-9]*) (blue|red|green)[,;]?[\s]?)*", line)
    #print(matches)
    game = int(line.split(":")[0][len("Game "):])
    
    rounds = line.split(":")[1].split(";")
    valid = True
    for round in rounds:
        matches = re.findall("([0-9]+) ([a-z]+)", round)
        for match in matches:
            if int(match[0]) > maximum[match[1]]:
                valid = False
    if valid:
        game_sum += game

print(game_sum)

win = 0
for line in lines:
    #matches = re.findall(r"Game ([0-9]*): (?:([0-9]*) (blue|red|green)[,;]?[\s]?)*", line)
    #print(matches)
    game = int(line.split(":")[0][len("Game "):])
    score = {"red": 0, "blue": 0, "green": 0}
    rounds = line.split(":")[1].split(";")
    for round in rounds:
        matches = re.findall("([0-9]+) ([a-z]+)", round)
        for match in matches:
            if int(match[0]) > score[match[1]]:
                score[match[1]] = int(match[0])
    points = score["blue"] * score["green"] * score["red"]
    win += points

print(win)
