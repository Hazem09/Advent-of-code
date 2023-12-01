
import string

with open ("2022\input_day3.txt") as f:
    lines = f.readlines()

alphabets = list(string.ascii_letters) 
sum = 0

for line in lines:
    half_line = len(line)//2
    first_half = line[half_line:]
    second_half = line[:half_line]
    inter = set(first_half).intersection(second_half)
    inter = list(inter)
    sum += int(alphabets.index(inter[0])+1)


print(sum)
