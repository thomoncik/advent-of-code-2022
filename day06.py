with open("input.txt", 'r') as input_file:
    input = input_file.read()

def part1():
    r = 0
    last = []
    for line in input.splitlines():
        for a in line:
            r += 1
            last.insert(0, a)
            if len(set(last)) == 4:
                return r
            if len(last) >= 4:
                last.pop()
    return 0


def part2():
    r = 0
    last = []
    for line in input.splitlines():
        for a in line:
            r += 1
            last.insert(0, a)
            if len(set(last)) == 14:
                return r
            if len(last) >= 14:
                last.pop()
    return 0

print("Part One: " + str(part1()))
print("Part Two: " + str(part2()))
