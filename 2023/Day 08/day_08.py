with open('2023/Day 08/day_08.txt') as f:
    data = [line.strip() for line in f.readlines() ]
    
instructions = [0 if i == "L" else 1 for i in data[0]]
nodes = {}

def part_1(data):
    for line in data[2:]:
        node, neighbours = line.split(" = ", 1)
        neighbours = neighbours.split(", ")
        nodes[node] = (neighbours[0][1:], neighbours[1][:-1])
    curr_node = "AAA"
    steps = 0
    while (curr_node != "ZZZ"):
        for i in instructions:
            if curr_node == "ZZZ":
                break
            steps += 1
            curr_node = nodes[curr_node][i]

    print(steps)

part_1(data)