import re

def remove_non_num(inp):
    return re.sub(r'[^0-9]', '', inp)

example_input = '''1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet'''

total = 0

for line in example_input.split():
    nums = remove_non_num(line)
    total += int(nums[0])*10 + int(nums[0]) if len(nums) == 1 else int(nums[0])*10 + int(nums[-1]) #doesnt account for no numbers in nums ik
    
print(total)
