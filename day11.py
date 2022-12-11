import operator

with open("input.txt", 'r') as input_file:
    input = input_file.read()


def exec_operation(operation, worry_level):
    loc = {'old': worry_level}
    exec(operation, globals(), loc)
    return loc['new']

def part1():
    current_monkey = None
    items = {}
    operation = {}
    test = {}
    test_result_true = {}
    test_result_false = {}

    monkeys = 0
    for line in input.splitlines():
        words = line.lstrip().split(' ')
        if words[0] == 'Monkey':
            current_monkey = int(words[1][:-1])
            monkeys += 1
        if words[0] == 'Starting':
            items[current_monkey] = [int(item.replace(',', '')) for item in words[2:]]
        if words[0] == 'Operation:':
            operation[current_monkey] = line.lstrip()[len('Operation: '):]
        if words[0] == 'Test:':
            test[current_monkey] = int(words[-1])
        if words[0] == 'If':
            if words[1] == 'true:':
                test_result_true[current_monkey] = int(words[-1])
            if words[1] == 'false:':
                test_result_false[current_monkey] = int(words[-1])

    inspections = [0 for _ in range(monkeys)]
    for round_number in range(20):
        for monkey in range(monkeys):
            for item in items[monkey]:
                inspections[monkey] += 1
                worry_level = item
                worry_level = exec_operation(operation[monkey], worry_level)
                worry_level = worry_level // 3
                if worry_level % test[monkey] == 0:
                    items[test_result_true[monkey]].append(worry_level)
                else:
                    items[test_result_false[monkey]].append(worry_level)
            items[monkey] = []

    sorted_inspections = sorted(inspections, reverse=True)
    return sorted_inspections[0] * sorted_inspections[1]
def part2():
    current_monkey = None
    items = {}
    operation = {}
    test = {}
    test_result_true = {}
    test_result_false = {}

    monkeys = 0
    for line in input.splitlines():
        words = line.lstrip().split(' ')
        if words[0] == 'Monkey':
            current_monkey = int(words[1][:-1])
            monkeys += 1
        if words[0] == 'Starting':
            items[current_monkey] = [int(item.replace(',', '')) for item in words[2:]]
        if words[0] == 'Operation:':
            operation[current_monkey] = line.lstrip()[len('Operation: '):]
        if words[0] == 'Test:':
            test[current_monkey] = int(words[-1])
        if words[0] == 'If':
            if words[1] == 'true:':
                test_result_true[current_monkey] = int(words[-1])
            if words[1] == 'false:':
                test_result_false[current_monkey] = int(words[-1])

    mod = 1
    for t in test.values():
        mod *= t

    inspections = [0 for _ in range(monkeys)]
    for round_number in range(10000):
        for monkey in range(monkeys):
            for item in items[monkey]:
                inspections[monkey] += 1
                worry_level = item
                worry_level = exec_operation(operation[monkey], worry_level) % mod
                if worry_level % test[monkey] == 0:
                    items[test_result_true[monkey]] += [worry_level]
                else:
                    items[test_result_false[monkey]] += [worry_level]
            items[monkey] = []

    sorted_inspections = sorted(inspections, reverse=True)
    return sorted_inspections[0] * sorted_inspections[1]

print("Part One: " + str(part1()))
print("Part Two: " + str(part2()))
