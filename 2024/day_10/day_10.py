with open("2024/day_10/day_10.txt", "r") as fp:
    lines = fp.readlines()

data = {}
trailheads = {}
mountaintops = {}
for y, line in enumerate(lines):
    for x, column in enumerate(line):
        if column == "\n":
            continue
        data[(x,y)] = int(column)
        if int(column) == 0:
            trailheads[(x,y)] = 0
        if int(column) == 9:
            mountaintops[(x,y)] = 0


directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


score = 0
for trailhead in trailheads.keys():
    visited = {}
    current_position = trailhead
    while True:
        value = data[current_position]
        if value == 9:
            score += 1
        neighbors = []
        for direction in directions:
            coordinate = current_position[0] + direction[0], current_position[1] + direction[1]
            n_height = data.get(coordinate, 100)
            if n_height - value != 1 or coordinate in visited:
                continue
            neighbors.append(coordinate)
        if neighbors:
            visited[current_position] = len(neighbors)
            current_position = neighbors[-1]
            continue
        else:
            visited[current_position] = 0
            branches = [x[0] for x in visited.items() if x[1] > 1]
            if not branches:
                break
            current_position = branches[-1]
            continue
    
print(score)
