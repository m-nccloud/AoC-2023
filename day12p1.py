example_input = '''???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1'''

lines = example_input.split('\n')

sum_arrangements = 0

for line in lines: #. or # numbers = damaged
    line_part = line.split(' ')
    numbers = [int(x) for x in line_part[1].split(',')]
    potential_groups = [x for x in line_part[0].split('.') if len(x) > 0]


    potential_pieces = ['.','#']
    indexes = []
    c_index = 0
    while c_index < len(line_part[0]):
        if line_part[0][c_index] == '?':
            indexes.append([c_index, 0])
        c_index += 1
        
    _c_matches = 0
    
    while True:
        temp_combined = line_part[0]
        
        for pair in indexes:
            temp_combined = temp_combined[:pair[0]]+(potential_pieces[pair[1]])+temp_combined[pair[0]+1:]
        
        split_test = temp_combined.split(' ')
        numbers_test = []
        for x in split_test:
            for z in x.split('.'):
                if len(z) > 0:
                    numbers_test.append(z)

        numbers_test = [len(x) for x in numbers_test]
        if numbers_test == numbers:
            _c_matches += 1
        
        _t_index = 0
        
        while _t_index < len(indexes):
            if indexes[_t_index][1] == 1:
                indexes[_t_index][1] = 0
                _t_index += 1
            else:
                indexes[_t_index][1] = 1
                break
            
        if all([x[1] == 0 for x in indexes]):
            break
        
    sum_arrangements += _c_matches
    print(_c_matches)
                 
print(sum_arrangements)   
    
    
