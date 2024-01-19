with open ("input_day5.txt") as f:
    strings =[x.strip('\n') for x in f ]


def doublechars(s:str) -> bool:
    s_len=len(s)
    for i in range(1,s_len):
        if s[i-1] == s[i]:
            return True
    return False

def vowels(s:str) -> bool:
    total = 0
    for v in "aieou":
        total += s.count(v)
        
    return total >= 3    

def doenst_contain(s:str) -> bool:
    for _ in ['ab','cd','pq','xy']:
        if _ in s:
            return False
    return True

counter = 0
for string in strings:
    if doublechars(string) and vowels(string) and doenst_contain(string):
        counter += 1

print(counter)