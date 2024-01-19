with open ("2015\input_day1.txt") as f:
    line = f.readlines()


floor = 0
position = 0
for i in range (0,len(line[0])):

    if line[0][i] == "(":
        floor = floor + 1
    elif line[0][i] == ")":
        floor = floor - 1
    if floor == -1:
        position = i
        break
print(floor,position+1)

