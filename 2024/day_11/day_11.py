"""
If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.
"""


from collections import Counter, defaultdict


def dict_solution(blinks=75):
    with open("2024/day_11/day_11.txt", "r") as fp:
        lines = fp.readlines()

    numbers = defaultdict(int, Counter([int(x) for x in lines[0].split()]))

    for blink in range(blinks):
        current = numbers.copy()
        for key, value in current.items():
            numbers[key] -= value
            if key == 0:
                numbers[1] += value
                continue
            length = len(str(key))
            if not length % 2:
                numbers[int(str(key)[int(length/2):])] += value
                numbers[int(str(key)[:int(length/2)])] += value
                continue
            numbers[key * 2024] += value
            
    print(sum(numbers.values()))


def brute_list(blinks=25):
    with open("2024/day_11/day_11.txt", "r") as fp:
        lines = fp.readlines()

    numbers = [int(x) for x in lines[0].split()]

    for blink in range(blinks):
        i = 0
        while i < len(numbers):
            current_number = numbers[i]
            if current_number == 0:
                numbers[i] = 1
                i += 1
                continue
            length = len(str(current_number))
            if not length % 2:
                numbers[i] = int(str(current_number)[int(length/2):])
                numbers.insert(i,int(str(current_number)[:int(length/2)]))
                i += 2
                continue
            numbers[i] *= 2024
            i += 1

    print(len(numbers))


dict_solution(25)
dict_solution(75)
