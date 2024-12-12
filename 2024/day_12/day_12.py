with open("2024/day_12/day_12.txt", "r") as fp:
    lines = fp.readlines()

field: dict[dict] = {}
for y, line in enumerate(lines):
    for x, column in enumerate(line):
        if column == "\n":
            continue
        field[(x,y)] = column


visited = {}
up = (0,-1)
down = (0,1)
right = (1,0)
left = (-1,0)

directions = [up, right, down, left]

perimeter_directions = directions + [(-1,-1),(1,-1),(-1,1),(1,1)]

regions = 0
part_2 = 0

for coordinate, letter in field.items():
    if coordinate in visited:
        continue
    area = {}
    perimeter = {}
    to_visit = {coordinate: True}
    while to_visit:
        visited[coordinate] = True
        area[coordinate] = True
        for direction in directions:
            neighbor_coord = (coordinate[0] + direction[0], coordinate[1] + direction[1])
            neighbor = field.get(neighbor_coord)
            if not neighbor or neighbor != letter:
                perimeter[neighbor_coord] = perimeter.get(neighbor_coord, 0) + 1
                continue
            if neighbor_coord not in visited:
                to_visit[neighbor_coord] = True
        to_visit.pop(coordinate)
        for key in to_visit:
            coordinate = key
            break
            
    regions += len(area) * sum(perimeter.values())
    vertices = 0
    # find vertices for part_2, any open edges and any pixels in perimeter with value 2 or higher
    part_2 += len(area) * vertices

print(regions)
print(part_2)