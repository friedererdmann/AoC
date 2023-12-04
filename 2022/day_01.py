from utils.file_reader import read_file_to_lines


def main():
    file_path = "inputs/day_01.txt"

    input_list = read_file_to_lines(file_path)

    y = 0
    z = 0
    a = []
    for x in input_list:
        if x != "":
            y += int(x)
        else:
            if y > z:
                z = y
            a.append(y)
            y = 0

    print (z)
    a.sort()
    print(sum(a[-3:]))


if __name__ == "__main__":
    main()
