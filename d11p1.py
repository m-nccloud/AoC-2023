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
        lines.insert(line_index,'.'*len(lines[line_index]))
        line_index += 1
    line_index += 1
    
line_index = 0
col_index = 0

while col_index < len(lines[0]):
    has_non = False
    line_index = 0
    while line_index < len(lines):
        if lines[line_index][col_index] != '.':
            has_non = True
            break
        line_index += 1
        
    if not has_non:
        line_index = 0
        while line_index < len(lines):
            lines[line_index] = lines[line_index][:col_index]+'.'+lines[line_index][col_index:]
            line_index += 1
        col_index += 1
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

def dist(gA, gB):
    dX = abs(gA[1] - gB[1])
    dY = abs(gA[0] - gB[0])
    
    return dX + dY

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
