import itertools
import functools

with open("input.txt", 'r') as input_file:
    input = input_file.read()


def part1():
    r = 0
    for line in input.splitlines():
        a = line.split('-')
        a[1] = a[1].split(',')
        if int(a[0]) <= int(a[1][1]) and int(a[1][0]) >= int(a[2]):
            r += 1
        elif int(a[1][1]) <= int(a[0]) and int(a[2]) >= int(a[1][0]):
            r += 1
    return r


def part2():
    r = 0
    for line in input.splitlines():
        a = line.split('-')
        a[1] = a[1].split(',')
        if int(a[1][0]) >= int(a[1][1]) and int(a[0]) <= int(a[2]):
            r += 1
        elif int(a[1][1]) >= int(a[1][0]) and int(a[2]) <= int(a[0]):
            r += 1
    return r


print("Part One: " + str(part1()))
print("Part Two: " + str(part2()))
