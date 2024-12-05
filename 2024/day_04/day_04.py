with open("2024/day_04/day_04.txt", "r") as fp:
    lines = fp.readlines()

field = {}
for y, line in enumerate(lines):
    for x, column in enumerate(line):
        field[(x,y)] = column

searches = [
    [( 0, 0), ( 1, 0), ( 2, 0), ( 3, 0)], # DOWN
    [( 0, 0), (-1, 0), (-2, 0), (-3, 0)], # UP
    [( 0, 0), ( 0, 1), ( 0, 2), ( 0, 3)], # RIGHT
    [( 0, 0), ( 0,-1), ( 0,-2), ( 0,-3)], # LEFT
    [( 0, 0), ( 1, 1), ( 2, 2), ( 3, 3)], # DIAGONAL DOWN RIGHT
    [( 0, 0), (-1,-1), (-2,-2), (-3,-3)], # DIAGONAL UP LEFT
    [( 0, 0), (-1, 1), (-2, 2), (-3, 3)], # DIAGONAL UP RIGHT
    [( 0, 0), ( 1,-1), ( 2,-2), ( 3,-3)], # DIAGONAL DOWN LEFT
]


count = 0
for coordinate in field:
    for search in searches:
        local_co = [(x+coordinate[0], y+coordinate[1]) for x, y in search]
        text = "".join([field.get(x, "") for x in local_co])
        if text == "XMAS":
            count += 1

print(count)


count = 0
part_2 = ("SSAMM", "MSASM", "SMAMS", "MMASS")
part_2_search = [(-1,-1), (-1, 1), ( 0, 0), (1, 1), (1, -1)]
for coordinate in field:
    local_co = [(x+coordinate[0], y+coordinate[1]) for x, y in part_2_search]
    text = "".join([field.get(x, "") for x in local_co])
    if text in part_2:
        count += 1
print(count)