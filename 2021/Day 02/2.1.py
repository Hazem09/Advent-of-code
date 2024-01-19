with open ('input_day2.txt') as f:
    lines = f.readlines()


h_pos = 0
depth = 0 

for i in lines:
    splitted = i.split()
    if splitted[0] == 'forward':
        h_pos += int(splitted[1])
    elif splitted[0] == 'down':
        depth += int(splitted[1])
    else:
        depth -= int(splitted[1])

print(h_pos*depth)

