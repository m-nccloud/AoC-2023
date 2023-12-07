race = [71530,940200]


possible_wins = 0

for time in range(race[0]): #cpu goes brrr
    _t = time * (race[0] - time)
    if _t > race[1]:
        possible_wins += 1
            
print(possible_wins)
