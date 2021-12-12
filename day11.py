def prepare_puzzle(puzzle):
    return [[int(n) for n in x] for x in puzzle]

adjacent = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]

def step(energy):
    len_x, len_y = len(energy[0]), len(energy)
    for y in range(len_y):
        for x in range(len_x):
            energy[y][x] += 1
    flashed_octopuses, flashed = set(), True
    while flashed:
        flashed = False
        for y in range(len_y):
            for x in range(len_x):
                if energy[y][x] > 9 and (x, y) not in flashed_octopuses:
                    flashed = True
                    flashed_octopuses.add((x, y))
                    for ix, iy in adjacent:
                        if y+iy >= 0 and y+iy < len_y and x+ix >= 0 and x+ix < len_x:
                            energy[y+iy][x+ix] += 1
        for x, y in flashed_octopuses:
            energy[y][x] = 0
    return flashed_octopuses

def solve_part1(puzzle):
    return sum([len(step(puzzle)) for _ in range(100)])

def solve_part2(puzzle):
    steps = 0
    while len({n for line in puzzle for n in line}) > 1:
        steps += 1
        step(puzzle)
    return steps
