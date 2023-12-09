import pyperclip
import sys
import math
import string
import re

endsum = 0

extrapolate= {}

file = sys.argv[1]
if '.txt' not in file:
    file += '.txt'
    
with open(file) as f:
    endsum = 0
    i = 0
    for line in f.readlines():
        line = line.strip().lower()
        if(line == ""):
            continue
        
        numbers = [int(number) for number in line.split (" ")]
        extrapolate[i] = []
        extrapolate[i].append(numbers)
        arr = numbers
        j = 0
        while any (n != 0 for n in extrapolate[i][j]):
            arr = extrapolate[i][j]
            extrapolate[i].append([])
            j += 1
            for index in range(1, len(arr)):
                extrapolate[i][j].append(arr[index] -arr[index-1])

        i += 1
        
        
for key in extrapolate:
    lists = extrapolate[key]
    for i in range(len(lists)-1, -1, -1):
        lists[i].insert(0,0)
        if (i < len(lists) -1):
            lists[i][0] = lists[i][1] - lists[i+1][0]
            if i == 0:
                endsum += lists[i][1] - lists[i+1][0]
print(extrapolate)
print(endsum)
pyperclip.copy(endsum)