import pyperclip
import sys
import math
import string
import re

field = []
endsum = 0

file = sys.argv[1]
if '.txt' not in file:
    file += '.txt'
    
with open(file) as f:
    for line in f.readlines():
        line = line.strip().lower()
        if(line == ""):
            continue
        
        field.append (line)
        
for i, line in enumerate(field):
    word = False
    wordbegin = -1
    wordend = -1
    adjacent = False
    for j, char in enumerate(line):
        if char.isnumeric ():
            if not word:
                word = True
                wordbegin = j
            wordend = j
        elif word:
            word =False #word ends
            adjacent = False
            #print("word: " + line[wordbegin:wordend+1])
            for lineidx in range(max(0, i-1), i+2):
                if lineidx < 0 or lineidx >= len(field) -1:
                    continue
                searchline = field[lineidx][max(0,wordbegin-1):wordend+2]
                #print(searchline)
                searchline = re.sub("[0-9\.]", "", searchline)
                #print(searchline + "( " + str(len(searchline)) +")")
                adjacent |= len(searchline) > 0
                #print(str(adjacent))
            
            if(adjacent):
                endsum += int(field[i][wordbegin:wordend+1])
    if word:
        word =False #word ends
        for lineidx in range(len(field) -2, len(field)):
            searchline = field[lineidx][wordbegin:len(line)]
            searchline = re.sub("[0-9\.]", "", searchline)
            adjacent |= len(searchline) > 0
        
        if(adjacent):
            endsum += int(field[i][wordbegin:len(line)])
print(endsum)
pyperclip.copy(endsum)