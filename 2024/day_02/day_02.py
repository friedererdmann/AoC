with open("2024/day_02/day_02.txt", "r") as fp:
    lines = fp.readlines()


def is_it_good(series):
    good = False
    dir = 1
    for i, v in enumerate(series):
        if i == 0:
            distance = series[i + 1] - v
            if distance == 0:
                break
            dir = abs(distance)/distance
            continue
        distance = v - series[i - 1]
        if distance == 0:
            break
        if dir != abs(distance)/distance:
            break
        if 3 < abs(distance):
            break
        if i == len(series) - 1:
            good = True
    return i, good


safe = 0
part_2 = False

for line in lines:
    series = [int(x) for x in line.split(" ")]
    idx, success = is_it_good(series)
    if not success and part_2:
        for i in range(len(series)):
            xseries = series.copy()
            xseries.pop(i)
            xidx, xsuccess = is_it_good(xseries)
            if xsuccess:
                series = xseries
                success = True
                break
    if success:
        safe += 1

print(safe)
