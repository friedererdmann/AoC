with open("2024/day_01/day_01.txt", "r") as fp:
    lines = fp.readlines()

a = []
b = []


for line in lines:
    x, y = line.split(" ", 1)
    a.append(int(x))
    b.append(int(y))


# part 1
a.sort()
b.sort()
print(sum([abs(m - n) for m,n in zip(a, b)]))


# part 2
count_a = {}
for z in list(set(a)):
    count_a[z] = a.count(z)

count_b = {}
for z in list(set(b)):
    count_b[z] = b.count(z)

part_2 = 0
for key, value in count_a.items():
    part_2 += key * count_b.get(key, 0) * value

print(part_2)
