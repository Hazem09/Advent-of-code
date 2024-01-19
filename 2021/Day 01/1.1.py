with open ('input.txt') as f:
    lines = f.readlines()


countincreased = 0
first_num = lines[0]



for line in lines:
    if int(line) > int(first_num):
        countincreased += 1
    first_num = line    



print(countincreased)