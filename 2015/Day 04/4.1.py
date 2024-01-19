from hashlib import md5

continue_1 = True
num = 0

while continue_1:
    string ='yzbqklnj'+str(num)  
    result  = md5(string.encode())

    if result.hexdigest()[:6] == '000000':
        continue_1 = False
    else:
        num += 1    
        print(num)

print(result.hexdigest()[:5])
print(num)