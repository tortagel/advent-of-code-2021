def prepare_puzzle(puzzle):
    return [int(n) for n in puzzle]

def solve_part1(puzzle):
    return sum([1 for i, n in enumerate(puzzle[1:]) if n > puzzle[i]])

def solve_part2(puzzle):    
    return sum([1 for i in range(len(puzzle)-3) if sum(puzzle[i+1:i+4]) > sum(puzzle[i:i+3])])
