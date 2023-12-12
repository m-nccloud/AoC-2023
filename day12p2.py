#this brute force method has not finished running on my PC for the real input... :/
#documenting this: run time start 1:15:00 AM EST 

example_input = '''???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1'''

lines = example_input.split('\n')

sum_arrangements = 0
_c_line = 0
_t_line = len(lines)
for line in lines: #. or # numbers = damaged
    _c_line += 1
    print(_c_line,'/',_t_line)
    line_part = line.split(' ')
    short_numbers = [int(x) for x in line_part[1].split(',')]
    numbers = []
    for i in range(5):
        numbers.extend(short_numbers)
        
    line_long = (line_part[0]+'?') * 4 + line_part[0]
    potential_groups = [x for x in line_long.split('.') if len(x) > 0]


    potential_pieces = ['.','#']
    indexes = []
    c_index = 0
    while c_index < len(line_long):
        if line_long[c_index] == '?':
            indexes.append([c_index, 0])
        c_index += 1
        
    _c_matches = 0
    
    #_c_attempts = 0
    #_max = 2**len(indexes)
    while True:
        #if _c_attempts % 100000 == 0:
        #    print(_c_line,'/',_t_line,'-',_c_attempts,_max)
        temp_combined = line_long
        
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
        
        #_c_attempts += 1
        
    sum_arrangements += _c_matches
    print(_c_matches)
                 
print(sum_arrangements)   
    
    
