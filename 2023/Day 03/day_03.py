import re
from collections import defaultdict
from functools import reduce
from operator import mul

with open('Day 03\day_03.txt') as f:
    data = [line.strip('\n') for line in f.readlines()]

def day_03(data):
    nums = re.compile('(\d+)')
    
    total = 0
    grid = defaultdict(list)
    
    for i,line in enumerate(data):
        for j in nums.finditer(line):
            num = int(j.group(1))
            add = False
            
            left = max(i - 1, 0)
            right = min(i + 1, len(data) - 1)
            top = max(0, j.start(1) - 1)
            bottom = min(j.end(1), len(line) - 1)
            
            for row in range(left, right + 1):
                for pos in range(top, bottom + 1):
                    c = data[row][pos]
                    if c != '.' and not c.isdigit():
                        add = True
                        if c == '*':
                            grid[(row, pos)].append(num)
            
            if add == True:
                total += num
    
    return print(total, sum([reduce(mul, x) for x in grid.values() if len(x) == 2]))

day_03(data)