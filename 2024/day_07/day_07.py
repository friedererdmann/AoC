with open("2024/day_07/day_07.txt", "r") as fp:
    lines = fp.readlines()


def add(i, j):
    return i + j

def mul(i, j):
    return i * j

def conc(i, j):
    return int(str(i) + str(j))



def solve(result: int, parts: list[int], operators: list[callable]) -> bool:
    results = [0]
    for part in parts:
        new_line = []
        for nr in results:
            new_line += [x(nr, part) for x in operators]
        results = new_line
    return result in results


part_1 = 0
part_2 = 0
for line in lines:
    result = int(line.split(":")[0])
    parts = [int(x) for x in line.split(":")[1].split()]
    if solve(result, parts, [add, mul]):
        part_1 += result
    if solve(result, parts, [add, mul, conc]):
        part_2 += result

print(part_1)
print(part_2)