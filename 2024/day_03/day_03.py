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
full_pattern = "do\\(\\)|don't\\(\\)|mul\\(\\d{1,3},\\d{1,3}\\)"
statements = re.findall(full_pattern, lines)

i = 0
do = True
for statement in statements:
    if statement.startswith("mul("):
        i += eval(statement) * do
    else:
        do = True if (statement == "do()") else False
print(i)
