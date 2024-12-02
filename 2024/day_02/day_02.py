def is_it_good(series):
    good = False
    diff = [series[i + 1] - series[i] for i in range(len(series) - 1)]
    zeroes = any([x == 0 for x in diff])
    larger_three = any([abs(x) > 3 for x in diff])
    direction = [((abs(x)/x) + 1) / 2 for x in diff if x != 0]
    good = not zeroes and not larger_three and (all(direction) or not any(direction))
    return good


def run_part(part=0):
    with open("2024/day_02/day_02.txt", "r") as fp:
        lines = fp.readlines()
    count = 0
    for line in lines:
        series = [int(x) for x in line.split()]
        count += int(any([is_it_good(series[0:i] + series[i+part:len(series)]) for i in range(len(series))]))
    return count


print(run_part(0))
print(run_part(1))
