with open ("input_day8.txt") as f:
	lines = []
	for line in f:
		lines.append([int(elem) for elem in line.rstrip()])

rows_len = len(lines)
col_len = len(lines[0])

def visible(row,col) -> bool:
    tree = lines[row][col]

    for i in range(row-1,-1,-1):
        if lines[i][col] >= tree:
            break
    else:
            return True

    for i in range(row+1,rows_len):
        if lines[i][col] >= tree:
            break
    else:
            return True

    for t in lines[row][col+1:]:
        if t >= tree:
            break
    else:
            return True

    for t in reversed(lines[row][:col]):
        if t >= tree:
            break
    else:
            return True

    return False

visible_t= 0

for row in range(1,rows_len-1):
    for col in range(1,col_len-1):
        if visible(row,col):
            visible_t += 1
visible_t += rows_len * 2 + col_len * 2 - 4

print(visible_t)



#too high 7096
#right answer 1733 