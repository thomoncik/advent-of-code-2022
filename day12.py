with open("input.txt", 'r') as input_file:
    input = input_file.read()

def is_adjacent(lhs, rhs):
    lhs = lhs.replace('E', 'z').replace('S', 'a')
    rhs = rhs.replace('E', 'z').replace('S', 'a')
    return ord(rhs) - ord(lhs) <= 1
def part1():
    grid = input.splitlines()
    queue = []

    distance = dict()
    for y in range(len(grid)):
        x = grid[y].find('S')
        if x != -1:
            queue.append((y, x))
            distance[(y, x)] = 0

    while queue:
        y, x = queue.pop(0)
        if grid[y][x] == 'E':
            return distance[(y, x)]

        for ny, nx in [(y, x - 1), (y, x + 1), (y - 1, x), (y + 1, x)]:
            if (ny, nx) not in distance and 0 <= nx < len(grid[0]) and 0 <= ny < len(grid) and is_adjacent(grid[y][x], grid[ny][nx]):
                queue.append((ny, nx))
                distance[(ny, nx)] = distance[(y, x)] + 1

def part2():
    grid = input.splitlines()
    queue = []

    distance = dict()
    for y in range(len(grid)):
        x = grid[y].find('S')
        if x != -1:
            queue.append((y, x))
            distance[(y, x)] = 0
        x = grid[y].find('a')
        if x != -1:
            queue.append((y, x))
            distance[(y, x)] = 0

    while queue:
        y, x = queue.pop(0)
        if grid[y][x] == 'E':
            return distance[(y, x)]

        for ny, nx in [(y, x - 1), (y, x + 1), (y - 1, x), (y + 1, x)]:
            if (ny, nx) not in distance and \
                    0 <= nx < len(grid[0]) and \
                    0 <= ny < len(grid) and \
                    is_adjacent(grid[y][x], grid[ny][nx]):
                queue.append((ny, nx))
                distance[(ny, nx)] = distance[(y, x)] + 1

print("Part One: " + str(part1()))
print("Part Two: " + str(part2()))
