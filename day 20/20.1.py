from collections import deque

with open('input_day20.txt') as f:
    numbers =[int(line.strip('\n')) for line in f.readlines()]

mixed_numbers = deque(numbers.copy())

index_list = deque([i for i in range(len(numbers))])


for k,j in enumerate(numbers):
    index= index_list.index(k)

    del mixed_numbers[index]
    del index_list[index]

    mixed_numbers.rotate(j*-1)
    index_list.rotate(j*-1)

    mixed_numbers.insert(index,j)
    index_list.insert(index,k)

print(mixed_numbers.index(0))

value_1 = mixed_numbers[(mixed_numbers.index(0) + 1000) % len(numbers)]
value_2 = mixed_numbers[(mixed_numbers.index(0) + 2000) % len(numbers)]
value_3 = mixed_numbers[(mixed_numbers.index(0) + 3000) % len(numbers)]

print(value_1 + value_2 + value_3)
#wrong -10357
#wrong -7517
#right 27726

#part2

