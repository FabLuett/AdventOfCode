import pyperclip
import sys
import math
import string
import re

endsum = 0

file = sys.argv[1]
if '.txt' not in file:
    file += '.txt'
    
mappings = {}
seeds = []
ingredients = []

currentMap = None
currentRight = None
    
with open(file) as f:
    for line in f.readlines():
        line = line.strip().lower()
        if(line == ""):
            currentMap =None
            continue
            
        if not currentMap == None:
            parts = line.split (" ")
            dest = int (parts[0])
            source = int (parts[1])
            steps = int (parts[2])
            mappings[currentMap][dest] = (source, steps)
            
        splitted = line.split(": ")
        if( len(splitted) > 1): 
            for seed in splitted[1].split (" "):
                seeds.append(int(seed))
        
        if line.find("map") > 0:
            mapname = line.split(" ")
            ingridients = mapname[0].split("-")
            currentMap = ingridients[2]
            currentRight = ingridients[0]
            ingredients.append (currentMap)
            mappings[currentMap] = {}           
        

minVal = None

i = 1
while True:
    endsum = i
    breakWhile = False
    for ing in reversed(ingredients):
        for val in mappings[ing]:
            tpl = mappings[ing][val]
            if endsum >= val and endsum <= val + tpl[1] -1:
                endsum = tpl[0] + (endsum - val)
                break
        # else endsum stays the same
    # check if seed (endsum) is present
    for i in range(0, len(seeds), 2):
        if endsum >= seeds[i] and endsum <= seeds[i] + seeds[i+1]:
            endsum = i
            breakWhile = True
            break
    i += 1
    if breakWhile:
        break


print(endsum)
pyperclip.copy(endsum)