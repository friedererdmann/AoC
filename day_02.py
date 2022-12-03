from utils.file_reader import read_file_to_lines


def part_one():
    file_path = "inputs/day_02.txt"

    input_list = read_file_to_lines(file_path)

    a = ["A", "B", "C"]
    b = ["X", "Y", "Z"]

    score = 0
    for line in input_list:
        opponent, mine = line.split(" ")
        op_id = a.index(opponent)
        my_id = b.index(mine)
        score += my_id + 1
        outcome = my_id - op_id
        if outcome < 0: outcome += 3
        if outcome == 0:
            score += 3
        elif outcome == 1:
            # print(line)
            score += 6
        else:
            score += 0
    print(score)


def part_two():
    file_path = "inputs/day_02.txt"

    input_list = read_file_to_lines(file_path)

    a = ["A", "B", "C"]
    b = ["X", "Y", "Z"]
    c = ["Rock", "Paper", "Scissors"]

    score = 0
    for line in input_list:
        opponent, mine = line.split(" ")
        op_id = a.index(opponent)
        my_id = b.index(mine)
        score += my_id * 3 # outcome of the round
        outcome = op_id + my_id - 1
        if outcome < 0: outcome += 3
        if outcome > 2: outcome -= 3
        score += outcome + 1
    print(score)


def main():
    part_one()
    part_two()


if __name__ == "__main__":
    main()
