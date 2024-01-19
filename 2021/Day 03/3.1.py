with open ('input_day3.txt') as f:
    lines = f.readlines()


gamma_rate_bin = []
epsilon_rate_bin = []
for k in range(12):
    ones = 0
    zeros = 0
    for i in lines:
        if i[k] == '1':
            ones += 1
        else:
            zeros += 1
    if ones > zeros:
        gamma_rate_bin.append(1)
        epsilon_rate_bin.append(0)
    else:
        gamma_rate_bin.append(0)
        epsilon_rate_bin.append(1)        

gamma_rate = int("".join(str(x) for x in gamma_rate_bin), 2)
epsilon_rate = int("".join(str(x) for x in epsilon_rate_bin), 2)
print(gamma_rate)
print(epsilon_rate)

print(gamma_rate*epsilon_rate)