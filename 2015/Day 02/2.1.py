with open ("2015\input_day2.txt") as f:
    lines = f.readlines()

area = 0

for line in lines:
    length, width, height = line.split('x')
    
    sides = []
    sides.append(2 * int(length) * int(width))
    sides.append(2 * int(width) * int(height))
    sides.append(2 * int(height) * int(length))   

    slack = min(sides) // 2
    area += slack + sum(sides)


print(area)

