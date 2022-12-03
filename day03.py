import itertools
import functools

with open("input.txt", 'r') as input_file:
    input = input_file.read()


def part1():
    r = 0
    for line in input.splitlines():
        half = len(line) // 2
        a = set(line[:half])
        b = set(line[half:])
        r += score(a.intersection(b).pop())
    return r


def part2():
    lines = input.splitlines()
    r = 0
    for i in range(0, len(lines), 3):
        chunk = lines[i:i + 3]
        x = functools.reduce(lambda a, b: set(a).intersection(b), chunk)
        r += score(x.pop())
    return r


def score(x):
    if x == x.lower():
        return ord(x) - ord('a') + 1
    else:
        return ord(x) - ord('A') + 27


print("Part One: " + str(part1()))
print("Part Two: " + str(part2()))
