import pyperclip
import sys
import math
import string
import re

endsum = 0

red = 12
green = 13
blue = 14

file = sys.argv[1]
if '.txt' not in file:
    file += '.txt'
    
with open(file) as f:
    endsum = 0
    for line in f.readlines():
        line = line.strip().lower()
        if(line == ""):
            continue
        
        line = line[5:] #eliminate "game "
        ind = line.find(":")
        gameId = int(line[:ind])
        line = line[ind+2:]
        
        games = line.split(";")
        
        add = True
        dices = {
            "green": 0,
            "blue": 0,
            "red": 0
        }
        
        for game in games:
            for teststr in game.split (","):
                teststr = teststr.strip()
                num = teststr.split(" ")[0].strip()
                color = teststr.split(" ")[1].strip()
                if int(num) > dices[color]:
                   dices[color] = int(num) 
                
        power = 1
        for val in dices:
            power *= dices[val]
        endsum += power
print(endsum)
pyperclip.copy(endsum)