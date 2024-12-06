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


# def ray_cast(_pos, _dir, max=11):
#     c = 0
#     while True:
#         next_step = (_pos[0] + directions[_dir][0], _pos[1] + directions[_dir][1])
#         next_field = field.get(next_step)
#         if not next_field:
#             return False
#         if not obstructions.get(next_field):
#             continue
#         if (_dir + 1) % len(directions) in obstructions:
#             return True
#         _pos = next_step
#         c += 1
#         if c > max:
#             return False

        
            

# possible_obs = {}

# position = starting_pos
# while True:
#     next_step = (position[0] + directions[direction][0], position[1] + directions[direction][1])
#     next_field = field.get(next_step)


#     _dire = visited_fields.get(position)
#     if not next_field:
#         break
#     if next_field != "#":
#         position = next_step
#         continue
#     obstructions[next_step] = set(list(obstructions.get(next_step, [])) + [direction])
#     direction += 1
#     direction = direction % len(directions)