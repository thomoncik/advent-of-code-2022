import tqdm

from sympy import pprint, Symbol, Eq, solve

with open("input.txt", 'r') as input_file:
    input = input_file.read()


def part1():
    d = {x[:4]: x[6:] for x in input.splitlines()}
    s = 'root'
    for i in tqdm.tqdm(range(len(d))):
        for k, v in d.items():
            # print(k, v)
            s = s.replace(k, '(' + v + ')')
    print(s)
    return int(eval(s))

def part2():
    d = {x[:4]: x[6:] for x in input.splitlines()}
    a, b = d['root'][0:4], d['root'][7:11]
    for _ in tqdm.tqdm(range(len(d))):
        for k, v in d.items():
            if k == 'humn':
                v = 'humn'
            if not v.isnumeric():
                a = a.replace(k, '(' + v + ')')
                b = b.replace(k, '(' + v + ')')
            else:
                a = a.replace(k, v)
                b = b.replace(k, v)

    i = a.find('humn') - 1
    j = i + 5
    while i >= 0 and j < len(a) and a[i] == '(' and a[j] == ')':
        i -= 1
        j += 1
    a = a[:i+1] + 'humn' + a[j:]

    humn = Symbol('humn')
    a = eval(a)
    eq1 = Eq(a, int(eval(b)))

    return int(solve(eq1, humn)[0])


print("Part One: " + str(part1()))
print("Part Two: " + str(part2()))
