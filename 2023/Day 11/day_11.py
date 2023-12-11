# I started by expanding the grid first then calculating the distance between stars,
# but it's better to calculate the manhaten distance between stars first then add the
# additional distance due to the empty rows and columns
# for part 1 each empty row and column add 1 to the distance
# for part 2 each empty row and column add 999999 to the distance

with open('2023/Day 11/day_11.txt') as f:
    data = [line.strip() for line in f.readlines()]
    
def day_11(data):
    hight, width = len(data), len(data[0])

    emptyrows, emptycols = [], []

    for i, line in enumerate(data):
        if line == '.'*width:
            emptyrows.append(i)

    for j in range(width):
        if [data[i][j] for i in range(hight)] == ['.']*hight:
            emptycols.append(j)

    stars = []
    for i in range(hight):
        for j in range(width):
            if data[i][j] == '#': stars.append( (i,j) )


    def dist(star1, star2,gap):
        i, j = star1
        k, l = star2
        d = abs(i-k) + abs(j-l)
        for row in emptyrows:
            if i < row < k or k < row < i: d += gap
        for col in emptycols:
            if j < col < l or l < col < j: d += gap

        return d

    sumdist_1,sumdist_2 = 0,0
    for (i,j) in stars:
        for (k,l) in stars:
            if (i,j) < (k,l):
                d_1 = dist((i,j), (k,l),1)
                d_2 = dist((i,j), (k,l),999999)
                sumdist_1 += d_1
                sumdist_2 += d_2
    return print(sumdist_1,sumdist_2)

day_11(data)
