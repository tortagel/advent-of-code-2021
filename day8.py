def prepare_puzzle(puzzle):
    return [ (x.split(' | ')[0].split(' '), x.split(' | ')[1].split(' ')) for x in puzzle]

def solve_part1(puzzle):
    return sum([len([_ for digit in output if len(digit) in (2, 3, 4, 7)]) for _, output in puzzle])

def solve_part2(puzzle):
    result = 0
    for patterns, output in puzzle:
        patterns.sort(key=len)

        digits = list(range(10))
        digits[1] = set(patterns[0])
        digits[7] = set(patterns[1])
        digits[4] = set(patterns[2])
        digits[8] = set(patterns[9])

        digits069 = patterns[6:9]
        digit9 = [n for n in digits069 if set(digits[4]).issubset(set(n))][0]
        digits[9] = set(digit9)
        digits069.remove(digit9)

        digit6 = digits069[0] if set(digits069[0]).union(digits[1]) == digits[8] else digits069[1]
        digits[6] = set(digit6)
        digits069.remove(digit6)
        digits[0] = set(digits069[0])

        digits235 = patterns[3:6]
        digit3 = [n for n in digits235 if set(digits[7]).issubset(set(n))][0]
        digits[3] = set(digit3)
        digits235.remove(digit3)

        digit2 = digits235[0] if set(digits235[0]).union(digits[9]) == digits[8] else digits235[1]
        digits[2] = set(digit2)
        digits235.remove(digit2)
        digits[5] = set(digits235[0])

        result += int(''.join([str(digits.index(set(digit))) for digit in output]))

    return result
