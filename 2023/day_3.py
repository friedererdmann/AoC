from collections import defaultdict

system = defaultdict(lambda: ".")

with open("day_3.txt", "r") as fh:
    lines = fh.readlines()

max_y = len(lines)
max_x = len(lines[0])

for i, line in enumerate(lines):
    for j, char in enumerate(line[:-1]):
        system[(j, i)] = char

is_number = False
is_part = False
number = ""
list_digits = []
digits = {}
parts = []
for y in range(max_y):
    for x in range(max_x):
        char = system[(x,y)]
        if char.isdigit():
            is_number = True
            list_digits.append((x,y))
            number += char
            for a in [(x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)]:
                if not system[a].isdigit() and not system[a] == ".":
                    is_part = True
        else:
            is_number = False
            if is_part:
                parts.append(int(number))
                for digit in list_digits:
                    digits[digit] = [len(parts)-1,int(number)]
                is_part = False
            number = ""
            list_digits = []

print(sum(parts))

lookup = {}
for x,y in digits.values():
    lookup[x] = y

gears = []
for y in range(max_y):
    for x in range(max_x):
        char = system[(x,y)]
        if char != "*":
            continue
        gear_pieces = []
        for a in [(x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)]:
            if a in digits:
                gear_pieces.append(digits[a][0])
        if len(set(gear_pieces)) == 2:
            a = list(set(gear_pieces))
            gears.append(lookup[a[0]] * lookup[a[1]])

print(sum(gears))