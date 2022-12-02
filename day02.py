import itertools

with open("input.txt", 'r') as input_file:
    input = input_file.read()


def to_int(c):
    c = c.replace('A', '1')
    c = c.replace('B', '2')
    c = c.replace('C', '3')
    c = c.replace('X', '1')
    c = c.replace('Y', '2')
    c = c.replace('Z', '3')
    return int(c)


def part1():
    a = 0
    for line in input.splitlines():
        x, y = line.split(' ')
        x, y = to_int(x), to_int(y)
        # 1 - rock
        # 2 - paper
        # 3 - scissors
        if x == 1 and y == 2:
            a += 6
        elif x == 1 and y == 3:
            a += 0
        elif x == 2 and y == 1:
            a += 0
        elif x == 2 and y == 3:
            a += 6
        elif x == 3 and y == 1:
            a += 6
        elif x == 3 and y == 2:
            a += 0
        elif y == x:
            a += 3
        a += y

    return a


def part2():
    a = 0
    for line in input.splitlines():
        x, y = line.split(' ')
        x, y = to_int(x), to_int(y)
        # 1 - rock
        # 2 - paper
        # 3 - scissors
        if y == 1:
            if x == 1:
                a += 3
            if x == 2:
                a += 1
            if x == 3:
                a += 2
        if y == 2:
            a += 3 + x
        if y == 3:
            a += 6
            if x == 1:
                a += 2
            if x == 2:
                a += 3
            if x == 3:
                a += 1

    return a


print("Part One: " + str(part1()))
print("Part Two: " + str(part2()))
