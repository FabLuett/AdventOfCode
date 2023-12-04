import pyperclip
import sys
import math
import string
import re

endsum = 0

file = sys.argv[1]
if '.txt' not in file:
    file += '.txt'
    
matches = {}
cardcount = {}
    
with open(file) as f:
    endsum = 0
    for line in f.readlines():
        line = line.strip().lower()
        if(line == ""):
            continue
        
        ind = line.find(":")
        cardnr = int(line[5:ind])
        matches[cardnr] = []
            
        numbers = line[ind+1:].split ("|")
        winningnumbers = numbers[0].strip()
        mynumbers = numbers[1].strip()
        correct = 0
        
        winners = []
        for s in winningnumbers.split (" "):
            if s == "":
                continue
            winners.append(int(s.strip()))
        
        for s in mynumbers.split(" "):
            if s == "":
                continue
            if int(s.strip()) in winners:
                correct += 1
        
        matches[cardnr] = correct
        cardcount[cardnr] = 1
                
        
for card in matches:
    for j in range(cardcount[card]):
        for i in range(matches[card]):

            cardcount[card + i + 1]+= 1

        
for cnt in cardcount:
    endsum += cardcount[cnt]
print(endsum)
pyperclip.copy(endsum)