from dataclasses import dataclass
from collections import defaultdict


with open("2024/day_15/day_15.txt", "r") as fp:
    lines = fp.read()


def present():
    
    representation = ([" "] * size_x + ["\n"]) * size_y

    for coord, value in field.items():
        position = coord[1] * (size_x + 1) + coord[0]
        if position > len(representation):
            continue
        representation[position] = value

    representation[current_pos[1] * (size_x + 1) + current_pos[0]] = "@"
    print("".join(representation))


field_str, movement = lines.split("\n\n")

size_x = len(field_str.splitlines()[0])
size_y = len(field_str.splitlines())

lookup = {"<": (-1, 0), "v": (0, 1), ">": (1, 0), "^": (0, -1)}
inverse = {v: k for k, v in lookup.items()}
moves = [lookup[x] for x in movement if x in lookup]


# # = wall
# O = object
# @ = robot
starting_pos = (0, 0)
field = defaultdict(lambda: " ", {})
for y, line in enumerate(field_str.splitlines()):
    for x, column in enumerate(line):
        if column == "\n":
            continue
        if column == "@":
            starting_pos = (x, y)
            continue
        if column == ".":
            continue
        field[(x,y)] = column


current_pos = starting_pos
for move in moves:
    # present()
    # print(inverse[move] + "\n\n")
    neighbor_coord = current_pos[0] + move[0], current_pos[1] + move[1]
    if field[neighbor_coord] == " ":
        current_pos = neighbor_coord
        continue
    if field[neighbor_coord] == "#":
        continue
    if field[neighbor_coord] == "O":
        # raycast, find out if there's an empty space before we hit a #
        empty = None
        boxes = []
        for y in range(abs(move[1]) * size_y + 1):
            breakage = False
            for x in range(abs(move[0]) * size_x + 1):
                check = neighbor_coord[0] + x * move[0], neighbor_coord[1] + y * move[1]
                if field[check] == "O":
                    boxes.append(check)
                if field[check] == " ":
                    empty = check
                    breakage = True
                    break
                if field[check] == "#":
                    breakage = True
                    break
            if breakage: break
        if not empty:
            continue
        current_pos = neighbor_coord
        for box in boxes:
            field.pop(box)
        for box in boxes:
            field[(box[0] + move[0], box[1] + move[1])] = "O"

# present()

score = 0
for coord, value in field.items():
    if value != "O":
        continue
    score += 100 * coord[1] + coord[0]

print(score)