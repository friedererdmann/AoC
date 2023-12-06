with open("2023/day_06.txt", "r") as fh:
    lines = fh.readlines()

time = lines[0]
distance = lines[1]

times = [int(x) for x in time.split(" ")[1:] if x]
distances = [int(x) for x in distance.split(" ")[1:] if x]

mapping = {x:y for x,y in list(zip(times, distances))}
print(mapping)


points = 1
for time, record in zip(times, distances):
    beats = 0
    for i in range(time):
        distance = (time - i) * i
        if distance > record:
            beats += 1
    points *= beats

print(points)


(time - i) * i = record
record / (time - i) = i

# part 2
# solve pt1 and pt2 for and take the difference
# time = int(lines[0].split(" ", 1)[1].replace(" ", ""))
# distance = int(lines[1].split(" ", 1)[1].replace(" ", ""))
# distance = - pow(x, 2) + time * x

