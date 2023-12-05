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
            mappings[currentMap][source] = (dest, steps)
            
        splitted = line.split(": ")
        if( len(splitted) > 1): 
            for seed in splitted[1].split (" "):
                seeds.append(int(seed))
        
        if line.find("map") > 0:
            mapname = line.split(" ")
            ingridients = mapname[0].split("-")
            currentMap = ingridients[0]
            currentRight = ingridients[2]
            ingredients.append (currentMap)
            mappings[currentMap] = {}           
        

minVal = None
for i in range (0, len(seeds), 2):
    for j in range(0, seeds[i+1]):
        val = seeds[i] +j
        for ing in ingredients:
            for key in mappings[ing]:
                tupl = mappings[ing][key]
                
                if val >= key and val <= key + tupl[1]-1:
                    val = tupl[0] + (val - key)
                    break
                
        if minVal == None or val < minVal:
            minVal = val

endsum = minVal
print(endsum)

pyperclip.copy(endsum)