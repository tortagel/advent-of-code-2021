def prepare_puzzle(puzzle):
    reboot_steps = []
    for line in puzzle:
        tmp = line.split(' ')
        x, y, z = [t[2:].split('..') for t in tmp[1].split(',')]        
        reboot_steps.append((tmp[0] == 'on', (int(x[0]), int(x[1])), (int(y[0]), int(y[1])), (int(z[0]), int(z[1])) ))
    return reboot_steps

def solve_part1(puzzle):
    cubes = dict()
    for on, (x1, x2), (y1, y2), (z1, z2) in puzzle:
        for x in range(max(x1, -50), min(x2+1, 51)):
            for y in range(max(y1, -50), min(y2+1, 51)):
                for z in range(max(z1, -50), min(z2+1, 51)):
                    cubes[(x, y, z)] = on
    return len([1 for on in cubes.values() if on])

def solve_part2(puzzle):
    return None
