with open('input_day10.txt') as f:
    lines = [x.split() for x in f.readlines()]


screen = ['.']*240
cycle=0
x=1
x_sum = 0

for line in lines:
    if x-1 <= cycle%40 <= x+1:
        screen[cycle]='#'
    cycle+=1
    if (cycle-20)%40 ==0:
        x_sum += cycle*x 
    if line[0]=='addx':
        if x-1 <= cycle%40 <= x+1:
            screen[cycle]='#'
        cycle += 1
        if(cycle-20)%40==0:
            x_sum +=cycle*x
        x+=int(line[1])

for x in range(6):
    print(''.join(screen[x*40:x*40+40]))    