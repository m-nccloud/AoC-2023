example_input = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''

lines = example_input.split('\n')

game_id = 1

loaded_bag = {
    'red':12,
    'green':13,
    'blue':14,
}

potential_ids = []

while game_id <= len(example_input.split('\n')):#does assume its in order
    series = example_input.split('\n')[game_id-1].split(':')[1].split(';')
    
    max_cubes = {k:0 for k in loaded_bag}
    
    for game_round in series:
        round_pulls = game_round.split(',')
        for pull in round_pulls:
            cubes = pull.strip().split()
            if max_cubes[cubes[1]] < int(cubes[0]):
                max_cubes[cubes[1]] = int(cubes[0])
            
    if all(max_cubes.get(key) <= loaded_bag.get(key) for key in loaded_bag):
        potential_ids.append(game_id)
        
    game_id += 1
    
print(sum(potential_ids))
