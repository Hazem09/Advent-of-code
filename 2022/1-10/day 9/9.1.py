with open('1-10\input_day9.txt') as f:
    lines = [x.split() for x in f.readlines()]

def is_close(h_pos,t_pos):
    distance = [abs(x-y) for x,y in zip(h_pos, t_pos) if abs(x-y) <= 1]
    if len(distance) == 2:
        return True
    return False




def move(i,h_pos,t_pos):
    dic = {'U': [0, 1], 'D': [0, -1],'R': [1, 0],'L': [-1, 0]}
    h_init = h_pos
    h_pos = [(x+y) for x,y in zip(dic[i], h_init)]

    if is_close(h_pos,t_pos):
        return h_pos,t_pos
    else:
        if h_pos[0]==t_pos[0]:
    
            if h_pos[1] > t_pos[1]:
                t_pos = [t_pos[0],t_pos[1]+1]
            else:
                t_pos = [t_pos[0],t_pos[1]-1]

        elif h_pos[1] == t_pos[1]:
            if h_pos[0] > t_pos[0]:
                t_pos=[t_pos[0]+1,t_pos[1]]
            else:
                t_pos=[t_pos[0]-1,t_pos[1]]


        else:
            direction = [True if z > 0 else False for z in [(x-y) for x, y in zip(h_pos, t_pos)]]
            # True means positive
            if direction == [True, True]:
                t_pos  = [t_pos[0] + 1, t_pos[1] + 1]
            if direction == [False, True]:
                t_pos  = [t_pos[0] - 1, t_pos[1] + 1]            
            if direction == [False, False]:
                t_pos  = [t_pos[0] - 1, t_pos[1] - 1]    
            if direction == [True, False]:
                t_pos  = [t_pos[0] + 1, t_pos[1] - 1]

    return h_pos, t_pos

h_current ,t_current=[0,0],[0,0]
h_moves,t_moves=[],[]


moves = ''
for i in lines: 
    moves += i[0] * int(i[1])

t_tails =[]
for i in moves:
    a, b = move(i, h_current, t_current)
    h_current = a
    t_current = b

    if t_current not in t_tails:
        t_tails.append(t_current)

print(len(t_tails))



#Part 1: 6175
#Part 2: 2578