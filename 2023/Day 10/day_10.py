

with open('2023\Day 10\day_10.txt') as f:
    data =[line.strip('\n') for line in f.readlines()]
    
grid = []
for y, line in enumerate(data):
    grid.append(line)
    S_pos = line.find('S')
    if S_pos != -1:
        x1, y1 = S_pos, y
x, y, steps = x1, y1, 0

if x < len(grid[0]) - 1 and grid[y][x + 1] in {'-', 'J', '7'}:
    direction = 1
elif y < len(grid) - 1 and grid[y + 1][x] in {'|', 'J', 'L'}:
    direction = 2
if x > 0 and grid[y][x - 1] in {'-', 'F', 'L'}:
    direction = 3
if y > 1 and grid[y - 1][x] in {'|', 'F', '7'}:
    direction = 0
while True:
    match direction:
        case 0:
            y -= 1
        case 1:
            x += 1
        case 2:
            y += 1
        case 3:
            x -= 1
    match grid[y][x]:
        case 'L':
            direction = 1 if direction == 2 else 0
        case 'J':
            direction = 3 if direction == 2 else 0
        case '7':
            direction = 2 if direction == 1 else 3
        case 'F':
            direction = 2 if direction == 3 else 1
    steps += 1
    if x1 == x and y1 == y:
        print(steps // 2 + (1 if steps % 2 == 1 else 0))
        break