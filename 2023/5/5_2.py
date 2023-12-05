import pyperclip
import sys
import math
import string
import re

endsum = 0

def sortTuple (elem):
    return elem[0]
    
def translate(interval, target, steps):
    return (target[1] + (interval[0] - target[0]), steps)
    
def splitInterval (interval, searchList):
    #print("interval to split", interval, "list: ", searchList)
    source = interval[0]
    steps = interval[1]
    ret = []
    for search in searchList:
        maxbound = search[0] + search[2]
        if source < search[0]:
            # maybe right side is inside the interval?
            if source + steps >= search[0]:
                #print("left but split", search)
                ret.append((source, search[0] - source))
                #print("added", ret)
                for i in splitInterval ( (search[0], steps - (search[0] - source)), searchList):
                    ret.append(i)
                break
        elif source >= search[0] and source < maxbound:
            # source in interval (maybe not all?)
            if source + steps > maxbound:
                #print("right outside", search)
                ret.append (translate(interval, search, maxbound - source))
                for i in splitInterval ( (maxbound, steps - (maxbound - source)), searchList):
                    ret.append (i)
                break
            else:
                #print("complete inside", search)
                ret.append( translate(interval, search, steps))
                break
    if len(ret) == 0:
        ret.append (interval)
    #print("retvalue", ret)
    return list(set(ret))

file = sys.argv[1]
if '.txt' not in file:
    file += '.txt'
    
# map: [(source, dest, steps)]
mappings = {}
seeds = []
ingredients = []

currentMap = None
currentRight = None
    
with open(file) as f:
    for line in f.readlines():
        line = line.strip().lower()
        if(line == ""):
            currentMap = None
            continue
            
        if not currentMap == None:
            parts = line.split (" ")
            dest = int (parts[0])
            source = int (parts[1])
            steps = int (parts[2])
            mappings[currentMap].append((source,dest, steps))
            mappings[currentMap].sort (key = sortTuple)
            
        splitted = line.split(": ")
        if len(splitted) > 1:
            splitted = splitted[1].split (" ")
            for i in range(0, len(splitted), 2):
                seeds.append ((int(splitted[i]), int(splitted[i+1])))
        
        if line.find("map") > 0:
            mapname = line.split(" ")
            ingridients = mapname[0].split("-")
            currentMap = ingridients[2]
            currentRight = ingridients[0]
            ingredients.append (currentMap)
            mappings[currentMap] = []           
        

minVal = None

j = 0


#print("1:", splitInterval((11,4), [(12,20,2), (14,30,1)]))
#print("2:",splitInterval((11,4), [(24,24,4), (234,234,1)]))



current = seeds
current.sort(key = sortTuple)
for ing in ingredients:        
    newcurrent = []
    for interval in current:
        for i in splitInterval (interval, mappings[ing]):
            newcurrent.append(i)
    current = list(set(newcurrent))
    current.sort(key = lambda x: x[0])
    j+= 1
    if j == 12:
        break

endsum = current[0][0]

print(endsum)
pyperclip.copy(endsum)