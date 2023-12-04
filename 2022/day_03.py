from utils.file_reader import read_file_to_lines


def part_one():
    file_path = "inputs/day_03.txt"

    input_list = read_file_to_lines(file_path)

    d = 0
    for line in input_list:
        size = int(len(line) / 2)
        a = line[:size]
        b = line[size:]
        for x in list(set(a)):
            
            if x in b:

                v = ord(x) - 64
                if v > 32:
                    v -= 32
                else:
                    v += 26
                d += v
    print(d)


def part_two():
    file_path = "inputs/day_03.txt"

    input_list = read_file_to_lines(file_path)
    size = len(input_list)
    d = 0
    for i in range(0, size, 3):
        a = set(input_list[i]).intersection(input_list[i+1]).intersection(input_list[i+2])
        x = list(a)[0]
        v = ord(x) - 64
        if v > 32:
            v -= 32
        else:
            v += 26
        d += v
    print(d)


def main():
    part_one()
    part_two()


if __name__ == "__main__":
    main()
