with open ("input_day5.txt") as f:
    lines = f.readlines()[10:]

stacks=[['B','V','S','N','T','C','H','Q'],
    ['W','D','B','G'],
    ['F','W','R','T','S','Q','B'],
    ['L','G','W','S','Z','J','D','N'],
    ['M','P','D','V','F'],
    ['F','W','J'],
    ['L','N','Q','B','J','V'],
    ['G','T','R','C','J','Q','S','N'],
    ['J','S','Q','C','W','D','M']]

for line in lines:
    move = [int(s) for s in line.split() if s.isdigit()]

    for i in range(0,move[0]):
        inter = stacks[move[1]-1].pop()
        stacks[move[2]-1].append(inter)

solution =''
for stack in stacks:
    solution += stack.pop()

print(solution)    
    