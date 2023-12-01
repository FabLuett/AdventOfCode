import pyperclip
import sys
import math
import string
import re

help_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}
 

file = sys.argv[1]
if '.txt' not in file:
    file += '.txt'
    
endsum = 0

with open(file) as f:
    for line in f.readlines():
        line = line.strip().lower ()
        if(line == ""):
            continue
        # cleanup string
        i = 0
        while i < len(line):
            for j in range(1,6):
                if line[i:i+j] in help_dict:
                    line = line[:i] + help_dict[line[i:i+j]] + line[i+j-1:]
                    break
            i += 1
        line = re.sub('[^0-9]', '', line)
        endsum += int(line[0] + line[len(line) -1])
        
print(endsum)        
pyperclip.copy(endsum)