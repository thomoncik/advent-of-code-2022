import tqdm
from itertools import cycle

with open("input.txt", 'r') as input_file:
    input = input_file.read()

rocks = [
    ['..####.'],
    ['...#...',
     '..###..',
     '...#...'],
    ['....#..',
     '....#..',
     '..###..'],
    ['..#....',
     '..#....',
     '..#....',
     '..#....'],
    ['..##...',
     '..##...']
]


def is_colliding(chamber, rock, rock_height):
    chamber_idxs = set(i for i, v in enumerate(''.join(chamber[rock_height:rock_height + len(rock)])) if v != '.')
    rock_idxs = set(i for i, v in enumerate(''.join(rock)) if v != '.')
    return chamber_idxs.intersection(rock_idxs) != set()


def merge_element(a, b):
    if a == '.':
        return b
    if b == '.':
        return a
    return '.'


def combine(chamber, rock, rock_height):
    for y in range(rock_height, rock_height + len(rock)):
        l = []
        for x in range(len(chamber[y])):
            l.append(merge_element(chamber[y][x], rock[y - rock_height][x]))
        chamber[y] = ''.join(l)


def shift_rock(rock, shift):
    if shift == '<':
        for x in range(len(rock)):
            if rock[x][0] != '.':
                return
        for x in range(len(rock)):
            rock[x] = rock[x][1:] + '.'
    if shift == '>':
        for x in range(len(rock)):
            if rock[x][6:] != '.':
                return
        for x in range(len(rock)):
            rock[x] = '.' + rock[x][:6]
    return rock


def part1():
    chamber = ['.' * 7] * 4 + ['@' * 7]
    rocks_iterator = cycle(rocks)
    rock = next(rocks_iterator)
    shift_iterator = cycle(input)
    shift = next(shift_iterator)

    for n in range(2022):
        height = 0
        while True:
            shifted = [row[:] for row in rock]
            shift_rock(shifted, shift)
            shift = next(shift_iterator)
            if not is_colliding(chamber, shifted, height):
                rock = shifted

            if is_colliding(chamber, rock, height + 1):
                break
            height += 1

        combine(chamber, rock, height)

        floor = 0
        for i in range(len(chamber)):
            if any(x != '.' for x in chamber[i]):
                floor = i
                break
        rock = next(rocks_iterator)
        chamber = ['.' * 7] * (3 + len(rock)) + chamber[floor:]

    floor = 0
    for i in range(len(chamber)):
        if any(x != '.' for x in chamber[i]):
            floor = i
            break
    return len(chamber) - floor - 1


def part2():
    memo = {}
    chamber = ['.' * 7] * 4 + ['@' * 7]
    rocks_iterator = cycle(rocks)
    rock = next(rocks_iterator)
    shift_iterator = cycle(input)
    shift = next(shift_iterator)
    sni = cycle(range(len(input)))
    sn = next(sni)
    rni = cycle(range(len(rocks)))
    rn = next(rni)
    result = 0
    h = dict()

    n = 0
    while n < 1000000000000:
        print('!!', n)
        height = 0
        while True:
            shifted = [row[:] for row in rock]
            shift_rock(shifted, shift)
            shift = next(shift_iterator)
            sn = next(sni)
            rn = next(rni)
            if not is_colliding(chamber, shifted, height):
                rock = shifted

            if is_colliding(chamber, rock, height + 1):
                break
            height += 1

        combine(chamber, rock, height)

        floor = [-1] * 7
        for i in range(len(chamber)):
            if min(floor) != -1:
                break
            for j, x in enumerate(chamber[i]):
                if floor[j] == -1 and x != '.':
                    floor[j] = i
        print(floor)
        floor_level = min(floor)
        fl = max(floor)
        floor = ','.join(str(x) for x in floor)

        h[n] = len(chamber) - floor_level - 1
        print(chamber[floor_level], rn, sn)
        if result == 0 and (floor, rn, sn) in memo:
            m = memo[(floor, rn, sn)]
            print('ding ding', n, m, len(chamber) - floor_level - 1)
            period = n - m[0]
            dy = ((len(chamber) - floor_level - 1) - m[1])
            cycles = (1000000000000 - n) // period
            result = m[1] + cycles * dy
            rock = next(rocks_iterator)
            rn = next(rni)
            carry = h[m[0] + (1000000000000 - n) % period]
            print(dy, m[0], m[1], len(chamber) - floor_level - 1, period, n, carry)
            print(carry - m[1] + result)
            return result

        memo[(floor, rn, sn)] = (n, len(chamber) - floor_level - 1)
        rock = next(rocks_iterator)
        rn = next(rni)
        chamber = ['.' * 7] * (3 + len(rock)) + chamber[
                                                floor_level:]  # i've made a bug here, when trying to improve. Maybe someday i will fix it, have to find soultion half manually
        n += 1

    floor = 0
    for i in range(len(chamber)):
        if any(x != '.' for x in chamber[i]):
            floor = i
            break
    return result, (len(chamber) - floor - 1)


print("Part One: " + str(part1()))
print("Part Two: " + str(part2()))
