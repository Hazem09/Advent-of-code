with open('input_day7.txt') as file:
    commands = file.read().split('\n')

lines = [x.split(' ') for x in commands]
dirs = {}
current_dirS = []
for l in lines:
    if l[0] == '$' and l[1] == 'cd':
        if l[2] == '/':
            current_dirS = ['//']
            dirs['//'] = 0
        elif l[2] == '..':
            current_dirS.pop()
        else:
            current_dir = '/'.join(current_dirS) + '/' + l[2]
            current_dirS.append(current_dir)
            if not dirs.get(current_dir):
                dirs[current_dir] = 0
    elif l[0].isdigit():
        for dir in current_dirS:
            dirs[dir] += int(l[0])

files_sum = [x for x in dirs.values() if x<=100000]

print(sum(files_sum))
#print(dirs)

space = dirs['//'] - 40000000

can_be_deleted = [x for x in dirs.values() if x > space]
print(min(can_be_deleted))

#print(lines)


#too high 2735087
#right 1543140