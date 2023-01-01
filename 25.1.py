with open("input_day25.txt") as f:
    lines = [line.strip('\n') for line in f.readlines()]

dict = {'2':2,'1':1,'-':-1,'=':-2,'0':0}

count=0
for line in lines:
    for i in range(len(line)):
        count += 5**(len(line)-i-1)*dict[line[i]]

print(count)

snafu=''
rest =0

while count!=0 or rest:
    remainder = count %5 + rest
    rest = 0
    if remainder >2:
        rest = 1
    snafu= {0: "0", 1: "1", 2: "2", 3: "=", 4: "-", 5: "0"}[remainder] + snafu
    count //=5
print(snafu)

