with open('2023/Day 09/day_09.txt') as f:
    data = [line.strip() for line in f.readlines()]


def diff(list):
    return [list[i+1] - list[i] for i in range(len(list)-1)]

def reverse_add(dict):
    dict_len = len(dict)
    
    for i in range(dict_len, 1,-1):
        dict[i-1].append(dict[i][-1]+dict[i-1][-1])

    return dict

def reverse_sub(dict):
    dict_len = len(dict)
    
    for i in range(dict_len, 1,-1):
        dict[i-1].insert(0,dict[i-1][0]-dict[i][0])
        
    return dict

def day_08(data):
    first_element, last_element = [], []
    for line in data:
        line = [int(i) for i in line.split()]
        i = 0
        dict_1 = {}
        for i in range(1, len(line) + 1):
            dict_1[i] = list(map(int, line))
            line = diff(dict_1[i])
            if all(element == 0 for element in line):
                break

        last_element.append(reverse_add(dict_1)[1][-1])
        first_element.append(reverse_sub(dict_1)[1][0])

    return print(sum(last_element), sum(first_element))


day_08(data)