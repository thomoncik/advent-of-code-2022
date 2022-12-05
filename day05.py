with open("input.txt", 'r') as input_file:
    input = input_file.read()

stacks = [
    # my input here, changed to example
    list('NZ'),
    list('DCM'),
    list('P')
]

for i in range(len(stacks)):
    stacks[i] = stacks[i][::-1]

def part1():
    for l in input.splitlines():
        line = l.split(' ')
        for i in range(int(line[1])):
            a = stacks[int(line[3]) - 1].pop()
            stacks[int(line[5]) - 1].append(a)

    r = list(s.pop() for s in stacks)
    return ''.join(r)


def part2():
    for l in input.splitlines():
        line = l.split(' ')
        q = int(line[3]) - 1
        w = int(line[1])
        x = stacks[q][-w:]
        stacks[q] = stacks[q][:-w]
        stacks[int(line[5]) - 1].extend(x)

    r = list(s.pop() for s in stacks)
    return ''.join(r)

# print("Part One: " + str(part1()))
print("Part Two: " + str(part2()))
