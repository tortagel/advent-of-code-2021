from operator import itemgetter 

def prepare_puzzle(puzzle):
    puzzle.append('')
    boards = []
    board = {}
    for x in puzzle[2:]:
        if x == '':
            boards.append(board)
            board = {}
        else:
            for n in [int(n) for n in x.split(' ') if n != '']:
                board[n] = False
    return ([int(n) for n in puzzle[0].split(',')], boards)

wins = [[n for n in range(i, 25, 5)] for i in range(5)]
wins.extend([list(range(25)[i:i+5]) for i in range(0, 25, 5)])

def has_won(board):
    for win in wins:
        if all(itemgetter(*win)(list(board.values()))):
            return True
    return False

def solve_part1(puzzle):
    numbers, boards = puzzle
    for number in numbers:
        for board in boards:
            if number in board: board[number] = True
            if has_won(board):
                return number * sum([key for key in board if not board[key]])

def solve_part2(puzzle):
    numbers, boards = puzzle
    for number in numbers:
        for board in boards:
            if number in board: board[number] = True
        i = 0
        while i < len(boards):
            if has_won(boards[i]):
                if len(boards) == 1:
                    return number * sum([key for key in boards[0] if not boards[0][key]])
                del boards[i]
            else:
                i += 1
