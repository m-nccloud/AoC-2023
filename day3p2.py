import re

example_input = '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..'''

def get_symbol_set():
    return set(list(re.sub(r'[0-9\.\n]', '', example_input)))
    
def is_a_number(inp):
    return re.sub(r'[^0-9]','',inp) == inp
    
symbols = get_symbol_set()

lines = example_input.split('\n')

gear_ratios = []

for line_index in range(len(lines)):
    for char_index in range(len(lines[line_index])):
        if lines[line_index][char_index] == '*':
            touching_nums = []
            adj_lines = [line_index-1, line_index, line_index+1]
            for adj_line_index in adj_lines:
                if adj_line_index >= 0 and adj_line_index < len(lines):
                    num = ''
                    start_index = -1
                    for adj_char_index in range(len(lines[adj_line_index])):
                        is_num = is_a_number(lines[adj_line_index][adj_char_index])
                        if is_num:
                            if num == '':
                                start_index = adj_char_index
                            num += lines[adj_line_index][adj_char_index]
                        
                        if start_index >= 0 and (not is_num or adj_char_index+1 == len(lines[adj_line_index])):
                            if start_index - 1 <= char_index and start_index+len(num) >= char_index:
                                touching_nums.append(int(num))
                            num = ''
                            start_index = -1
            if len(touching_nums) == 2:
                gear_ratios.append(touching_nums[0] * touching_nums[1])
                
print(sum(gear_ratios))
                        
 

                    
    
    
