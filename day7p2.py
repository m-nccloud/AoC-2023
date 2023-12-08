cards = ['J','2','3','4','5','6','7','8','9','T','Q','K','A']
card_scores = {cards[index]:index+1 for index in range(len(cards))}

card_stature_cache = {}

def stature_calculator(inp):
    if inp in card_stature_cache:
        return card_stature_cache[inp], True
        
    card_count = {}
    for c in inp:
        if not c in card_count:
            card_count[c] = 0
        card_count[c] += 1
        
    stature = 0
    
    if len(card_count) == 1:#5 of a kind
        stature = 6
    elif len(card_count) == 2:
        if any([card_count[c] == 4 for c in card_count]):# 4 of a kind
            stature = 5
        elif any([card_count[c] == 3 for c in card_count]):# full house
            stature = 4
    elif len(card_count) == 3:
        if any([card_count[c] == 3 for c in card_count]):# three of a kind
            stature = 3
        else:
            stature = 2 #two pair
    elif len(card_count) == 4:
        stature = 1 #one pair
    
    if not 'J' in card_count:#dont save prematurely for J
        card_stature_cache[inp] = stature
    
    return stature, False

def deck_stature(inp):
    stature, was_cached = stature_calculator(inp)
    
    if was_cached:
        return stature
        
    if 'J' in inp:
        j_indicies = [i for i in range(len(inp)) if inp[i] == 'J']
        j_replace = [1 for _ in range(len(j_indicies))]
        
        while True:#brute force time
            temp_deck = inp
            for index in range(len(j_indicies)):
                temp_deck = temp_deck[:j_indicies[index]] + cards[j_replace[index]] + temp_deck[j_indicies[index] + 1:]
            n_stature, _ = stature_calculator(temp_deck)
            if stature < n_stature:
                stature = n_stature
            
            if all([rep == len(cards) - 1 for rep in j_replace]):
                break
            else:
                to_inc = [0]
                while len(to_inc) > 0:
                    j_replace[to_inc[0]] += 1
                    if j_replace[to_inc[0]] == len(cards):
                        if to_inc[0] < len(j_replace):
                            j_replace[to_inc[0]] = 1
                            if to_inc[0] + 1 < len(j_replace):
                                to_inc.append(to_inc[0] + 1)
                    to_inc.pop(0)
            

    card_stature_cache[inp] = stature
    
    return stature

def compare_decks(deck_a, deck_b):
    diff = deck_stature(deck_b) - deck_stature(deck_a)
    if diff == 0:
        for card_index in range(len(deck_a)):
            if card_scores[deck_a[card_index]] < card_scores[deck_b[card_index]]:
                diff = 1
                break
            if card_scores[deck_a[card_index]] > card_scores[deck_b[card_index]]:
                diff = -1
                break
    return diff
    
example_input = '''32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483''' 

deck_bid = []

for line in example_input.split('\n'):
    deck_bid.append([])
    deck_bid[-1].append(line.split()[0])
    deck_bid[-1].append(int(line.split()[1]))

index_outter = 0
while index_outter < len(deck_bid):
    index_inner = index_outter
    while index_inner < len(deck_bid):
        result = compare_decks(deck_bid[index_outter][0], deck_bid[index_inner][0])
        if result > 0:
            tmp = deck_bid[index_outter]
            deck_bid[index_outter] = deck_bid[index_inner]
            deck_bid[index_inner] = tmp
            index_outter -= 1
            break
        index_inner += 1
    index_outter += 1
    if index_outter < 0:
        index_outter = 0

print(sum([deck_bid[i][1]*(len(deck_bid)-i) for i in range(len(deck_bid))]))
