import re
from functools import reduce
from operator import mul

with open('2023\Day 06\day_06.txt', 'r') as f:
    data = [line.strip('\n') for line in f.readlines()]

times = [int(time) for time in re.findall(r'\d+', data[0])]
distances = [int(time) for time in re.findall(r'\d+', data[1])]

def part_1(times, distances):
    combs = []
    for time, distance in zip(times, distances):
        win = sum(1 for j in range(time - 1) if (j * (time - j)) > distance)
        combs.append(win)

    print(reduce(mul, combs))

part_1(times,distances)


def part_2(times, distances):
    time = int(''.join(map(str, times)))
    distance = int(''.join(map(str, distances)))

    win = sum(1 for j in range(1, time) if j * (time - j) > distance)
    
    return print(win)

part_2(times, distances)