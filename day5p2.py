def remapper(rules, inp):
    for rule in rules:
        if rule[1] <= inp and inp < rule[1]+rule[2]:
            return rule[0] + (inp - rule[1])
    return inp

seeds_sets = [[79,14],[55,13]]


seed_to_soilmap = '''50 98 2
52 50 48'''

seed_to_soil_rules = [[int(x) for x in line.split()] for line in seed_to_soilmap.split('\n')]

soil_to_fertilizermap='''0 15 37
37 52 2
39 0 15'''

soil_to_fertilizer_rules = [[int(x) for x in line.split()] for line in soil_to_fertilizermap.split('\n')]

fertilizer_to_watermap='''49 53 8
0 11 42
42 0 7
57 7 4'''

fertilizer_to_water_rules = [[int(x) for x in line.split()] for line in fertilizer_to_watermap.split('\n')]

water_to_lightmap='''88 18 7
18 25 70'''

water_to_light_rules = [[int(x) for x in line.split()] for line in water_to_lightmap.split('\n')]

light_to_temperaturemap='''45 77 23
81 45 19
68 64 13'''

light_to_temperature_rules = [[int(x) for x in line.split()] for line in light_to_temperaturemap.split('\n')]

temperature_to_humiditymap='''0 69 1
1 0 69''' #nice

temperature_to_humidity_rules = [[int(x) for x in line.split()] for line in temperature_to_humiditymap.split('\n')]

humidity_to_locationmap='''60 56 37
56 93 4'''

humidity_to_location_rules = [[int(x) for x in line.split()] for line in humidity_to_locationmap.split('\n')]

lln=-1

for pairs in seeds_sets:
    for i in range(pairs[1]):
        seed = pairs[0] + i
        sts = remapper(seed_to_soil_rules, seed)
        stf = remapper(soil_to_fertilizer_rules, sts)
        ftw = remapper(fertilizer_to_water_rules, stf)
        wtl = remapper(water_to_light_rules, ftw)
        ltt = remapper(light_to_temperature_rules, wtl)
        tth = remapper(temperature_to_humidity_rules, ltt)
        htl = remapper(humidity_to_location_rules, tth)
        if lln == -1 or lln > htl:
            lln = htl

print(lln)
