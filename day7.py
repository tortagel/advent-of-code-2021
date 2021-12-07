def prepare_puzzle(puzzle):
    return [int(n) for n in puzzle[0].split(',')]

def solve_part1(puzzle):
    return min([sum([abs(n2 - n1) for n2 in puzzle]) for n1 in range(max(puzzle)+1)])

def solve_part2(puzzle):
    f = lambda n: n * (n + 1) // 2
    return min([sum([f(abs(n2 - n1)) for n2 in puzzle]) for n1 in range(max(puzzle)+1)])
