with open ("input_day8.txt") as f:
	lines = []
	for line in f:
		lines.append([int(elem) for elem in line.rstrip()])

rows_len = len(lines)
col_len = len(lines[0])

def score(row,col) -> int:
    tree = lines[row][col]
    up, down, right, left = [0,0,0,0]

    for i in range(row-1,-1,-1):
        up += 1
        if lines[i][col] >= tree:
            break


    for i in range(row+1,rows_len):
        down += 1
        if lines[i][col] >= tree:
            break


    for t in lines[row][col+1:]:
        right += 1
        if t >= tree:
            break


    for t in reversed(lines[row][:col]):
        left += 1
        if t >= tree:
            break


    return up*down*right*left

max=0

for row in range(1,rows_len-1):
    for col in range(1,col_len-1):
        score_1 = score(row,col)
        if score_1 > max:
            max = score_1

print(max)



#too high 7096
#right answer 1733 