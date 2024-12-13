
def part_two():
    with open("2024/day_13/day_13.txt", "r") as fp:
        lines = fp.readlines()
    press_a = 3
    press_b = 1
    per_button_limit = 100

    score = 0

    for i in range(0, len(lines), 4):
        move_a_x, move_a_y = [int(x.split('+')[-1]) for x in lines[i + 0].split(':')[1].split(',')] # 94, # 34

        move_b_x, move_b_y = [int(x.split('+')[-1]) for x in lines[i + 1].split(':')[1].split(',')] # 22 , # 67

        prize_x,  prize_y= [10000000000000 + int(x.split('=')[-1]) for x in lines[i + 2].split(':')[1].split(',')] # 8400, # 5400

        b = (prize_y * move_a_x - prize_x * move_a_y) / (move_b_y * move_a_x - move_b_x * move_a_y)
        a = (prize_x - (move_b_x * b)) / move_a_x
        
        if int(a) == a and int(b) == b:
            score += press_a * a + press_b * b

    print(int(score))

part_two()

def part_one():
    with open("2024/day_13/day_13.txt", "r") as fp:
        lines = fp.readlines()
    press_a = 3
    press_b = 1
    per_button_limit = 100

    score = 0

    for i in range(0, len(lines), 4):
        move_a_x, move_a_y = [int(x.split('+')[-1]) for x in lines[i + 0].split(':')[1].split(',')] # 94, # 34

        move_b_x, move_b_y = [int(x.split('+')[-1]) for x in lines[i + 1].split(':')[1].split(',')] # 22 , # 67

        prize_x,  prize_y= [int(x.split('=')[-1]) for x in lines[i + 2].split(':')[1].split(',')] # 8400, # 5400

        factor_a = move_a_x - move_a_y
        factor_b = move_b_x - move_b_y

        prize = prize_x - prize_y

        found = False
        local_score = 0

        for a in range(per_button_limit):
            for b in range(per_button_limit):
                if factor_a * a + factor_b * b - prize != 0:
                    continue
                if a * move_a_x + b * move_b_x == prize_x:
                    local_score = a * press_a + b * press_b
                    found = True
                    break
            if found: break

        if found:
            score += local_score

    print(score)
