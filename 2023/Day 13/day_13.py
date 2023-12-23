# The bug that took too long to realize is how i read my input, the use of readlines(),
# strips the empty line so there's no way to know where the new pattern starts, 
# also having the script inside the open context manager yielded a wrong result(smaller) ¯\_(ツ)_/¯,
# found this solution in reddit where it uses a while loop to read the file line by line.

def part_1():
    patterns = []
    data = open('2023\Day 13\day_13.txt')
    total = 0

    while True:
        line = data.readline()
        if line == '\n' or line == '':
            found = False
            for i in range(1, len(patterns)):
                ref_range = min(i, len(patterns) - i)
                for j in range(1, ref_range + 1):
                    if patterns[i - j] != patterns[i + j - 1]:
                        break
                else:
                    found = True
                    total += 100 * i
                    break
            if not found:
                for i in range(1, len(patterns[0])):
                    ref_range = min(i, len(patterns[0]) - i)
                    for j in range(1, ref_range + 1):
                        if [patterns[n][i - j] for n in range(len(patterns))] != [patterns[n][i + j - 1] for n in range(len(patterns))]:
                            break
                    else:
                        total += i
            if line == '':
                print(total)
                break
            patterns = []
        else:
            patterns.append(line.strip())
    return print(total)

part_1()
