def prepare_puzzle(puzzle):
    puzzle = [[9] + [int(n) for n in x] + [9] for x in puzzle]
    temp = len(puzzle[0]) * [9]
    puzzle.insert(0, temp)
    puzzle.append(temp)
    return puzzle

adjacent = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def is_low_point(heightmap, x, y):
    return all([heightmap[y][x] < heightmap[y+iy][x+ix] for ix, iy in adjacent])

def get_basin(heightmap, x, y):
    if heightmap[y][x] == 9: return set()
    basin = {(x, y)}
    return basin.union(*[get_basin(heightmap, x+ix, y+iy) for ix, iy in adjacent if heightmap[y][x] < heightmap[y+iy][x+ix]])

def solve_part1(puzzle):
    return sum([puzzle[y][x]+1 for y in range(1, len(puzzle)-1) for x in range(1, len(puzzle[0])-1) if is_low_point(puzzle, x, y)])

def solve_part2(puzzle):
    basins = [get_basin(puzzle, x, y) for y in range(1, len(puzzle)-1) for x in range(1, len(puzzle[0])-1) if is_low_point(puzzle, x, y)]
    basins = [len(x) for x in basins]
    basins.sort()
    return basins[-1] * basins[-2] * basins[-3]
