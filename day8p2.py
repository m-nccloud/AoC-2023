### My original solution, which is more correct, relied on brute forcing the problem
#   the only reason least common multiple works is because (probably) Advent of Coding wanted it this way
#   if the data wasn't setup to be cyclical then this solution breaks
#   a solution that doesn't break with data that isnt made to be cyclical https://github.com/savvamadar/AoC-2023/blob/main/day8p2_ALT.py

example_input = '''LR
11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)'''

def gcd(x, y):
    big = x
    small = y
    
    if small > big:
        big = y
        small = x
    
    mod_result = big % small
    if mod_result == 0:
        return small
    else:
        return gcd(small, mod_result)

def lcm(a,b):
    return a*b // gcd(a,b)

lines = example_input.split('\n')

dirs = lines[0]

dir_map = {}

current_nodes = []
node_steps = []

index_i = 1

while index_i < len(lines):
    line_split = lines[index_i].split('=')
    dir_map[line_split[0].strip()] = [line_split[1].replace('(','').replace(')','').split(',')[0].strip() , line_split[1].replace('(','').replace(')','').split(',')[1].strip()]
    if line_split[0].strip()[-1] == 'A':
        current_nodes.append(line_split[0].strip())
        node_steps.append(-1)
    index_i += 1

steps_solved = 0

while any([x == -1 for x in node_steps]):
    steps_capped = steps_solved % len(dirs)
    _dir = dirs[steps_capped]
    for c_index in range(len(current_nodes)):
        if current_nodes[c_index][-1] != 'Z':
            current_nodes[c_index] = dir_map[current_nodes[c_index]][0] if _dir == 'L' else dir_map[current_nodes[c_index]][1]
        elif node_steps[c_index] == -1:
            node_steps[c_index] = steps_solved
    steps_solved += 1

while len(node_steps) > 1:
    a = node_steps.pop(0)
    b = node_steps.pop(0)
    r = lcm(a,b)
    node_steps.insert(0,r)

print(node_steps[0])

