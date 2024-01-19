with open ("2015\input_day3.txt") as f:
    directions = f.readlines()

    
santa_coordinates = [0,0]
robot_santa_coordinates = [0,0]
visited = [[0,0]]

for i in range(0,len(directions[0]),2):
    if directions[0][i] == '^':
        santa_coordinates = [santa_coordinates[0],santa_coordinates[1]+1]

    elif directions[0][i] == 'v':
        santa_coordinates = [santa_coordinates[0],santa_coordinates[1]-1]
    
    elif directions[0][i] == '<':
        santa_coordinates = [santa_coordinates[0]-1,santa_coordinates[1]]
    
    elif directions[0][i] == '>':
        santa_coordinates = [santa_coordinates[0]+1,santa_coordinates[1]]

    if santa_coordinates not in visited:
        visited.append(santa_coordinates)

    if directions[0][i+1] == '^':
        robot_santa_coordinates = [robot_santa_coordinates[0],robot_santa_coordinates[1]+1]

    elif directions[0][i+1] == 'v':
        robot_santa_coordinates = [robot_santa_coordinates[0],robot_santa_coordinates[1]-1]
    
    elif directions[0][i+1] == '<':
        robot_santa_coordinates = [robot_santa_coordinates[0]-1,robot_santa_coordinates[1]]
    
    elif directions[0][i+1] == '>':
        robot_santa_coordinates = [robot_santa_coordinates[0]+1,robot_santa_coordinates[1]]

    if robot_santa_coordinates not in visited:
        visited.append(robot_santa_coordinates)

print(len(visited))