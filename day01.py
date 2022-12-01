import itertools

with open("input.txt", 'r') as input_file:
    input = input_file.read()


def part1():
    sublists = [list(map(lambda x: int(x), g)) for m, g in
                itertools.groupby(input.splitlines(), key=lambda x: x.isnumeric()) if m]
    sums = map(sum, sublists)
    return max(sums)


def part2():
    sublists = [list(map(lambda x: int(x), g)) for m, g in
                itertools.groupby(input.splitlines(), key=lambda x: x.isnumeric()) if m]
    sums = map(sum, sublists)
    return sum(sorted(sums, reverse=True)[:3])


print("Part One: " + str(part1()))
print("Part Two: " + str(part2()))
