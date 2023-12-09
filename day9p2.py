example_input = '''0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45'''

lines = example_input.split('\n')

extrapolated_sum = 0
for line in lines:
    line_nums = line.split()
    
    diffs = [[int(x) for x in line_nums]]
    
    while not all([x == 0 for x in diffs[-1]]):
        diffs.append([])
        for i in range(len(diffs[-2]) - 1):
            diffs[-1].append(diffs[-2][i+1] - diffs[-2][i])
    
    for i in range(len(diffs) - 1):
        current_line = (len(diffs) - i - 2)
        diffs[current_line].insert(0,(diffs[current_line][0]-diffs[current_line+1][0]))
    
    extrapolated_sum += diffs[0][0]
    
print(extrapolated_sum)
