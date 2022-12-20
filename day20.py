import tqdm

with open("input.txt", 'r') as input_file:
    input = input_file.read()


def part1():
    inlen = len(input.splitlines())
    a = [(int(x), i) for i, x in enumerate(input.splitlines())]

    for i in tqdm.tqdm(range(inlen)):
        for j in range(inlen):
            if a[j][1] == i:
                break
        val, pos = a[j]
        a.pop(j)
        a.insert((j + val) % (inlen - 1), (val, i))

    for start in range(inlen):
        if a[start][0] == 0:
            break

    nums = [1000, 2000, 3000]
    return sum([a[(start + nums[i]) % inlen][0] for i in range(3)])


def part2():
    inlen = len(input.splitlines())
    key = 811589153
    a = [(int(x) * key, i) for i, x in enumerate(input.splitlines())]

    for _ in tqdm.tqdm(range(10)):
        for i in range(inlen):
            for j in range(inlen):
                if a[j][1] == i:
                    break
            val, pos = a[j]
            a.pop(j)
            a.insert((j + val) % (inlen - 1), (val, i))

    for start in range(inlen):
        if a[start][0] == 0:
            break

    nums = [1000, 2000, 3000]
    return sum([a[(start + nums[i]) % inlen][0] for i in range(3)])


print("Part One: " + str(part1()))
print("Part Two: " + str(part2()))
