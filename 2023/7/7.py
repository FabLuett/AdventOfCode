import pyperclip
import sys
import math
import string
import re

endsum = 0

#cards = ['A', 'K', 'Q', 'J', 'T'] + [str(x) for x in range(9,1,-1)]
cards = ['A', 'K', 'Q', 'T'] + [str(x) for x in range(9,1,-1)] + ['J']

hands = {}


def value(hand):
    hand = sorted(hand)
    jokers = hand.count('J')
    counts = [hand.count(x) for x in set(cards) if x != 'J']
    max_count = max(counts) + jokers
    if max_count >= 5:
        return 1 #five of a kind
    if max_count >= 4:
        return 2 #four of a kind
    pairs = [x for x in counts if x == 2]
    if max_count >= 3:
        if (jokers == 0 and len(pairs) == 1) or (jokers > 0 and len(pairs) == 2):
            return 3 #fullhouse
        return 4 # three of a kind
    if len(pairs) == 2:
        return 5 #2 pair
    if len(pairs) == 1 or jokers > 0:
        return 6 #one pair
    return 7 #high card

file = sys.argv[1]
if '.txt' not in file:
    file += '.txt'
    
with open(file) as f:
    endsum = 0
    for line in f.readlines():
        line = line.strip()
        if(line == ""):
            continue
        splitted = line.split(" ")
        hands[splitted[0]] = [int(splitted[1]), value(splitted[0])]

for i, hand in enumerate(sorted(hands.keys (), key = lambda x: (hands[x][1], [cards.index(char) for char in x]))):
    endsum += (len(hands) -i) * hands[hand][0]
        
print(endsum)
pyperclip.copy(endsum)