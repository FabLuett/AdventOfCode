import pyperclip
import sys
import math
import string
import re

endsum = 0

intervals = [(0,0)]

file = sys.argv[1]
if '.txt' not in file:
    file += '.txt'
    
with open(file) as f:
    endsum = 0
    x = 0
    y = 0
    for line in f.readlines():
        line = line.strip()
        if(line == ""):
            continue
            
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
    steps = max(lastInterval[1] - interval[1], lastInterval[0] - interval[0])
    # shift
    if interval[0] < 0:
        # downwards
        for i in range(-1*interval[0]):
            field.insert(0, ["." for l in range(len(field[0]))])
        steps = abs(lastInterval[0] - interval[0])
    if interval[1] < 0:
        # right wards
        steps = abs(lastInterval[1] - interval[1])
        for i in range(-1*interval[1]):
            for j in range (len(field)):
                field[j].insert(0, ".")
        
    # right and down
    if lastInterval[0] < interval[0]:
        for y in range(steps):
            field[y+1][lastInterval[1]] = "#"
    if lastInterval[1] < interval[1]:
        for x in range(lastInterval[1], interval[1]):
            field[lastInterval[0]][x+1] = "#"
    # left and up
    if interval[0] < lastInterval[0]:
        for y in range(steps):
            print("try y:",lastInterval, startx, startx + y, lastInterval[1])
            field[startx + y][lastInterval[1]] = "#"
    if interval[1] < lastInterval[1]:
        for x in range(steps):
            print("try x:", lastInterval[0], starty, x)
            field[lastInterval[0]][starty - x] = "#"
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
    print(field[i])

print(endsum)
print(intervals)
pyperclip.copy(endsum)