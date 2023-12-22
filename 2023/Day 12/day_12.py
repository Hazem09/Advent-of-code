with open('2023/Day 12/day_12.txt') as f:
    data = [line.strip('\n') for line in f.readlines()]
    

def possible_arrangements(spring, grps_size):
    positions = {0: 1}
    for i, contiguous in enumerate(grps_size):
        new_positions = {}
        for k, v in positions.items():
            for n in range(k, len(spring) - sum(grps_size[i + 1:]) + len(grps_size[i + 1:])):
                if n + contiguous - 1 < len(spring) and '.' not in spring[n:n + contiguous]:
                    if (i == len(grps_size) - 1 and '#' not in spring[n + contiguous:]) or (i < len(grps_size) - 1 and n + contiguous < len(spring) and spring[n + contiguous] != '#'):
                        new_positions[n + contiguous + 1] = new_positions[n + contiguous + 1] + v if n + contiguous + 1 in new_positions else v
                if spring[n] == '#':
                    break
        positions = new_positions
    yield sum(positions.values())

def day_12(data):
    part_1, part_2 = 0, 0
    for row in data:
        spring_1, grps_size = row.split()
        spring_2 = '?'.join([spring_1 for _ in range(5)])
        
        grps_size_1 = [int(n) for n in grps_size.split(',')]
        grps_size_2 = grps_size_1*5
        
        part_1 += sum(possible_arrangements(spring_1, grps_size_1))
        part_2 += sum(possible_arrangements(spring_2, grps_size_2))
        
    print(part_1, part_2)

day_12(data)