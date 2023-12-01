with open ("2022/input_day2.txt") as f:
    lines  = f.readlines()

score = 0

for line in lines:

    if line[2] == "X":  
        if line[0] == "A":
            score = score + 1 + 3
        elif line[0] == "B":
            score = score + 1 
        else:
            score = score + 1 + 6

    elif line [2] == "Y":
        if line[0] == "A":
            score = score + 2 + 6
        elif line[0] == "B":
            score = score + 2 + 3
        else:
            score = score + 2

    else:
        if line[0] == "A":
            score = score + 3
        elif line[0] == "B":
            score = score + 3 + 6
        else:
            score = score + 3 + 3

print(score)


#9343
#12133 low
#right answer 13565
