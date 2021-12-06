def prepare_puzzle(puzzle):
    return [int(n) for n in puzzle[0].split(',')]

def simulate(puzzle, days):
    fish = {n: puzzle.count(n) for n in range(9)}
    for _ in range(days):
        c0 = fish[0]
        for n in range(1, 9):
            fish[n-1] = fish[n]
        fish[6] += c0
        fish[8] = c0
    return sum(fish.values())

def solve_part1(puzzle):
    return simulate(puzzle, 80)

def solve_part2(puzzle):
    return simulate(puzzle, 256)
