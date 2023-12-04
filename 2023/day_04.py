with open("day_04.txt", "r") as fh:
    lines = fh.readlines()

result = 0
for line in lines:
    card, numbers = line.split(":")
    winners, yours = numbers.split("|")
    winning = [int(x) for x in winners.split(" ") if x]
    yours = [int(x) for x in yours.split(" ") if x]
    # print(winning, yours)
    length = (len(winning) + len(yours))
    points = (len(list(set(winning + yours))))
    x = length - points - 1
    if x >= 0:
        result += pow(2, x)

print(result)


cards = {}
for line in lines:
    card, numbers = line.split(":")
    card_id = int(card.split(" ", 1)[1])
    winners, yours = numbers.split("|")
    winning = [int(x) for x in winners.split(" ") if x]
    yours = [int(x) for x in yours.split(" ") if x]
    
    length = (len(winning) + len(yours))
    points = (len(list(set(winning + yours))))
    x = length - points
    cards[card_id] = x

print(cards)

from collections import defaultdict
number_of_cards = defaultdict(int)

for index in cards:
    number_of_cards[index] += 1
    for idx in range(cards[index]):
        number_of_cards[index + idx + 1] += 1 * number_of_cards[index]

print(sum(number_of_cards.values()))