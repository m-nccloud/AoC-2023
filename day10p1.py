pipe_types = {
    '|':[[0,1],[0,-1]],
    '-':[[1,0],[-1,0]],
    'L':[[0,-1],[1,0]],
    'J':[[0,-1],[-1,0]],
    '7':[[0,1],[-1,0]],
    'F':[[0,1],[1,0]],
    '.':[],
}


example_input = '''.....
.S-7.
.|.|.
.L-J.
.....'''

lines = example_input.split('\n')

starting_point = [-1,-1]

visited = []

replacement = ''

line_index = 0
for line in lines:
    visited.append([])
    for i in line:
        visited[-1].append(-1)
        
    if 'S' in line:
        starting_point[0] = line_index # y
        starting_point[1] = line.index('S') #x

        s_possible_connections = []
        #pipe_dir[0] = x
        #pipe_dir[1] = y
        if line_index > 0:
            #check prev
            if any([x[1] == 1 for x in pipe_types[lines[line_index-1][starting_point[1]]]]):
                s_possible_connections.append([0,-1])
        if line_index < len(lines):
            #check next
            if any([x[1] == -1 for x in pipe_types[lines[line_index+1][starting_point[1]]]]):
                s_possible_connections.append([0, 1])
        if starting_point[1] > 0:
            #check left
            if any([x[0] == 1 for x in pipe_types[lines[line_index][starting_point[1]-1]]]):
                s_possible_connections.append([-1,0])
        if starting_point[1] < len(lines[line_index]):
            #check right
            if any([x[0] == -1 for x in pipe_types[lines[line_index][starting_point[1]+1]]]):
                s_possible_connections.append([1,0])
                
        for key in pipe_types:#i do assume that there is no possible of dead end pipes being connected... 
            replacement = key
            all_found = True
            for spc in s_possible_connections:
                if not spc in pipe_types[key]:
                    all_found = False
                    break
            if all_found:
                break
    line_index += 1
    
lines[starting_point[0]] = lines[starting_point[0]].replace('S',replacement)


squares_to_visit = [[0,starting_point]]

farthest = 0

while len(squares_to_visit) > 0:
    path_step = squares_to_visit[0][0]
    _y = squares_to_visit[0][1][0]
    _x = squares_to_visit[0][1][1]
    
    if path_step > farthest:
        farthest = path_step
    
    visited[_y][_x] = path_step
    
    pipe_opportunities = pipe_types[lines[_y][_x]]
    
    for pipe_dir in pipe_opportunities:
        n_x = pipe_dir[0]+_x
        n_y = pipe_dir[1]+_y
        if n_y >= 0 and n_y < len(visited):
            if n_x >= 0 and n_x < len(visited[_y]):
                if len(pipe_types[lines[n_y][n_x]]) > 0 and visited[n_y][n_x] == -1:
                    squares_to_visit.append([(path_step+1), [n_y,n_x]])
    
    squares_to_visit.pop(0)

print(farthest)
