import re


def mul(a, b):
    return a * b


with open("2024/day_03/day_03.txt", "r") as fp:
    lines = fp.read()


# part 1
mul_pattern = "mul\\(\\d{1,3},\\d{1,3}\\)"
statements = re.findall(mul_pattern, lines)
i = sum([eval(s) for s in statements])
print(i)


# part 2
do_pattern = "do\\(\\)"
dont_pattern = "don't\\(\\)"
do = True
nr = 0
search = lines
while True:
    index = len(search)
    c_end = 0
    instruction = ""
    breaking = True
    for pattern in [mul_pattern, do_pattern, dont_pattern]:
        net = re.search(pattern, search)
        if not net:
            continue
        text = net.group()
        start, end = net.span()
        if start < index:
            index = start
            c_end = end
            instruction = text
            breaking = False
    if breaking:
        break
    if instruction == "don't()":
        do = False
    if instruction == "do()":
        do = True
    if do and instruction.startswith("mul("):
        nr += eval(instruction)
    search = search[c_end:]

print(nr)
