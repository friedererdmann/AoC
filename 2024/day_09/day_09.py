from itertools import chain


def part_2():
    with open("2024/day_09/day_09.txt", "r") as fp:
            lines = fp.readlines()

    line = lines[0]
    unpack = []
    idx = 0
    for i in range(0,len(line),2):
        idx = int(i / 2)
        size = int(line[i])
        size_empty = 0
        if i + 1 < len(line):
            size_empty = int(line[i + 1])
        unpack += [size * [str(idx)]] + [size_empty * ["."]]


    i = len(unpack)
    while True:
        i -= 1
        if i < 0:
            break
        file = unpack[i]
        if not len(file):
            continue
        if '.' in file:
            continue
        for idx in range(i):
            if not '.' in unpack[idx]:
                continue
            length = len(unpack[idx]) - len(file)
            if length < 0:
                continue
            unpack.pop(i)
            unpack.insert(i, len(file) * ['.'])
            unpack.pop(idx)
            unpack.insert(idx, file)

            if length:
                unpack.insert(idx + 1, length * ".")
            #print(''.join(unpack))
            break

    checksum = 0
    for i, v in enumerate(chain.from_iterable(unpack)):
        if v == '.':
            continue
        checksum += i * int(v)

    print(checksum)

def part_1():
    with open("2024/day_09/day_09.txt", "r") as fp:
        lines = fp.readlines()
    line = lines[0]

    unpack = []
    idx = 0
    for i in range(0,len(line),2):
        idx = int(i / 2)
        size = int(line[i])
        size_empty = 0
        if i + 1 < len(line):
            size_empty = int(line[i + 1])
        unpack += size * [str(idx)] + size_empty * ["."]

    i = 0
    while True:
        bit = unpack[i]
        if bit == ".":
            unpack.pop(i)
            unpack.insert(i, unpack[len(unpack) - 1])
            unpack.pop(len(unpack) - 1)
        else:
            i += 1
        if i >= len(unpack):
            break

    checksum = 0
    for i, v in enumerate(unpack):
        checksum += i * int(v)

    print(checksum)


part_1()
part_2()
