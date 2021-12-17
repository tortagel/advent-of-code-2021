def prepare_puzzle(puzzle):
    tmp = puzzle[0].split('x=')[1].split(', y=')
    x_target, y_target = tmp[0].split('..'), tmp[1].split('..')
    return (int(x_target[0]), int(y_target[0])), (int(x_target[1]), int(y_target[1]))

def move(x, y, vx, vy):
    x += vx
    y += vy
    if vx > 0: vx -= 1
    elif vx < 0: vx += 1
    vy -= 1
    return (x, y, vx, vy)

def check_velocity(vx, vy, max_x, max_y, target_area):
    x = y = highest_y = 0
    while (x, y) not in target_area and x <= max_x and y >= max_y:
        x, y, vx, vy = move(x, y, vx, vy)
        if y > highest_y:
            highest_y = y
    return (x, y) in target_area, highest_y

def get_velocities(x1, y1, x2, y2):
    target_area = {(x, y) for y in range(y1, y2+1) for x in range(x1, x2+1)}
    velocities = set()
    hights = []
    for vx in range(1, x2+1):
        for vy in range(y1, -y1):
            ok, highest_y = check_velocity(vx, vy, x2, y1, target_area)
            if ok:
                velocities.add((vx, vy))
                hights.append(highest_y)
    return velocities, max(hights)

def solve_part1(puzzle):
    (x1, y1), (x2, y2) = puzzle
    _, highest_y = get_velocities(x1, y1, x2, y2)
    return highest_y

def solve_part2(puzzle):
    (x1, y1), (x2, y2) = puzzle
    velocities, _ = get_velocities(x1, y1, x2, y2)
    return len(velocities)
