with open ("2022/input_day2.txt") as f:
    lines  = f.readlines()

score = 0
for line in lines:
    if line[0] ==  "A":
        if line[2] == "X":
            score += 3
        elif line[2] == "Y":
            score += 1 + 3
        else:
            score += 2 + 6        
    elif line[0] == "B":
        if line[2] == "X":
            score += 1               
        elif line[2] == "Y":
            score += 2 + 3
        else:
            score += 3 + 6
    else:
        if line[2] == "X":
            score += 2
        elif line[2] == "Y":
            score += 3 + 3
        else:
            score += 1 + 6
print(score)                              

#12460 high