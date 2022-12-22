with open("input.txt", 'r') as input_file:
    input = input_file.read()

direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def part1():
    grid, path = input.splitlines()[:-2], input.splitlines()[-1]
    facing = 0

    path = path.replace('R', 'R ').replace('L', 'L ') + '_'
    path = [(int(x[:-1]), 0 if x[-1] == '_' else (1 if x[-1] == 'R' else -1)) for x in path.split(' ')]

    max_line = max(len(line) for line in grid)
    grid = [' ' + line + (' ' * (max_line - len(line) + 1)) for line in grid]
    grid = [' ' * len(grid[0])] + grid + [' ' * len(grid[0])]
    position = [grid[1].find('.'), 1]

    for step, rotate in path:
        for _ in range(step):
            next_position = [position[0] + direction[facing][0], position[1] + direction[facing][1]]
            if grid[next_position[1]][next_position[0]] in {' '}:
                if direction[facing][0] == 1:
                    a = grid[next_position[1]].find('.')
                    b = grid[next_position[1]].find('#')
                    if min(a, b) == b:
                        next_position[0] = position[0]
                        break
                    else:
                        next_position[0] = a
                if direction[facing][0] == -1:
                    a = grid[next_position[1]].rfind('.')
                    b = grid[next_position[1]].rfind('#')
                    if max(a, b) == b:
                        next_position[0] = position[0]
                        break
                    else:
                        next_position[0] = a

                if direction[facing][1] == 1:
                    y = 0
                    while True:
                        if len(grid[y]) > next_position[0] and grid[y][next_position[0]] not in {' '}:
                            break
                        y += 1
                        if y == len(grid):
                            y = 0
                    if grid[y][next_position[0]] == '.':
                        next_position[1] = y
                    else:
                        next_position[1] = position[1]
                        break
                if direction[facing][1] == -1:
                    y = len(grid) - 1
                    while True:
                        if len(grid[y]) > next_position[0] and grid[y][next_position[0]] not in {' '}:
                            break
                        y -= 1
                        if y == 0:
                            y = len(grid) - 1
                    if grid[y][next_position[0]] == '.':
                        next_position[1] = y
                    else:
                        next_position[1] = position[1]
                        break
            if grid[next_position[1]][next_position[0]] == '.':
                position = next_position
            else:
                break
        facing += rotate
        facing %= 4

    return 1000 * position[1] + 4 * position[0] + facing


def part2():
    grid, path = input.splitlines()[:-2], input.splitlines()[-1]
    facing = 0

    path = path.replace('R', 'R ').replace('L', 'L ') + '_'
    path = [(int(x[:-1]), 0 if x[-1] == '_' else (1 if x[-1] == 'R' else -1)) for x in path.split(' ')]

    max_line = max(len(line) for line in grid)
    grid = [' ' + line + (' ' * (max_line - len(line) + 1)) for line in grid]
    grid = [' ' * len(grid[0])] + grid + [' ' * len(grid[0])]
    position = (grid[1].find('.'), 1)

    for step, rotate in path:
        for _ in range(step):
            cx = (position[0] - 1) // 50
            cy = (position[1] - 1) // 50
            next_position = [position[0] + direction[facing][0], position[1] + direction[facing][1]]
            foo = direction[facing]
            if grid[next_position[1]][next_position[0]] == ' ':
                if direction[facing][0] == 1:
                    if (cx, cy) == (2, 0):
                        next_position[0] = 100
                        next_position[1] = 151 - next_position[1]
                        facing = direction.index((-1, 0))
                    if (cx, cy) == (1, 1):
                        next_position[0] = next_position[1] + 50
                        next_position[1] = 50
                        facing = direction.index((0, -1))
                    if (cx, cy) == (1, 2):
                        next_position[0] = 150
                        next_position[1] = 150 - next_position[1]
                        facing = direction.index((-1, 0))
                    if (cx, cy) == (0, 3):
                        next_position[0] = next_position[1] - 100
                        next_position[1] = 150
                        facing = direction.index((0, -1))
                elif direction[facing][0] == -1:
                    if (cx, cy) == (1, 0):
                        next_position[0] = 1
                        next_position[1] = 150 - next_position[1] + 1
                        facing = direction.index((1, 0))
                    if (cx, cy) == (1, 1):
                        next_position[0] = next_position[1] - 50
                        next_position[1] = 101
                        facing = direction.index((0, 1))
                    if (cx, cy) == (0, 2):
                        next_position[0] = 51
                        next_position[1] = 151 - next_position[1]
                        facing = direction.index((1, 0))
                    if (cx, cy) == (0, 3):
                        next_position[0] = next_position[1] - 100
                        next_position[1] = 1
                        facing = direction.index((0, 1))
                elif direction[facing][1] == 1:
                    if (cx, cy) == (0, 3):
                        next_position[1] = 1
                        next_position[0] += 100
                        facing = direction.index((0, 1))
                    if (cx, cy) == (1, 2):
                        next_position[1] = next_position[0] + 100
                        next_position[0] = 50
                        facing = direction.index((-1, 0))
                    if (cx, cy) == (2, 0):
                        next_position[1] = next_position[0] - 50
                        next_position[0] = 100
                        facing = direction.index((-1, 0))
                elif direction[facing][1] == -1:
                    if (cx, cy) == (0, 2):
                        next_position[1] = next_position[0] + 50
                        next_position[0] = 51
                        facing = direction.index((1, 0))
                    if (cx, cy) == (1, 0):
                        next_position[1] = next_position[0] + 100
                        next_position[0] = 1
                        facing = direction.index((1, 0))
                    if (cx, cy) == (2, 0):
                        next_position[1] = 200
                        next_position[0] = next_position[0] - 100
                        facing = direction.index((0, -1))

            if grid[next_position[1]][next_position[0]] == '.':
                position = next_position
            else:
                if grid[next_position[1]][next_position[0]] == ' ':
                    print('position', position, cx, cy)
                    print('next_position', next_position)
                    print('was heading', foo)
                    exit(1)
        facing += rotate
        facing %= 4

    return 1000 * position[1] + 4 * position[0] + facing


print("Part One: " + str(part1()))
print("Part Two: " + str(part2()))
