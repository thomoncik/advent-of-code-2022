from collections import defaultdict
from functools import cache

import tqdm
import re

with open("input.txt", 'r') as input_file:
    input = input_file.read()


@cache
def resources(minute, ore, clay, obs, geode, robot_ore, robot_clay, robot_obs, robot_geode, blueprint, M=24):
    maxore = lambda x: min(x, 2 * (blueprint[1] + blueprint[2] + blueprint[3] + blueprint[5]))
    maxclay = lambda x: min(x, 2 * blueprint[4])
    maxobs = lambda x: min(x, 2 * blueprint[6])

    if minute == M:
        return (ore, clay, obs, geode), (robot_ore, robot_clay, robot_obs, robot_geode)

    can_buy_ore = ore >= blueprint[1]
    can_buy_clay = ore >= blueprint[2]
    can_buy_obs = ore >= blueprint[3] and clay >= blueprint[4]
    can_buy_geode = ore >= blueprint[5] and obs >= blueprint[6]

    to_check = []
    if can_buy_geode:
        return resources(minute + 1, maxore(ore - blueprint[5] + robot_ore), maxclay(clay + robot_clay), maxobs(obs - blueprint[6] + robot_obs),
                         geode + robot_geode, robot_ore, robot_clay, robot_obs, robot_geode + 1, blueprint, M)
    if can_buy_obs and robot_obs < blueprint[6]:
        to_check.append(
            resources(minute + 1, maxore(ore - blueprint[3] + robot_ore), maxclay(clay - blueprint[4] + robot_clay), maxobs(obs + robot_obs),
                      geode + robot_geode, robot_ore, robot_clay, robot_obs + 1, robot_geode, blueprint, M))
    if can_buy_clay and robot_clay < blueprint[4]:
        to_check.append(resources(minute + 1, maxore(ore - blueprint[2] + robot_ore), maxclay(clay + robot_clay), maxobs(obs + robot_obs),
                                  geode + robot_geode, robot_ore, robot_clay + 1, robot_obs, robot_geode, blueprint, M))
    if can_buy_ore and robot_ore < max([blueprint[1], blueprint[2], blueprint[3], blueprint[5]]):
        to_check.append(resources(minute + 1, maxore(ore - blueprint[1] + robot_ore), maxclay(clay + robot_clay), maxobs(obs + robot_obs),
                                  geode + robot_geode, robot_ore + 1, robot_clay, robot_obs, robot_geode, blueprint, M))

    to_check.append(
        resources(minute + 1, maxore(ore + robot_ore), maxclay(clay + robot_clay), maxobs(obs + robot_obs), geode + robot_geode,
                  robot_ore, robot_clay, robot_obs, robot_geode, blueprint, M))

    return max(to_check, key=lambda x: (x[0][3], x[1][3], x[0][2], x[1][2], x[0][1], x[1][1]))


def part1():
    blueprints = []
    pattern = re.compile(
        r'Blueprint (?P<id>.*?): Each ore robot costs (?P<ore>.*?) ore. Each clay robot costs (?P<clay>.*?) ore. Each obsidian robot costs (?P<obs_ore>.*?) ore and (?P<obs_clay>.*?) clay. Each geode robot costs (?P<g_ore>.*?) ore and (?P<g_obs>.*?) obsidian.')
    for line in input.splitlines():
        match = pattern.match(line)

        id = int(match.group("id"))
        ore = int(match.group("ore"))
        clay = int(match.group("clay"))
        obs_ore = int(match.group("obs_ore"))
        obs_clay = int(match.group("obs_clay"))
        g_ore = int(match.group("g_ore"))
        g_obs = int(match.group("g_obs"))
        print(id, ore, clay, obs_ore, obs_clay, g_ore, g_obs)
        blueprints.append((id, ore, clay, obs_ore, obs_clay, g_ore, g_obs))

    result = 0
    for blueprint in tqdm.tqdm(blueprints):
        max_geodes = resources(0, 0, 0, 0, 0, 1, 0, 0, 0, blueprint)
        resources.cache_clear()
        print(max_geodes)
        (_, _, _, geode), (_, _, _, _) = max_geodes
        result += geode * blueprint[0]
    return result


def part2():
    blueprints = []
    pattern = re.compile(
        r'Blueprint (?P<id>.*?): Each ore robot costs (?P<ore>.*?) ore. Each clay robot costs (?P<clay>.*?) ore. Each obsidian robot costs (?P<obs_ore>.*?) ore and (?P<obs_clay>.*?) clay. Each geode robot costs (?P<g_ore>.*?) ore and (?P<g_obs>.*?) obsidian.')
    for line in input.splitlines():
        match = pattern.match(line)

        id = int(match.group("id"))
        ore = int(match.group("ore"))
        clay = int(match.group("clay"))
        obs_ore = int(match.group("obs_ore"))
        obs_clay = int(match.group("obs_clay"))
        g_ore = int(match.group("g_ore"))
        g_obs = int(match.group("g_obs"))
        print(id, ore, clay, obs_ore, obs_clay, g_ore, g_obs)
        blueprints.append((id, ore, clay, obs_ore, obs_clay, g_ore, g_obs))

    result = 1
    for i in range(3):
        max_geodes = resources(0, 0, 0, 0, 0, 1, 0, 0, 0, blueprints[i], M=32)
        resources.cache_clear()
        print(max_geodes)
        (_, _, _, geode), (_, _, _, _) = max_geodes
        result *= geode
    return result


print("Part One: " + str(part1()))
print("Part Two: " + str(part2()))
