cards = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
card_scores = {cards[index]:index+1 for index in range(len(cards))}

def deck_stature(inp):
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
