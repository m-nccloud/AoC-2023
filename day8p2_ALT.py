### I like this solution better
#   However the input data of the actualy AoC challenge is made cyclical on purpose
#   the resulting answer for "how many steps does it take so that all start nodes are at their end nodes simultaneously" with the AoC input ends up in a 14 digit number
#   good luck getting that in a timely manner

example_input = '''LR
11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)'''

lines = example_input.split('\n')

dirs = lines[0]

dir_map = {}

current_nodes = []

index_i = 1

while index_i < len(lines):
    line_split = lines[index_i].split('=')
    dir_map[line_split[0].strip()] = [line_split[1].replace('(','').replace(')','').split(',')[0].strip() , line_split[1].replace('(','').replace(')','').split(',')[1].strip()]
    if line_split[0].strip()[-1] == 'A':
        current_nodes.append(line_split[0].strip())
    index_i += 1
    
steps_solved = 0

while not all([x[-1] == 'Z' for x in current_nodes]):
    steps_capped = steps_solved % len(dirs)
    _dir = dirs[steps_capped]
    for c_index in range(len(current_nodes)):
        current_nodes[c_index] = dir_map[current_nodes[c_index]][0] if _dir == 'L' else dir_map[current_nodes[c_index]][1]
    steps_solved += 1
    
print(steps_solved)
