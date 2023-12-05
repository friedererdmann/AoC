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


# for sample data
# destinations = []
# for i in range(0, len(seeds), 2):
#     for j in range(seeds[i], seeds[i] + seeds[i+1]):
#         destinations.append(run_through_mappings(j))
# print(min(destinations))

part_2 = {seeds[x]: seeds[x+1] for x in range(0, len(seeds), 2)}

# reverse brute force approach, ran with multiple numbers.
stop = False
i = 72246198 # guessing reasonable starting number
while True: # locations
    a = i
    for name in reversed(mappings):
        mapping = mappings[name]
        for (imin, imax), value in mapping.items():
            if value <= a <= value + imax - imin:
                a = imin + a-value
                break
    for start, irange in part_2.items():
        if start <= a <= start+irange:
            stop = True
            break
    if stop: break
    print(i)
    i += 1

print(i)

