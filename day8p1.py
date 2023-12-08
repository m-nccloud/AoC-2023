example_input = '''LLR
AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)'''

lines = example_input.split('\n')

dirs = lines[0]

dir_map = {}

index_i = 1

while index_i < len(lines):
    line_split = lines[index_i].split('=')
    dir_map[line_split[0].strip()] = [line_split[1].replace('(','').replace(')','').split(',')[0].strip() , line_split[1].replace('(','').replace(')','').split(',')[1].strip()]
    
    index_i += 1
    
c_step = "AAA"
steps_solved = 0

while c_step != 'ZZZ':
    steps_capped = steps_solved % len(dirs)
    _dir = dirs[steps_capped]
    
    c_step = dir_map[c_step][0] if _dir == 'L' else dir_map[c_step][1]
    
    steps_solved += 1

    
print(steps_solved)
