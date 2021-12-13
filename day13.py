def prepare_puzzle(puzzle):
    dots = set()
    folds = []
    for x in puzzle:
        if ',' in x:
            tmp = x.split(',')
            dots.add((int(tmp[0]), int(tmp[1])))
        elif '=' in x:
            tmp = x.split('fold along ')[1].split('=')
            folds.append((tmp[0], int(tmp[1])))
    return (dots, folds)

def fold_paper(dots, fold):
    direction, line = fold
    folded = set()
    for x, y in dots:
        if direction == 'y':
            if y > line:
                folded.add((x, line - (y-line)))
            else:
                folded.add((x, y))
        elif direction == 'x':
            if x > line:
                folded.add((line - (x-line), y))
            else:
                folded.add((x, y))
    return folded

def solve_part1(puzzle):
    dots, folds = puzzle
    return len(fold_paper(dots, folds[0]))

def solve_part2(puzzle):
    dots, folds = puzzle
    for fold in folds:
        dots = fold_paper(dots, fold)
    tmp = [['.' for _ in range(max([x for x, _ in dots])+1)] for _ in range(max([y for _, y in dots])+1)]
    for x, y in dots:
        tmp[y][x] = '#'
    for l in tmp:
        print(''.join(l))
    return 'see output before...'
