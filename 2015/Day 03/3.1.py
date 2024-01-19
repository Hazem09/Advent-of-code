with open ("2015\input_day3.txt") as f:
    directions = f.readlines()

visited = [[0,0]]
santa_coordinates = [0,0]
new_cord= [0,0]

for direction in directions[0]:
    if direction == '^':
        santa_coordinates = [santa_coordinates[0],santa_coordinates[1]+1]

    elif direction == 'v':
        santa_coordinates = [santa_coordinates[0],santa_coordinates[1]-1]
    
    elif direction == '<':
        santa_coordinates = [santa_coordinates[0]-1,santa_coordinates[1]]
    
    elif direction == '>':
        santa_coordinates = [santa_coordinates[0]+1,santa_coordinates[1]]

    if santa_coordinates not in visited:
        visited.append(santa_coordinates)

print(len(visited))


