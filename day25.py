import math
from functools import cache

with open("input.txt", 'r') as input_file:
    input = input_file.read()


def part1():
    sum = 0
    n = 0
    for line in input.splitlines():
        m = 1
        for x in reversed(line):
            if x.isdigit():
                n += int(x) * m
            if x == '-':
                n += -1 * m
            if x == '=':
                n += -2 * m
            m *= 5
        sum += n

    p = 1
    out = []
    while n > 0:
        r = n % 5
        if r in range(0, 2 + 1):
            out.append(str(r))
            n //= 5
        elif r == 3:
            out.append('=')
            n //= 5
            n += 1
        elif r == 4:
            out.append('-')
            n //= 5
            n += 1

        p *= 5
    return ''.join(reversed(out))
def part2():
    pass

print("Part One: " + str(part1()))
print("Part Two: " + str(part2()))
