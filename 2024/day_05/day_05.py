with open("2024/day_05/day_05.txt", "r") as fp:
    lines = fp.read()

page_rules_lines, update_lines = lines.split("\n\n")

page_rules = [tuple(map(int, pages.split("|"))) for pages in [line for line in page_rules_lines.splitlines()]]
page_rules_dict = {}
for rule in page_rules:
    page, required = rule
    page_rules_dict[required] = page_rules_dict.get(required, []) + [page]
updates = [list(map(int, pages.split(","))) for pages in [line for line in update_lines.splitlines()]]
# print(page_rules)
for page, rule in page_rules_dict.items():
    print(page, rule)
# print(updates)

# part 1
part_2 = []
count = 0
for update in updates:
    valid = True
    for idx, page in enumerate(update):
        requirements = page_rules_dict.get(page, [])
        if set(requirements).intersection(set(update[idx:])):
            valid = False
            part_2.append(update)
            break
    if valid:
        count += update[int(len(update) / 2)]
print(count)

# part 2
count = 0
for update in part_2:
    valid = False
    while True:
        intersection = []
        idx = 0
        for idx, page in enumerate(update):
            requirements = page_rules_dict.get(page, [])
            intersection = list(set(requirements).intersection(set(update[idx:])))
            if intersection:
                break
        for nr in intersection:
            update.pop(update.index(nr))
            update.insert(idx, nr)
        if not intersection:
            break
        
    count += update[int(len(update) / 2)]
print(count)