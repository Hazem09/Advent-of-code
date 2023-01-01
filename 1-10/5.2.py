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

k=0
for line in lines:
    move = [int(s) for s in line.split() if s.isdigit()]
    stacks[move[2]-1].extend(stacks[move[1]-1][len(stacks[move[1]-1])-move[1]:move[1]])
    k+=1
    print(k)
    for i in range(0,move[0]):
        if stacks[move[1]-1] == []:
            continue
        else:
            stacks[move[1]-1].pop()
    
    


print(stacks)
solution =''
for stack in stacks:
    solution += stack.pop()

print(solution)    
    

#right answer CJVLJQPHS