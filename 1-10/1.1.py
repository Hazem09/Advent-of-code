with open("2022\input_day1.txt") as f:
    lines = f.readlines()



calories = []
calorie_count = 0
for line in lines:

    if line.strip():
        calorie_count = calorie_count + int(line)
    else:
        calories.append(calorie_count)
        calorie_count = 0
print(max(calories)) 


calories.sort()
top_3 = 0
print(calories)
for i in range(-3,0):
    top_3 = top_3 + calories[i]

print(top_3)    


