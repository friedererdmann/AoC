with open("2023/day_05.txt", "r") as fh:
    lines = fh.readlines()

seeds = [int(x) for x  in lines[0].split(" ")[1: ]]

mappings = {
    "seed-to-soil": {},
    "soil-to-fertilizer": {},
    "fertilizer-to-water": {},
    "water-to-light": {},
    "light-to-temperature": {},
    "temperature-to-humidity": {},
    "humidity-to-location": {}
}

current_key = ""

for line in lines[1:]:
    if not line[:-1]:
        continue

    if line.startswith(tuple(mappings.keys())):
        current_key = line.split(" ")[0]
        continue
    dest, source, irange = [int(x) for x in line.split(" ", 2)]
    mappings[current_key][(source, source + irange)] = dest


def run_through_mappings(a):
    for name in mappings:
        mapping = mappings[name]
        for imin, imax in mapping.keys():
            if not imax >= a >= imin:
                continue
            source = mapping[(imin, imax)]
            a += source - imin
            break
    return a


destinations = []
for seed in seeds:
    destinations.append(run_through_mappings(seed))
print(min(destinations))


# destinations = []
# for i in range(0, len(seeds), 2):
#     for j in range(seeds[i], seeds[i] + seeds[i+1]):
#         destinations.append(run_through_mappings(j))
# print(min(destinations))

for i in range(100): # locations
    a = i
    for name in reversed(mappings):
        mapping = mappings[name]
        for (imin, imax), value in mapping.items():
            if not value <= a <= value + imax - imin:
                continue
            a += a-value
            break
    if a in seeds:
        break

print(i)

