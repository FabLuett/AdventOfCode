import pyperclip
import sys
import math
import string
import re

endsum = 0

field = []
marked = []
directions = [(0,1), (0,-1), (1,0), (-1,0)]

file = sys.argv[1]
if '.txt' not in file:
    file += '.txt'
    
def initmarked():    
    global marked
    marked = []
    for i in range(len(field)):
        for j in range (len(field[i])):
            marked.append([])
            marked[j].append([False for d in directions])
    
with open(file) as f:
    for line in f.readlines():
        line = line.strip().lower()
        if(line == ""):
            continue    
        field.append ([c for c in line])      
        #marked.append ([[False, False, False, False] for c in line])      
    initmarked()
        
def scan ():
    global marked, field
    for i, line in enumerate (field):
        print(["x" if any(marked[i][j]) else line[j] for j in range (len(line))])
        
    print("_____________")
        
def add (t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1])
    
cache = {}
    
def visit (startdirection, startposition, writeLines = False):
    # todo: rewrite with stack instead of recursion...
    global marked, field,directions,cache
    
    initmarked()
    
    stack = [(startdirection, startposition)]
    way = []
    steps = 0
    
    while len(stack) > 0:
        entry = stack.pop ()
        direction = entry[0]
        position = entry[1]
    
        if not (position[0] >= 0 and position[0] < len(marked)):
            continue
        if not (position[1] >= 0 and position[1] < len(marked[position[0]])):
            continue
        if marked[position[0]][position[1]][directions.index(direction)]:
            continue
            
        if (direction, position) in cache:
            print("Found " , (direction, position), "in cache",  steps , cache[(direction, position)])
            print(stack)
            steps += cache[(direction, position)]
            stack = stack[cache[(direction, position)]:]
            print(stack)
            continue
        if writeLines:
            scan()
        if not any (marked[position[0]][position[1]]):
            steps += 1
        marked[position[0]][position[1]][directions.index(direction)] = True
        way.append((direction, position, steps))
        currentchar = field[position[0]][position[1]]
        if currentchar == ".": 
            #visit (direction, add(position, direction), writeLines)
            stack.insert (0,(direction, add (position, direction)))
        elif currentchar == "|":
            if direction[1] == 0:
                #visit (direction, add(position, direction), writeLines)
                stack.insert (0,(direction, add (position, direction)))
            else:
                #visit ( (-1,0), add(position, (-1,0)), writeLines)
                #visit ( (1,0), add (position, (1,0)), writeLines)
                stack.insert (0,((-1,0), add (position, (-1,0))))
                stack.insert (1,((1,0), add (position, (1,0))))
        elif currentchar == "-":
            if direction[1] == 0:
                #visit ( (0,1), add (position, (0,1)), writeLines)
                #visit ( (0,-1), add(position, (0,-1)), writeLines)
                stack.insert (0,((0,1), add (position, (0, 1))))
                stack.insert (1,((0,-1), add (position, (0, -1))))
            else:
                #visit (direction, add (position, direction), writeLines)
                stack.insert (0,(direction, add (position, direction)))
        elif currentchar == "/":
            newdirection = None
            if direction == (1,0):
                newdirection = (0,-1)
            elif direction == (-1,0):
                newdirection = (0, 1)
            elif direction == (0, 1):
                newdirection = (-1,0)
            else:
                newdirection = (1, 0)
            #visit ( newdirection, add (position, newdirection), writeLines)
            stack.insert (0,(newdirection, add (position, newdirection)))
        elif currentchar == "\\":
            newdirection = None
            if direction == (1,0):
                newdirection = (0,1)
            elif direction == (-1,0):
                newdirection = (0, -1)
            elif direction == (0, 1):
                newdirection = (1,0)
            else:
                newdirection = (-1, 0)
            #visit (newdirection, add (position, newdirection), writeLines)
            stack.insert (0,(newdirection, add (position, newdirection)))
            
    for item in way:
        cache[(item[0], item[1])] = steps- item[2]
    
    return steps
    
    
endsum = 0
for i in range(len(field)):
    for j in range(len(field[i])):
        if i == 0:
            # take each j downwards
            num = visit ((1,0), (i, j))
            if num > endsum:
                endsum = num
        elif i == len(field) -1:
            # take each j upwards
            num = visit ((-1, 0), (i, j))
            if num > endsum:
                endsum = num
                
        if j == 0:
            num = visit ((0, 1), (i, j))
            if num > endsum:
                endsum = num
        elif j == len(field[i]) -1:
            num = visit ((0, -1), (i, j))
            if num > endsum:
                endsum = num
        print (i,j, endsum)

print(endsum)
pyperclip.copy(endsum)