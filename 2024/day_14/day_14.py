from dataclasses import dataclass
from collections import defaultdict

with open("2024/day_14/day_14.txt", "r") as fp:
    lines = fp.readlines()


@dataclass
class Vector2:
    x: int = 0
    y: int = 0


@dataclass
class Robot:
    point: Vector2
    velocity: Vector2


robots = []
for line in lines:
    p_x, p_y, v_x, v_y = [int(a) for b in [z[1].split(',') for z in [y.split('=') for y in [x for x in line.split()]]] for a in b]
    point = Vector2(p_x, p_y)
    velocity = Vector2(v_x, v_y)
    robots.append(Robot(point, velocity))


field_x = 101
field_y = 103
seconds = 100
# seconds = 6515
field = defaultdict(int, {})

middle_x = field_x // 2
middle_y = field_y // 2

def part_1():
    for robot in robots:
        robot.point.x = (robot.point.x + (robot.velocity.x * seconds)) % (field_x)
        robot.point.y = (robot.point.y + (robot.velocity.y * seconds)) % (field_y)
        if robot.point.x == middle_x or robot.point.y == middle_y:
            continue
        field[(robot.point.x > middle_x, robot.point.y > middle_y)] += 1

    score = 1
    for value in field.values():
        score *= value

    print(score)

part_1()

# part 2 - iterate over the images
while input() == '':
    picture = [" "] * field_x + ["\n"]
    picture = picture * field_y
    for robot in robots:
        robot.point.x = (robot.point.x + robot.velocity.x) % (field_x)
        robot.point.y = (robot.point.y + robot.velocity.y) % (field_y) 
        picture[robot.point.y * (field_x + 1) + robot.point.x] = "x"
    print('seconds', seconds + 1)
    print(''.join(picture))
    seconds += 1