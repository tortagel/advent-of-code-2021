def prepare_puzzle(puzzle):
    return [(x.split(' ')[0], int(x.split(' ')[1])) for x in puzzle]

def solve_part1(puzzle):
    pos = depth = 0
    for direction, n in puzzle:
        if direction == 'forward':
            pos += n
        elif direction == 'up':
            depth -= n
        elif direction == 'down':
            depth += n
    return pos * depth

def solve_part2(puzzle):
    pos = depth = aim = 0
    for direction, n in puzzle:
        if direction == 'forward':
            pos += n
            depth += aim * n
        elif direction == 'up':
            aim -= n
        elif direction == 'down':
            aim += n
    return pos * depth
