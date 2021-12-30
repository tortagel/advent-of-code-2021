def prepare_puzzle(puzzle):
    image_enhancement_algorithm = {i for i, pixel in enumerate(puzzle[0]) if pixel == '#'}
    input_image = {(x, y) for y in range(len(puzzle[2:])) for x in range(len(puzzle[2])) if puzzle[2+y][x] == '#'}
    return (image_enhancement_algorithm, input_image)

def apply_image_enhancement_algorithm(input_image, image_enhancement_algorithm, dark_pixels):
    output_image = set()
    min_x = min([x for x, _ in input_image])
    max_x = max([x for x, _ in input_image])
    min_y = min([y for _, y in input_image])
    max_y = max([y for _, y in input_image])
    d = [(-1, -1), (0, -1), (1, -1), (-1, 0), (0, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    for y in range(min_y-1, max_y+2):
        for x in range(min_x-1, max_x+2):
            bin_num = 0
            for dx, dy in d:
                bin_num <<= 1
                if ((x+dx, y+dy) in input_image) == dark_pixels:
                    bin_num |= 1
            if (bin_num in image_enhancement_algorithm) != dark_pixels:
                output_image.add((x, y))
    return output_image

def solve_part1(puzzle):
    image_enhancement_algorithm, input_image = puzzle
    for i in range(2):
        input_image = apply_image_enhancement_algorithm(input_image, image_enhancement_algorithm, i % 2 == 0)
    return len(input_image)

def solve_part2(puzzle):
    image_enhancement_algorithm, input_image = puzzle
    for i in range(50):
        input_image = apply_image_enhancement_algorithm(input_image, image_enhancement_algorithm, i % 2 == 0)
    return len(input_image)
