def prepare_puzzle(puzzle):
    return (int(puzzle[0].split(': ')[1]), int(puzzle[1].split(': ')[1]))

def deterministic_dice_turn(current_pos, i, score):
    current_pos = (current_pos + sum(range(i, i+3)) - 1) % 10 + 1
    score += current_pos
    i += 3
    return current_pos, i, score

def solve_part1(puzzle):
    current_pos1, current_pos2 = puzzle
    score1 = score2 = 0
    i = 1
    while score1 < 1000 and score2 < 1000:
        current_pos1, i, score1 = deterministic_dice_turn(current_pos1, i, score1)
        if score1 >= 1000: continue
        current_pos2, i, score2 = deterministic_dice_turn(current_pos2, i, score2)
    return score2 * (i - 1)

def solve_part2(puzzle):
    return None
