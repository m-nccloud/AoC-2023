import re

def remove_non_num(inp):
    return re.sub(r'[^0-9]', '', inp)

example_input = '''two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen'''

num_map = {
    'zero':'0ero',
    'one':'1ne',
    'two':'2wo',
    'three':'3hree',
    'four':'4our',
    'five':'5ive',
    'six':'6ix',
    'seven':'7even',
    'eight':'8ight',
    'nine':'9ine',
}

total = 0

for unprocessed_line in example_input.split():
    line = unprocessed_line
    while True:
        lowest_index = -1
        best_replace = ''
        for entry in num_map:
            try:
                potential_index = line.index(entry)
                if lowest_index == -1 or potential_index < lowest_index:
                    lowest_index = potential_index
                    best_replace = entry
            except:
                pass
        
        if lowest_index >= 0:
            line = line[:lowest_index] + num_map[best_replace] + line[lowest_index+len(best_replace):]
        else:
            break
    
    nums = remove_non_num(line)
    total += int(nums[0])*10 + int(nums[0]) if len(nums) == 1 else int(nums[0])*10 + int(nums[len(nums)-1]) #doesnt account for no numbers in nums ik
    
print(total)
