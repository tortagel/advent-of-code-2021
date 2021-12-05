from collections import Counter

def prepare_puzzle(puzzle):
    lines = []
    for line in puzzle:
        p1, p2 = line.split(' -> ')
        x1, y1 = p1.split(',')
        x2, y2 = p2.split(',')
        lines.append(((int(x1), int(y1)), (int(x2), int(y2))))
    return lines

def solve_part1(puzzle):
    points = []
    for (x1, y1), (x2, y2) in puzzle:
        if x1 == x2:
            for n in (range(y1, y2+1) if y1 < y2 else range(y2, y1+1)):
                points.append((x1, n))
        elif y1 == y2:
            for n in (range(x1, x2+1) if x1 < x2 else range(x2, x1+1)):
                points.append((n, y1))
    return len([n for n in dict(Counter(points)).values() if n > 1])

def solve_part2(puzzle):
    points = []
    for (x1, y1), (x2, y2) in puzzle:
        if x1 == x2:
            for n in (range(y1, y2+1) if y1 < y2 else range(y2, y1+1)):
                points.append((x1, n))
        elif y1 == y2:
            for n in (range(x1, x2+1) if x1 < x2 else range(x2, x1+1)):
                points.append((n, y1))
        else:
            if x1 > x2: x1, y1, x2, y2 = x2, y2, x1, y1
            change = 1 if y1 < y2 else -1
            for x, y in zip(range(x1, x2+1), range(y1, y2+change, change)):
                points.append((x, y))
    return len([n for n in dict(Counter(points)).values() if n > 1])
