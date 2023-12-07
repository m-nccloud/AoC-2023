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

part_numbers = []

for line_index in range(len(lines)):
    nums = []
    num = ''
    for char_index in range(len(lines[line_index])):
        is_num = is_a_number(lines[line_index][char_index])
        if is_num:
            if num == '':
                nums.append([char_index])
            num += lines[line_index][char_index]
        if num!='' and (not is_num or char_index >= (len(lines[line_index])-1)):
            nums[-1].append(num)
            num = ''
    
    adj_lines = [line_index-1, line_index, line_index+1]
    
    for pair in nums:
        added = False
        range_coverage = range(0 if pair[0]-1 < 0 else pair[0]-1 , len(lines[line_index]) if pair[0]+len(pair[1])+1 > len(lines[line_index]) else pair[0]+len(pair[1])+1)
        for adj_line_index in adj_lines:
            if added:
                break
            if adj_line_index >= 0 and adj_line_index < len(lines):
                for adj_index in range_coverage:
                    if lines[adj_line_index][adj_index] in symbols:
                        part_numbers.append(int(pair[1]))
                        added = True
                        break

print(sum(part_numbers))
                    
    
    
