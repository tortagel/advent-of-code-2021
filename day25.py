def prepare_puzzle(puzzle):
    f = lambda c : [(x, y) for y, line in enumerate(puzzle) for x, t in enumerate(line) if t == c]
    return (f('>'), f('v'))

def solve_part1(puzzle):
    east, south = puzzle
    steps = 0
    changed = True
    while changed:
        changed = False
        east.sort(key=lambda tup: tup[0], reverse=False)
        old_east = east.copy()
        for x, y in old_east:
            tx = (x+1) % 139
            if (tx, y) not in old_east and (tx, y) not in south:
                changed = True
                east.remove((x, y))
                east.append((tx, y))
        south.sort(key=lambda tup: tup[1], reverse=False)
        old_south = south.copy()
        for x, y in old_south:
            ty = (y+1) % 137
            if (x, ty) not in east and (x, ty) not in old_south:
                changed = True
                south.remove((x, y))
                south.append((x, ty))
        steps += 1
    return steps

def solve_part2(puzzle):
    return None
