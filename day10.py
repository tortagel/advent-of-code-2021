def prepare_puzzle(puzzle):
    return puzzle

brackets = {'(': ')', '[': ']', '{': '}', '<': '>'}

def solve_part1(puzzle):
    lookup = {')': 3, ']': 57, '}': 1197, '>': 25137}
    syntax_error_score = 0
    for chunks in puzzle:
        stack = []
        for chunk in chunks:
            if chunk in brackets:
                stack.append(chunk)
            elif brackets[stack.pop()] != chunk:
                syntax_error_score += lookup[chunk]
                break
    return syntax_error_score

def solve_part2(puzzle):
    lookup = {')': 1, ']': 2, '}': 3, '>': 4}    
    scores = []
    for chunks in puzzle:
        stack = []
        for chunk in chunks:
            if chunk in brackets:
                stack.append(chunk)
            elif brackets[stack.pop()] != chunk:
                stack = []
                break
        if len(stack) > 0:
            scores.append(sum([lookup[brackets[chunk]] * 5**(len(stack)-i-1) for i, chunk in enumerate(stack[::-1])]))
    scores.sort()
    return scores[len(scores)//2]
