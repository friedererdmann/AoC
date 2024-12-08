from itertools import permutations

with open("2024/day_08/day_08.txt", "r") as fp:
    lines = fp.readlines()

antennas: dict[dict] = {}
frequencies = set()
map_bounds_y = len(lines)
map_bounds_x = len(lines[0]) - 1
for y, line in enumerate(lines):
    for x, column in enumerate(line):
        if column == "\n":
            continue
        if column == ".":
            continue
        antennas[column] = antennas.get(column, set())
        antennas[column].add((x,y))
        frequencies.add(column)


part_2 = True
antinodes = set()
for frequency in frequencies:
    locations = antennas[frequency]
    if part_2:
        for location in locations:
            antinodes.add(location)
    for perm in permutations(locations, 2):
        a1_x, a1_y = perm[0]
        a2_x, a2_y = perm[1]
        i = 0
        while True:
            i += 1
            anti_x = a1_x + i * (a1_x - a2_x)
            anti_y = a1_y + i * (a1_y - a2_y)
            if 0 <= anti_x < map_bounds_x and 0 <= anti_y < map_bounds_y:
                antinodes.add((anti_x, anti_y))
                if part_2:
                    break
            else:
                break


print(len(antinodes))
