with open('2023\Day 05\day_05.txt', 'r') as f:
    data = [line.strip() for line in f.readlines()]


def part_1(data):
    seeds = [int(seed) for seed in data[0][7:].split()]
    changed = [False] * len(seeds)
    for line in data[1:]:
        if line:
            if not line.endswith(':'):
                map = [int(val) for val in line.split()]
                for i in range(len(seeds)):
                    if not changed[i] and map[1] <= seeds[i] < map[1] + map[2]:
                        seeds[i] = map[0] + seeds[i] - map[1]
                        changed[i] = True
            else:
                changed = [False] * len(seeds)

    return print(min(seeds))

part_1(data)