import pyperclip
import sys
import math
import string
import re

endsum = 0

intervals = [(0,1)]

file = sys.argv[1]
if '.txt' not in file:
    file += '.txt'
    
with open(file) as f:
    endsum = 0
    x = 0
    y = 1
    for line in f.readlines():
        line = line.strip()
        if(line == ""):
            break
            
        splitted = line.split (" ")
        direction = splitted[0]
        steps = int(splitted[1])
        color = splitted[2]
        if direction == "U":
            x -= steps
        elif direction == "D":
            x += steps
        elif direction == "R":
            y += steps
        elif direction == "L":
            y -= steps
        intervals.append((x, y))

xvals = [k[0] for k in intervals]
yvals = [k[1] for k in intervals]
xoffset = min(xvals)
yoffset = min(yvals)
maxx = max(xvals) - min (xvals)
maxy = max(yvals) - min(yvals)

field = []
for x in range (maxx +1):
    field.append([])
    for y in range(maxy +1):
        field[x].append(".")
        
field[0][0] = '#'        
lastInterval = intervals[0]        
for interval in intervals[1:]:
    startx = lastInterval[0]
    starty = lastInterval[1]
    steps = max(abs(lastInterval[1] - interval[1]), abs(lastInterval[0] - interval[0]))     
    
    for i in range(steps):
        # up down
        if interval[0] < lastInterval[0]:
            #print("case 1", interval, lastInterval, i)
            field[interval[0] + i][lastInterval[1]-1] = '#'
        elif lastInterval[0] < interval[0]:
            #print("Case 2", interval, lastInterval)
            field[lastInterval[0] + i+1][interval[1]-1] = '#'
        # left right
        elif interval[1] < lastInterval[1]:
            #print("Case 3")
            field[lastInterval[0]][interval[1] + i-1] = '#'
        else:
            #print("Case 4")
            field[lastInterval[0]][lastInterval[1] + i] = '#'

    print("After interval", interval, lastInterval)
    for i in range(len(field)):
        print(field[i])
    lastInterval = interval
    
endsum = 0    
for i in range(len(field)):
    line = field[i]
    idx = line.index ("#")
    idx2 = len(line) - line[::-1].index("#")
    #field[i] = line[:idx] + ["#" for i in range(idx2-idx)] + line[idx2:]
    endsum += idx2-idx#sum ( [1 if char == "#" else 0 for char in field[i]])
    #print(field[i])

print(endsum)
#print(intervals)
pyperclip.copy(endsum)