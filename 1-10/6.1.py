with open ("input_day6.txt") as f:
    code = f.readline()

def uniqueCharacters(str):
     

    for i in range(len(str)):
        for j in range(i + 1,len(str)):
            if(str[i] == str[j]):
                return False
 
    return True

i = 0
#part 1
while not uniqueCharacters(code[i:i+4]) and i <len(code):
    i +=1
else:
    print(i+4)

#part2
while not uniqueCharacters(code[i:i+14]) and i <len(code):
    i +=1
else:
    print(i+14)    

