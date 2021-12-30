from math import ceil

def prepare_puzzle(puzzle):
    return [eval(x) for x in puzzle]

def add_pair(pair, n, left = True):
    if n is None:
        return pair
    if isinstance(pair, int):
        return pair + n
    if left:
        return [add_pair(pair[0], n), pair[1]]
    return [pair[0], add_pair(pair[1], n, False)]

def explode(pair, i = 0):
    if isinstance(pair, int):
        return False, None, pair, None
    left, right = pair
    if i == 4:
        return True, left, 0, right
    else:
        reduced, exp_left, left, exp_right = explode(left, i+1)
        if reduced:
            return True, exp_left, [left, add_pair(right, exp_right) ], None
        reduced, exp_left, right, exp_right = explode(right, i+1)
        if reduced:
            return True, None, [add_pair(left, exp_left, False), right], exp_right
    return False, None, pair, None

def split(pair):
    if isinstance(pair, int):
        if pair >= 10:
            return True, [pair // 2, ceil(pair / 2)]
        return False, pair
    left, right = pair
    reduced, left = split(left)
    if reduced:
        return True, [left, right]
    reduced, right = split(right)
    return reduced, [left, right]

def reduce(pair):    
    reduced, _, pair, _ = explode(pair)
    if not reduced:
        reduced, pair = split(pair)
    return reduced, pair

def addition(x, y):
    pair = [x, y]
    reduced = True
    while reduced:
        reduced, pair = reduce(pair)
    return pair

def magnitude(pair):
    left, right = pair
    if isinstance(left, list):
        left = magnitude(left)
    if isinstance(right, list):
        right = magnitude(right)
    return left * 3 + right * 2

def solve_part1(puzzle):
    sum = puzzle[0] 
    for snailfish_number in puzzle[1:]:
        sum = addition(sum, snailfish_number)
    return magnitude(sum)

def solve_part2(puzzle):
    return max([magnitude(addition(line1, line2)) for line1 in puzzle for line2 in puzzle])
