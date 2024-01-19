with open ('input.txt') as f:
    lines = f.readlines()

lines =[eval(line) for line in lines]
total =[]
k=0
for _ in range(len(lines)-2):
    temp =0
    for i in range(k,k+3):
        temp += lines[i]
    total.append(temp)
    k += 1

first_num = total [0]
countincreased = 0
for a_total in total:
    if int(a_total) > int(first_num):
        countincreased += 1
    first_num = a_total

print(countincreased)        

