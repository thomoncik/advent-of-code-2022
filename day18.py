import itertools

import tqdm

with open("input.txt", 'r') as input_file:
    input = input_file.read()


def part1():
    lines = input.splitlines()
    split = [l.split(',') for l in lines]
    coords = [[int(s) for s in l] for l in split]

    sides = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]
    result = 0
    for x, y, z in coords:
        for nx, ny, nz in sides:
            if [x + nx, y + ny, z + nz] not in coords:
                result += 1
    return result


def part2():
    lines = input.splitlines()
    split = [l.split(',') for l in lines]
    coords = set(tuple(int(s) for s in l) for l in split)

    sides = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]

    q = [(-1, -1, -1)]
    visited = set()
    while q:
        x, y, z = q.pop()
        neighbours = {(x + nx, y + ny, z + nz) for nx, ny, nz in sides}
        q += [s for s in (neighbours - coords - visited) if all(-1 <= c <= 30 for c in s)]
        visited.update({(x, y, z)})

    result = 0
    for x, y, z in coords:
        for nx, ny, nz in sides:
            if (x + nx, y + ny, z + nz) in visited:
                result += 1
    return result


print("Part One: " + str(part1()))
print("Part Two: " + str(part2()))

