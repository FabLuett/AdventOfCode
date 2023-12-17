import pyperclip
import sys
import math
import string
import re

endsum = 0

file = sys.argv[1]
if '.txt' not in file:
    file += '.txt'
    
field = []
    
with open(file) as f:
    endsum = 0
    for line in f.readlines():
        line = line.strip().lower()
        if(line == ""):
            continue
        field.append([int(char) for char in line])
        
def isInverted (direction1, direction2):
    if direction1 == None:
        return False
    if direction1[0] == 0:
        return direction1[1] == direction2[1] * -1
    return direction1[0] == direction2[0] * -1
        

def visit (starti, startj, endi, endj):
    global field
    stack = [(starti, startj, 0, 1, None)]
    # i,j,total steps, steps in direction, direction
    distances = {}
    
    while len(stack) > 0:  
        node = stack.pop ()
        if node[0] < 0 or node[0] == len(field):
            continue
        if node[1] < 0 or node[1] == len(field[node[0]]):
            continue
        
        if (node[0], node[1]) in distances and distances[(node[0],node[1])] < node[2]:
            continue
        else:
            distances[(node[0],node[1])] = node[2]
        
        steps = node[2]
        stepsInDirection = node[3]
        direction = node[4]
        
        for d in [(0,1), (1,0),(0,-1), (-1,0)]:
            if isInverted (direction, d) or (direction == d and stepsInDirection == 3):
                # not allowed to go back or in the same direction >3 times
                continue
            i = node[0]
            j = node[1]
            newi = i + d[0]
            newj = j + d[1]
            stack.append((newi, newj, steps + field[i][j], stepsInDirection +1 if d == direction else 1, d))
    
    return distances[(endi, endj)] + field[endi][endj]
        
endsum = visit (0,0, len(field)-1, len(field[-1])-1)
print(endsum)
pyperclip.copy(endsum)