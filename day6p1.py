races = [[7,9],[15,40],[30,200]]

possible_wins = []
for race in races:
    possible_wins.append([])
    for time in range(race[0]):
        _t = time * (race[0] - time)
        if _t > race[1]:
            possible_wins[-1].append(_t)
            
total = 1#assumes at least one possiblity in all races can win
for x in [len(i) for i in possible_wins]:
    total *= x
    
print(total)
