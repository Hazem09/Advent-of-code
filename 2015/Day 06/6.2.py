import re

with open ("input_day6.txt") as f:   
    lines=[x.strip('\n') for x in f.readlines()]
    
commands=[]
coordinates=[]
for line in lines:
    match_1 = re.findall('\d+',line)
    match_2 = re.findall('on|off|toggle',line)
    coordinates.append(match_1)
    commands.append(match_2)


lights = [[0 for _ in range(1000)] for _ in range(1000)]


for i,j in zip(commands,coordinates):
    coord_0,coord_1,coord_2,coord_3=int(j[0]),int(j[1]),int(j[2]),int(j[3])
    if i[0] == 'toggle': 
        for k in range(coord_0,coord_2+1):
            for l in range(coord_1,coord_3+1):
                lights[k][l] += 2


    elif i[0] == 'on':
        for k in range(coord_0,coord_2+1):
            for l in range(coord_1,coord_3+1):
                    lights[k][l] += 1

    else:  
            for k in range(coord_0,coord_2+1):
                for l in range(coord_1,coord_3+1):
                    if lights[k][l] > 0:
                        lights[k][l] -= 1   

lights_on = sum(light for row in lights for light in row)

print(lights_on)