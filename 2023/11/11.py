import pyperclip
import sys
import math
import string
import re

endsum = 0

galaxies = {}

emptyrows= []
emptycols = None

grid = []
galaxycount = 1

maxX = None
maxY = None

file = sys.argv[1]
if '.txt' not in file:
    file += '.txt'
    
with open(file) as f:
    endsum = 0
    for i, line in enumerate(f.readlines()):
        maxX = i
        line = line.strip().lower()
        if(line == ""):
            continue
        if emptycols == None: #second part fillup cols only once
            emptycols = [i for i in range(0, len(line))]

        grid.append(line)
        maxY = len(line)
        if line.count('.') == maxY:
            emptyrows.append(i)
        else:
            for j,char in enumerate(line):
                if char != '#':
                    continue
                galaxies[galaxycount] = (i,j)
                galaxycount += 1
                
                if j in emptycols:
                    emptycols.remove(j)

for galaxy in galaxies:
    for galaxy2 in galaxies:
        if galaxy2 <= galaxy:
            continue
        (x1, y1) =galaxies[galaxy]
        (x2, y2) = galaxies[galaxy2]
        dist = abs(y2- y1) + abs(x2- x1)
        # some rows may count double
        for x in range(min(x1,x2), max(x1,x2) +1):
            if x in emptyrows:
                dist += 1000000 -1
        for y in range(min(y1, y2), max(y1,y2) +1):
            if y in emptycols:
                dist += 1000000 -1
        #print(galaxy, galaxy2, dist)
        endsum += dist
        
print(endsum)
pyperclip.copy(endsum)