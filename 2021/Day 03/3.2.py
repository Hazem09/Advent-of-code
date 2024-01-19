from copy import copy

with open ('input_day3.txt') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]


oxygen = copy(lines)
for i in range(len(lines[0])):
    if len(oxygen) == 1:
        break
    all_entries_at_pos = [entry[i] for entry in oxygen]
    common_bit = '1' if all_entries_at_pos.count('1') >= len(oxygen)/2 \
                 else '0'
    oxygen = [entry for entry in oxygen 
                                    if entry[i]==common_bit]
oxygen_rating = int(oxygen[0], base=2)
print('oxygen', oxygen[0], oxygen_rating)


co2= copy(lines)

for i in range(len(lines[0])):
    if len(co2) == 1:
        break
    all_entries_at_pos = [entry[i] for entry in co2]
    least_common_bit = '0' if all_entries_at_pos.count('1') >= len(co2)/2 \
                       else '1'
    co2 = [entry for entry in co2
                                 if entry[i]==least_common_bit]
co2_rating = int(co2[0], base=2)
print('co2', co2[0], co2_rating)

print(oxygen_rating*co2_rating)