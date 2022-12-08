with open("input.txt", 'r') as input_file:
    input = input_file.read()

def part1():
    m = input.splitlines()
    m = [[int(y) for y in x] for x in m]
    v = [[0 for y in x] for x in m]
    width = len(m[0])
    height = len(input.splitlines())

    for y in range(height):
        t1, t2 = -1, -1
        for x in range(width):
            if m[y][x] > t1:
                t1 = m[y][x]
                v[y][x] = 1
            if m[y][-x - 1] > t2:
                t2 = m[y][-x - 1]
                v[y][-x + -1] = 1

    for x in range(width):
        t1, t2 = -1, -1
        for y in range(height):
            if m[y][x] > t1:
                t1 = m[y][x]
                v[y][x] = 1
            if m[-y - 1][x] > t2:
                t2 = m[-y - 1][x]
                v[-y - 1][x] = 1

    return sum([sum(x) for x in v])

def part2():
    m = [[int(y) for y in x] for x in input.splitlines()]
    width = len(m[0])
    height = len(input.splitlines())

    r = 0
    for y in range(height):
        for x in range(width):
            r1 = 0
            for a in range(1, x + 1):
                r1 += 1
                if m[y][x - a] >= m[y][x]:
                    break

            r2 = 0
            for a in range(x + 1, width):
                r2 += 1
                if m[y][a] >= m[y][x]:
                    break

            r3 = 0
            for a in range(1, y + 1):
                r3 += 1
                if m[y - a][x] >= m[y][x]:
                    break

            r4 = 0
            for a in range(y + 1, height):
                r4 += 1
                if m[a][x] >= m[y][x]:
                    break

            r = max(r, r1 * r2 * r3 * r4)
    return r

print("Part One: " + str(part1()))
print("Part Two: " + str(part2()))
