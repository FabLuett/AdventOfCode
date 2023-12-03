import pyperclip
import sys
import math
import string
import re

endsum = 0

file = sys.argv[1]
if '.txt' not in file:
    file += '.txt'
    
with open(file) as f:
    endsum = 0
    for line in f.readlines():
        line = line.strip().lower()
        if(line == ""):
            continue
        
        
        
print(endsum)
pyperclip.copy(endsum)