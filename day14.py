from math import ceil

with open("input.txt", 'r') as input_file:
    input = input_file.read()

def print_grid(grid, min_x, min_y, max_x, max_y):
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            print(grid[y][x], end='')
        print('')
def sand_step(grid, min_x, min_y, max_x, max_y):
    sx, sy = 500, 0
    while min_x <= sx < max_x and sy < max_y:
        if grid[sy + 1][sx] == '.':
            sy += 1
        elif grid[sy + 1][sx - 1] == '.':
            sy += 1
            sx -= 1
        elif grid[sy + 1][sx + 1] == '.':
            sy += 1
            sx += 1
        else:
            grid[sy][sx] = '+'
            break

    sand_particles = 0
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if grid[y][x] == '+':
                sand_particles += 1
    return sand_particles
def part1():
    rocks = set()
    min_x, min_y = 10000, 0
    max_x, max_y = 0, 0
    for line in input.splitlines():
        last_x, last_y = None, None
        for coord in line.split(' -> '):
            [x, y] = coord.split(',')
            x, y = int(x), int(y)
            if last_x is not None:
                if last_x == x:
                    for a in range(min(last_y, y), max(last_y, y) + 1):
                        rocks.add((x, a))
                if last_y == y:
                    for a in range(min(last_x, x), max(last_x, x) + 1):
                        rocks.add((a, y))
            last_x, last_y = x, y
            min_x, min_y = min(min_x, x), min(min_y, y)
            max_x, max_y = max(max_x, x), max(max_y, y)

    grid = [['.' for x in range(max_x + 1)] for y in range(max_y + 1)]
    for rock in rocks:
        grid[rock[1]][rock[0]] = '#'

    last_sand_len = 0
    while True:
        print_grid(grid, min_x, min_y, max_x, max_y)
        sand_len = sand_step(grid, min_x, min_y, max_x, max_y)
        if last_sand_len == sand_len:
            return sand_len
        last_sand_len = sand_len
        print('\n\n')

def part2():
    rocks = set()
    min_x, min_y = 10000, 0
    max_x, max_y = 0, 0
    for line in input.splitlines():
        last_x, last_y = None, None
        for coord in line.split(' -> '):
            [x, y] = coord.split(',')
            x, y = int(x), int(y)
            if last_x is not None:
                if last_x == x:
                    for a in range(min(last_y, y), max(last_y, y) + 1):
                        rocks.add((x, a))
                if last_y == y:
                    for a in range(min(last_x, x), max(last_x, x) + 1):
                        rocks.add((a, y))
            last_x, last_y = x, y
            min_x, min_y = min(min_x, x), min(min_y, y)
            max_x, max_y = max(max_x, x), max(max_y, y)

    min_x -= ceil(1.5 * (max_y - min_y))
    max_x += ceil(1.5 * (max_y - min_y))
    max_y += 2

    grid = [['.' for x in range(max_x + 1)] for y in range(max_y + 1)]
    for rock in rocks:
        grid[rock[1]][rock[0]] = '#'
    for x in range(min_x, max_x):
        grid[max_y][x] = '#'

    last_sand_len = 0
    i = 100
    while True:
        sand_len = sand_step(grid, min_x, min_y, max_x, max_y)
        if last_sand_len == sand_len:
            print('\n\n')
            print_grid(grid, min_x, min_y, max_x, max_y)
            return sand_len
        last_sand_len = sand_len
        i -= 1
        if i == 0:
            print('\n\n')
            print_grid(grid, min_x, min_y, max_x, max_y)
            i = 100

# print("Part One: " + str(part1()))
print("Part Two: " + str(part2()))
