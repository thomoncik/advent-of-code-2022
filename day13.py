from functools import cmp_to_key

with open("input.txt", 'r') as input_file:
    input = input_file.read()

def compare(x, y):
    for (x_val, y_val) in zip(x, y):
        if not isinstance(x_val, list) and not isinstance(y_val, list):
            if x_val < y_val:
                return -1
            elif y_val < x_val:
                return 1
        if isinstance(x_val, list) and isinstance(y_val, list):
            if compare(x_val, y_val) != 0:
                return compare(x_val, y_val)
        if not isinstance(x_val, list) and isinstance(y_val, list):
            if compare([x_val], y_val) != 0:
                return compare([x_val], y_val)
        if isinstance(x_val, list) and not isinstance(y_val, list):
            if compare(x_val, [y_val]) != 0:
                return compare(x_val, [y_val])

    if len(x) < len(y):
        return -1
    if len(y) < len(x):
        return 1
    return 0

def part1():
    lines = input.splitlines()
    i, pair = 0, 1
    result = 0
    while i < len(lines):
        left = eval(lines[i])
        right = eval(lines[i + 1])

        if compare(left, right) == -1:
            result += pair
        i += 3
        pair += 1
    return result

def part2():
    lines = input.splitlines()
    lines.append('')
    lines.append('[[2]]')
    lines.append('[[6]]')

    lines = list(map(lambda x: eval(x), filter(lambda x: not x == '', lines)))
    lines.sort(key=cmp_to_key(compare))
    a = lines.index([[2]]) + 1
    b = lines.index([[6]]) + 1
    return a * b

print("Part One: " + str(part1()))
print("Part Two: " + str(part2()))
