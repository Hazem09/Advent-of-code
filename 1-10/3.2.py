import string

with open ("2022\input_day3.txt") as f:
    lines = f.readlines()

alphabets = list(string.ascii_letters) 
sum = 0

for i in range(0,len(lines),3):
    first_line = lines[i].strip()
    second_line = lines[i+1].strip()
    third_line = lines[i+2].strip()
    inter = set(first_line).intersection(second_line).intersection(third_line)
    inter = list(inter)
    sum += int(alphabets.index(inter[0]) + 1)


print(sum)    