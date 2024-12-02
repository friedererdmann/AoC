with open("2024/day_01/day_01.txt", "r") as fp:
    lines = fp.readlines()

a, b = list(zip(*[x for x in [map(int, line.split()) for line in lines]]))

# part 1
print(sum([abs(m - n) for m,n in zip(sorted(a), sorted(b))]))

# part 2
print(sum([d * a.count(d) * b.count(d) for d in set(a)]))
