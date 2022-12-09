with open("input.txt", 'r') as input_file:
    input = input_file.read()

dirs = {'L': (-1, 0), 'R': (1, 0), 'U': (0, 1), 'D': (0, -1)}

def is_adjacent(head, tail):
    return abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1
def part1():
    tail_visited = {(0, 0)}
    tail_position = (0, 0)
    head_position = (0, 0)

    for line in input.splitlines():
        [direction, steps] = line.split(' ')
        for i in range(int(steps)):
            head_position = (head_position[0] + dirs[direction][0], head_position[1] + dirs[direction][1])
            while not is_adjacent(head_position, tail_position):
                diff_x = head_position[0] - tail_position[0]
                diff_y = head_position[1] - tail_position[1]
                x = diff_x // abs(diff_x) if diff_x != 0 else 0
                y = diff_y // abs(diff_y) if diff_y != 0 else 0
                tail_position = (tail_position[0] + x, tail_position[1] + y)
                tail_visited.add(tail_position)

    return len(tail_visited)

def part2():
    tail_visited = {(0, 0)}
    position = [(0, 0)] * 10

    for line in input.splitlines():
        [direction, steps] = line.split(' ')
        for _ in range(int(steps)):
            position[0] = (position[0][0] + dirs[direction][0], position[0][1] + dirs[direction][1])
            for i in range(1, 10):
                while not is_adjacent(position[i - 1], position[i]):
                    diff_x = position[i - 1][0] - position[i][0]
                    diff_y = position[i - 1][1] - position[i][1]
                    x = diff_x // abs(diff_x) if diff_x != 0 else 0
                    y = diff_y // abs(diff_y) if diff_y != 0 else 0
                    position[i] = (position[i][0] + x, position[i][1] + y)
                    tail_visited.add(position[9])
    return len(tail_visited)

print("Part One: " + str(part1()))
print("Part Two: " + str(part2()))
