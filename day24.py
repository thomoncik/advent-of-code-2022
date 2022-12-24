from functools import cache

with open("input.txt", 'r') as input_file:
    input = input_file.read()

grid = input.splitlines()


@cache
def step_blizzards(bz):
    b = []
    for ((by, bx), (dy, dx)) in bz:
        if grid[by + dy][bx + dx] == '#':
            if (dy, dx) == (1, 0):
                b.append(((1, bx), (dy, dx)))
            if (dy, dx) == (-1, 0):
                b.append(((len(grid) - 2, bx), (dy, dx)))
            if (dy, dx) == (0, 1):
                b.append(((by, 1), (dy, dx)))
            if (dy, dx) == (0, -1):
                b.append(((by, len(grid[0]) - 2), (dy, dx)))
        else:
            b.append(((by + dy, bx + dx), (dy, dx)))
    return {(q, w) for ((q, w), _) in b}, tuple(sorted(b))


def part1():
    blizzards = set()  # ((y, x), (diry, dirx))
    bz = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == '>':
                blizzards.add((y, x))
                bz.append(((y, x), (0, 1)))
            if grid[y][x] == 'v':
                blizzards.add((y, x))
                bz.append(((y, x), (1, 0)))
            if grid[y][x] == '<':
                blizzards.add((y, x))
                bz.append(((y, x), (0, -1)))
            if grid[y][x] == '^':
                blizzards.add((y, x))
                bz.append(((y, x), (-1, 0)))
    bz = tuple(sorted(bz))

    start = (0, 1)  # y,x
    end = (len(grid) - 1, grid[-1].find('.'))

    queue = [(start, 1)]
    visited = {(start, bz)}
    minute = 0

    while queue:
        ((y, x), distance) = queue.pop(0)
        if (y, x) == end:
            return minute - 1

        if distance > minute:
            blizzards, bz = step_blizzards(bz)
            minute = distance

        for ny, nx in [(y, x - 1), (y, x + 1), (y - 1, x), (y + 1, x), (y, x)]:
            if not 0 <= nx < len(grid[0]) or not 0 <= ny < len(grid):
                continue
            if (ny, nx) not in blizzards and ((ny, nx), bz) not in visited and grid[ny][nx] != '#':
                visited.add(((ny, nx), bz))
                queue.append(((ny, nx), distance + 1))
    return None


def part2():
    blizzards = set()  # ((y, x), (diry, dirx))
    bz = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == '>':
                blizzards.add((y, x))
                bz.append(((y, x), (0, 1)))
            if grid[y][x] == 'v':
                blizzards.add((y, x))
                bz.append(((y, x), (1, 0)))
            if grid[y][x] == '<':
                blizzards.add((y, x))
                bz.append(((y, x), (0, -1)))
            if grid[y][x] == '^':
                blizzards.add((y, x))
                bz.append(((y, x), (-1, 0)))
    bz = tuple(sorted(bz))

    def dist(start, end, bz):
        queue = [(start, 1)]
        visited = {(start, bz)}
        minute = 0

        while queue:
            ((y, x), distance) = queue.pop(0)
            if (y, x) == end:
                return distance - 1, step_blizzards(bz)[1]

            if distance > minute:
                blizzards, bz = step_blizzards(bz)
                minute = distance

            for ny, nx in [(y, x - 1), (y, x + 1), (y - 1, x), (y + 1, x), (y, x)]:
                if not 0 <= nx < len(grid[0]) or not 0 <= ny < len(grid):
                    continue
                if (ny, nx) not in blizzards and ((ny, nx), bz) not in visited and grid[ny][nx] != '#':
                    visited.add(((ny, nx), bz))
                    queue.append(((ny, nx), distance + 1))
        return 0, bz

    start = (0, 1)  # y,x
    end = (len(grid) - 1, grid[-1].find('.'))

    dist1, bz = dist(start, end, bz)
    dist2, bz = dist(end, start, bz)
    dist3, bz = dist(start, end, bz)

    return dist1 + dist2 + dist3 + 4

print("Part One: " + str(part1()))
print("Part Two: " + str(part2()))
