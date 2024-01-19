with open ("2015\input_day2.txt") as f:
    lines = f.readlines()

ribbon = 0
for line in lines:
    dimensions = line.split('x')
    dimensions = [int(num) for num in dimensions]
    dimensions.sort()
    ribbon += dimensions[0]*2 + dimensions[1]*2 + dimensions[0] * dimensions[1] * dimensions[2]


print(ribbon)
