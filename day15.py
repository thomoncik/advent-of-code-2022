import tqdm

with open("input.txt", 'r') as input_file:
    input = input_file.read()

def distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def tuning_freq(x, y):
    return x * 4000000 + y

def part1():
    row_to_check = 2000000
    potential_beacons_x = set()

    for i, line in enumerate(input.splitlines()):
        filtered_line = ''.join(filter(lambda x: x.isnumeric() or x in [',', ":", '-'], line.replace(':', ','))).split(',')
        [sensor_x, sensor_y, beacon_x, beacon_y] = [int(x) for x in filtered_line]
        dist = distance(sensor_x, sensor_y, beacon_x, beacon_y)

        diff = dist - abs(sensor_y - row_to_check)
        potential_beacons_x.update(range(sensor_x - diff, sensor_x + diff + 1))
        if beacon_y == row_to_check:
            potential_beacons_x.discard(beacon_x)

    return len(potential_beacons_x)

def part2():
    limit = 20
    potential = set()

    points = []
    for line in input.splitlines():
        filtered_line = ''.join(filter(lambda x: x.isnumeric() or x in [',', ":", '-'], line.replace(':', ','))).split(',')
        points.append([int(x) for x in filtered_line])

    for sensor_x, sensor_y, beacon_x, beacon_y in tqdm.tqdm(points):
        dist = distance(sensor_x, sensor_y, beacon_x, beacon_y) + 1

        for x in range(sensor_x - dist, sensor_x + dist + 1):
            y = sensor_y + (dist - abs(sensor_x - x))
            if (0 <= x <= limit) and (0 <= y <= limit):
                potential.add((x, y))
            y = sensor_y - (dist - abs(sensor_x - x))
            if (0 <= x <= limit) and (0 <= y <= limit):
                potential.add((x, y))

    for x, y in tqdm.tqdm(potential):
        if all(distance(sx, sy, x, y) > distance(sx, sy, bx, by) for sx, sy, bx, by in points):
            return tuning_freq(x, y)


# print("Part One: " + str(part1()))
print("Part Two: " + str(part2()))
