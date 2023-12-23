with open('2023/Day 15/day_15.txt') as f:
    data = f.readline().strip().split(',')
    
def part_1(data):
    total = 0
    for line in data:
        temp = 0
        for char in line: 
            temp = ((ord(char) + temp) * 17) % 256
        total += temp
    return print(total)

part_1(data)