from collections import defaultdict
from functools import cache

import tqdm

with open("input.txt", 'r') as input_file:
    input = input_file.read()


def part1():
    tunnel = dict()
    flow = dict()
    # Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
    for line in input.splitlines():
        l = line.split(' ')
        tunnel[l[1]] = [x.replace(',', '') for x in l[9:]]
        flow[l[1]] = int(l[4][5:-1])

    states = [('AA', frozenset(), 0)]
    best = {}

    for t in range(1, 30 + 1):
        next_states = []
        for valve, opened, pressure in states:
            key = (valve, opened)
            if key in best and pressure <= best[key]:
                continue

            best[key] = pressure

            if valve not in opened and flow[valve] > 0:
                next_states.append((valve, opened.union({valve}), pressure + flow[valve] * (30 - t)))
            for dest in tunnel[valve]:
                next_states.append((dest, opened, pressure))

        states = next_states

    return max(pressure for _, _, pressure in states)


def part2():
    tunnel = dict()
    flow = dict()
    # Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
    for line in input.splitlines():
        l = line.split(' ')
        tunnel[l[1]] = [x.replace(',', '') for x in l[9:]]
        if l[4][5:-1] != '0':
            flow[l[1]] = int(l[4][5:-1])

    dist = defaultdict(lambda: float('inf'))
    for v1, neighbours in tunnel.items():
        for v2 in neighbours:
            dist[v1, v2] = 1

    for u in tunnel.keys():
        for v1 in tunnel.keys():
            for v2 in tunnel.keys():
                if dist[v1, v2] > dist[v1, u] + dist[u, v2]:
                    dist[v1, v2] = dist[v1, u] + dist[u, v2]

    available_from = {}
    for k, v in dist.keys():
        if k not in flow == 0:
            continue
        if k != v and v in flow:
            available_from.setdefault(k, []).append((v, dist[k, v]))

    @cache
    def search(t, current='AA', nodes=frozenset(flow), elephant=False):
        return max(
            [flow[v] * (t - dist[current, v] - 1) +
             search(t - dist[current, v] - 1, v, nodes - {v}, elephant)
             for v in nodes if dist[current, v] < t] +
            [search(26, 'AA', nodes, elephant=False) if elephant else 0])

    return search(26, elephant=True)


print("Part One: " + str(part1()))
print("Part Two: " + str(part2()))
