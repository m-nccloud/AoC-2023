import math

example_input = '''...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....'''

lines = example_input.split('\n')

line_index = 0

while line_index < len(lines):
    if lines[line_index].replace('.','') == '':
        lines[line_index] = lines[line_index].replace('.','!')
    line_index += 1
    
line_index = 0
col_index = 0

while col_index < len(lines[0]):
    has_non = False
    line_index = 0
    while line_index < len(lines):
        if lines[line_index][col_index] == '#':
            has_non = True
            break
        line_index += 1
        
    if not has_non:
        line_index = 0
        while line_index < len(lines):
            lines[line_index] = lines[line_index][:col_index]+'!'+lines[line_index][1+col_index:]
            line_index += 1
    col_index += 1

galaxy_locations = [] #[y,x]

line_index = 0
col_index = 0

while line_index < len(lines):
    col_index = 0
    while col_index < len(lines[line_index]):
        if lines[line_index][col_index] == '#':
            galaxy_locations.append([line_index, col_index])
        col_index += 1
    line_index += 1

def dist(gA, gB, dbg = False):
    dX = abs(gA[1] - gB[1])
    dY = abs(gA[0] - gB[0])
    
    xDir = 1 if gA[1] - gB[1] < 0 else -1
    yDir = 1 if gA[0] - gB[0] < 0 else -1
    
    if dX == 0:
        xDir = 0
    if dY == 0:
        yDir = 0
    
    curLoc = [gA[0],gA[1]]
    
    path = []
    
    
    while curLoc[0] != gB[0] or curLoc[1] != gB[1]:
        if curLoc[0] != gB[0]:
            curLoc[0] += yDir
            path.append(lines[curLoc[0]][curLoc[1]])
        
        if curLoc[1] != gB[1]:
            curLoc[1] += xDir
            path.append(lines[curLoc[0]][curLoc[1]])

    steps = 0
    in_a_row = 0
    exclaim_cost = 100
    for itter in range(len(path)):
        if path[itter] == '!':
            in_a_row += 1
        else:
            if in_a_row > 0:
                if in_a_row == 1:
                    steps += exclaim_cost
                else:
                    steps += (exclaim_cost * in_a_row) - exclaim_cost + 1 #this math took me a while to figure out
            steps += 1
            in_a_row = 0
        
    return steps

calculated_pairs = {}

galaxy_outter_index = 0
galaxy_inner_index = 0

total_d = 0
while galaxy_outter_index < len(galaxy_locations):
    galaxy_inner_index = 0 
    if galaxy_outter_index not in calculated_pairs:
        calculated_pairs[galaxy_outter_index] = []
        
    while galaxy_inner_index < len (galaxy_locations):
        if galaxy_inner_index not in calculated_pairs:
            calculated_pairs[galaxy_inner_index] = []
        
        if galaxy_outter_index != galaxy_inner_index:
            if galaxy_inner_index not in calculated_pairs[galaxy_outter_index]:
                total_d += dist(galaxy_locations[galaxy_outter_index], galaxy_locations[galaxy_inner_index])
                calculated_pairs[galaxy_inner_index].append(galaxy_outter_index)
                calculated_pairs[galaxy_outter_index].append(galaxy_inner_index)
                
        galaxy_inner_index += 1
                
    galaxy_outter_index += 1
    
print(total_d)
