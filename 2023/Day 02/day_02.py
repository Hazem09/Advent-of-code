import re

with open('Day 02\day_02.txt') as f:
    data = f.readlines()
    

def day_02(data):
    total_1,total_2 = 0,0
    for line in data:
        line_split = line.split(':')
        game_num = int(re.findall(r'\d+', line_split[0])[0])
        rounds = line_split[1].split(';')     
        max_round_counts = {'red': 0, 'green': 0, 'blue': 0}
        
        for round_str in rounds:
            round_counts = {'red': 0, 'green': 0, 'blue': 0}
            round_cubes = re.findall(r'\d+ \w+', round_str)
            for cube in round_cubes:
                count, color = cube.split()
                round_counts[color] += int(count)
                if int(count) > max_round_counts[color]:
                    max_round_counts[color] = int(count)
        #part 1
        if max_round_counts['red'] <= 12 and max_round_counts['green'] <= 13 and max_round_counts['blue'] <= 14:
            total_1 += game_num
        #part 2
        temp = max_round_counts['red'] * max_round_counts['green']  * max_round_counts['blue']
        total_2 += temp
    return print(total_1,total_2)

day_02(data)


