from math import ceil

def prepare_puzzle(puzzle):
    return (puzzle[0], {x.split(' -> ')[0]: x.split(' -> ')[1] for x in puzzle[2:]})

def insert_pairs(pairs, rules):
    new_pairs = dict()
    for k in pairs:
        if k in rules:
            new_pairs[k[0] + rules[k]] = new_pairs.get(k[0] + rules[k], 0) + pairs[k]
            new_pairs[rules[k] + k[1]] = new_pairs.get(rules[k] + k[1], 0) + pairs[k]
        else:
            new_pairs[k] = pairs[k]
    return new_pairs

def apply_steps(template, rules, steps):
    pairs = {template[i:i+2]: 1 for i in range(len(template)-1)}
    for _ in range(steps):
        pairs = insert_pairs(pairs, rules)
    counter = dict()
    for k in pairs:
        counter[k[0]] = counter.get(k[0], 0) + pairs[k]
        counter[k[1]] = counter.get(k[1], 0) + pairs[k]
    counts = [n // 2 + (1 if template[0] == k or template[-1] == k else 0) for k, n in counter.items()]
    counts.sort()
    return counts[-1] - counts[0]

def solve_part1(puzzle):
    return apply_steps(puzzle[0], puzzle[1], 10)

def solve_part2(puzzle):
    return apply_steps(puzzle[0], puzzle[1], 40)
