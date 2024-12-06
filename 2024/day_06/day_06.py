with open("2024/day_06/day_06.txt", "r") as fp:
    lines = fp.readlines()

field = {}
starting_pos = (0,0)
for y, line in enumerate(lines):
    for x, column in enumerate(line):
        if column == "\n":
            continue
        if column == "^":
            starting_pos = (x,y)
        field[(x,y)] = column


up = (0,-1)
down = (0,1)
right = (1,0)
left = (-1,0)

directions = [up, right, down, left]
direction = 0
position = starting_pos

visited_fields = {}
obstructions = {}




while True:
    visited_fields[position] = set(list(visited_fields.get(position, [])) + [direction])
    next_step = (position[0] + directions[direction][0], position[1] + directions[direction][1])
    next_field = field.get(next_step)
    if not next_field:
        break
    if next_field != "#":
        position = next_step
        continue
    obstructions[next_step] = set(list(obstructions.get(next_step, [])) + [direction])
    direction += 1
    direction = direction % len(directions)


print(len(visited_fields.keys()))

loops = 0
for visited in visited_fields:
    direction = 0
    position = starting_pos
    new_field = field.copy()
    new_field[visited] = "#"
    loop = False
    new_visited_fields = {}
    while True:
        new_visited_fields[position] = set(list(new_visited_fields.get(position, [])) + [direction])
        next_step = (position[0] + directions[direction][0], position[1] + directions[direction][1])
        next_field = new_field.get(next_step)
        if next_step in new_visited_fields:
            if direction in new_visited_fields[next_step]:
                loop = True
                break
        if not next_field:
            break
        if next_field != "#":
            position = next_step
            continue
        obstructions[next_step] = set(list(obstructions.get(next_step, [])) + [direction])
        direction += 1
        direction = direction % len(directions)
    loops += loop

print(loops)