import pyperclip
import sys
import math
import string
import re

endsum = 0

file = sys.argv[1]
if '.txt' not in file:
    file += '.txt'

def hashWord (word):
    count = 0
    for char in word:
        count += ord(char)
        count *= 17
        count %= 256
    return count

boxes = {}
    
with open(file) as f:
    endsum = 0
    for line in f.readlines():
        line = line.strip().replace("\n", "")
        if(line == ""):
            continue

        

        for word in line.split(","):
            parts = None
            remove = False
            if "=" in word:
                parts = word.split ("=")

            else:
                parts = word.split ("-")
                remove = True

            box = hashWord(parts[0])
            label = parts[1]

            if not box in boxes:
                boxes[box] = []
            
            lens = (parts[0], label)
            if remove:
                for i,l in enumerate(boxes[box]):
                    if l[0] == lens[0]:
                        boxes[box] = boxes[box][:i] + boxes[box][i+1:]
                        break
            else:
                #print ("Adding lens", lens, "go box", box, boxes[box])
                hasToAdd = True
                for i,l in enumerate(boxes[box]):
                    if l[0] == lens[0]:
                        boxes[box] = boxes[box][:i] + [lens] + boxes[box][i+1:]
                        hasToAdd =False
                        break

                if hasToAdd:
                    boxes[box].append(lens)


for box in boxes:
    for slot, lens in enumerate(boxes[box]):
        endsum +=(box + 1) * (slot + 1) * int(lens[1])     
        
print(endsum)
pyperclip.copy(endsum)