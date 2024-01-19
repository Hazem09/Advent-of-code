with open ("input_day5.txt") as f:
    strings =[x.strip('\n') for x in f ]


def pair(s:str) -> bool:
    s_len = len (s)
    
    for i in range(1,s_len):
        pair_1 = s[i-1]+s[i] 
        for j in range(i+2,s_len):
            pair_2 = s[j-1] + s[j]
            if pair_1 == pair_2:
                return True
    return False

def double_char(s:str) -> bool:
    s_len = len(s)
    for i in range(1,s_len-1):
        if s[i-1] == s[i+1]:
            return True
    return False


counter = 0
for string in strings:
    if pair(string) and double_char(string):
        counter += 1

print(counter)