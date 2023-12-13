import pyperclip
import sys
import math
import string
import re

endsum = 0

file = sys.argv[1]
if '.txt' not in file:
    file += '.txt'
    
lines = []
patterns = []
    
with open(file) as f:
    endsum = 0
    for line in f.readlines():
        line = line.strip().lower()
        if(len(line) == 0):
            if len(lines) > 0:
                patterns.append(lines)
                lines  = []
            continue
        lines.append(line)
patterns.append(lines)

coltracker = {}
rowtracker = {}

def analysePattern (pattern):
    endsum = 0
    # rows
    for i in range(len(pattern) -1):
        match=True
        tocheck = 0
        isReplaced = False
        while match and i - tocheck >= 0 and i +tocheck +1  < len(pattern):
            differences = sum([0 if pattern[i-tocheck][ind] == pattern[i+tocheck+1][ind] else 1 for ind in range(len(pattern[i]))])
            match = differences == 0
            if(not match) and differences == 1:
                if isReplaced:
                    break
                isReplaced = True
                match = True
            tocheck += 1
        if match and isReplaced:
            endsum += 100 * (i+1)
            match= False
            #return endsum
    for j in range(len(pattern[0]) -1):
        match = True
        tocheck = 0
        isReplaced = False
        while match and j - tocheck >= 0 and j + 1+ tocheck < len(pattern[0]):
            differences = sum([0 if l[j-tocheck] == l[j+1+tocheck] else 1 for l in pattern])
            match = differences == 0
            if(not match) and differences == 1:
                if isReplaced:
                    break
                isReplaced = True
                match = True
            tocheck += 1
        if match and isReplaced:
            endsum += j +1
            match= False
            #return endsum
    #print(endsum)
    return endsum        
    

endsum = sum ([analysePattern(pattern) for pattern in patterns])
    
print(endsum)
pyperclip.copy(endsum)