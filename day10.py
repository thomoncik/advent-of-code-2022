with open("input.txt", 'r') as input_file:
    input = input_file.read()

def part1():
    i = 1
    register = 1
    result = 0
    for line in input.splitlines():
        cmd = line.split(' ')
        if i == 20 or (i - 20) % 40 == 0:
            result += i * register
        if cmd[0] == 'noop':
            pass
        if cmd[0] == 'addx':
            i += 1
            if i == 20 or (i - 20) % 40 == 0:
                result += i * register
            register += int(cmd[1])
        i += 1
    return result

def print_pixel(cycle, result, register):
    result += '#' if abs(register + 1 - (cycle % 40)) <= 1 else '.'
    result += '\n' if cycle % 40 == 0 else ''
    return result

def part2():
    cycle, register = 1, 1
    result = '\n'
    for line in input.splitlines():
        result = print_pixel(cycle, result, register)
        cycle += 1

        cmd = line.split(' ')
        if cmd[0] == 'addx':
            result = print_pixel(cycle, result, register)
            cycle += 1
            register += int(cmd[1])

    return result

print("Part One: " + str(part1()))
print("Part Two: " + str(part2()))
