with open('input_day10.txt') as f:
    lines = [x.split() for x in f.readlines()]


signal_strength=[]
def check (clock,X,signal_strength):
    cycles=[x for x in range(20,221,40)]
    if clock in cycles:
        signal_strength.append(clock*X)
        
        return print(sum(signal_strength))

clock = 0
X = 1
for line in lines:
    if line[0]=='noop':
        clock += 1
        check(clock,X,signal_strength)
    else:
        clock +=1
        check(clock,X,signal_strength)
        clock += 1
        check(clock,X,signal_strength)
        X += int(line[1])
        


# low 4620
# high 14820