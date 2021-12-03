def prepare_puzzle(puzzle):
    return [[int(n) for n in x] for x in puzzle]

def solve_part1(puzzle):
    gamma_rate = epsilon_rate = 0
    for bits in list(map(list, zip(*puzzle))):
        gamma_rate <<= 1
        epsilon_rate <<= 1
        if sum(bits) > len(bits) // 2:
            gamma_rate |= 1
        else:
            epsilon_rate |= 1
    return gamma_rate * epsilon_rate

def select_by_bit_criteria(selected, least_common = False):
    i = 0
    while len(selected) > 1:
        bits = list(map(list, zip(*selected)))[i]
        common = 1 if sum(bits) >= len(bits) / 2 else 0
        if least_common: common ^= 1
        selected = [n for n in selected if n[i] == common]
        i += 1
    return int(''.join([str(n) for n in selected[0]]), 2)

def solve_part2(puzzle):
    return select_by_bit_criteria(puzzle) * select_by_bit_criteria(puzzle, True)
