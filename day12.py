def prepare_puzzle(puzzle):
    puzzle = [conn.split('-') for conn in puzzle]
    return {cave: [c[1] if c[0] == cave else c[0] for c in puzzle if c[0] == cave or c[1] == cave] for c in puzzle for cave in c}

def get_all_paths_rec(connections, current_cave, paths, path, visited, small_twice):
    if current_cave.islower():
        if current_cave in visited:
            visited[current_cave] += 1
            if current_cave != small_twice or visited[current_cave] > 2:
                return
        else:
            visited[current_cave] = 1
    for cave in connections[current_cave]:
        if cave == 'end':
            paths.add(tuple(path))
        else:
            get_all_paths_rec(connections, cave, paths, path + [cave], visited.copy(), small_twice)

def get_all_paths(connections, small_twice = None):
    paths = set()
    get_all_paths_rec(connections, 'start', paths, [], dict(), small_twice)
    return paths

def solve_part1(puzzle):
    return len(get_all_paths(puzzle))

def solve_part2(puzzle):
    paths = set()
    for small in [cave for cave in puzzle.keys() if cave.islower() and cave not in ['start', 'end']]:
        paths = paths.union(get_all_paths(puzzle, small))
    return len(paths)
