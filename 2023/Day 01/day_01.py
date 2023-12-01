with open('Day 01\day_1.txt') as f:
    data = f.readlines()


def part_1(data):
    total = 0
    for line in data:
        digits = [int(char) for char in line if char.isdigit()]
        if len(digits) >= 2:
            total += digits[0]*10 + digits[-1]
        else:
            total += digits[0]*10 + digits[0]        
    
    print(total)

part_1(data)       

def part_2(data):
    DIGITS = "one two three four five six seven eight nine"
    def extract(line):
        for index, word in enumerate(DIGITS.split(), 1):
            line = line.replace(word, f"{word}{index}{word}")
        return int([d for d in line if d.isdigit()][:1][0]+[d for d in line if d.isdigit()][-1:][0])
    print(sum(extract(line) for line in data))  

part_2(data)
