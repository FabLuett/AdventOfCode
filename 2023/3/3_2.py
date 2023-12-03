import pyperclip
import sys
import math
import string
import re

field = []
endsum = 0

words = {
}

file = sys.argv[1]
if '.txt' not in file:
    file += '.txt'
    

with open(file) as f:
    for i, line in enumerate(f.readlines()):
        line = line.strip().lower()
        if(line == ""):
            continue
        
        field.append (line)
        words[i] = {}
        word = False
        wordbegin = -1
        wordend = -1
        for j, char in enumerate(line):
            if char.isnumeric ():
                if not word:
                    word = True
                    wordbegin = j
                wordend = j
            elif word:
                word =False #word ends
                #if i == 119 or i == 120 or i == 121:
                    #print("Found word " + line[wordbegin:wordend+1] + " in line " + str(i))
                    #print(line)
                key = line[wordbegin:wordend+1]
                if key in words[i]:
                    count = 1
                    key =key + "_1"
                    while key in words[i]:
                        count+=1
                        key = key[:len(key)-1] + str(count)
                        
                words[i][key] = [wordbegin, wordend]
        if word:
                word =False #word ends
                key = line[wordbegin:wordend+1]
                if key in words[i]:
                    count = 1
                    key = str(key) + "_1"
                    while key in words[i]:
                        count+=1
                        key = key[:len(key)-1] + str(count)
                words[i][key] = [wordbegin, wordend]

print(words[118])
print(words[119])
print(words[120])
        
for i, line in enumerate(field):
    for j, char in enumerate(line):
        if char == "*":
            number1 = 0
            number2 = 0
            br = False
            for searchline in range(max(0, i-1), i+2):
                currentwords = words[searchline]
                if br:
                    break
                for word in currentwords:
                    # 0,2
                    # muss zwischen j-1 und j+1
                    left = currentwords[word][0]
                    right = currentwords[word][1]
                    #if i == 119 and j == 46:
                        #print('i','j', 'search', 'left', 'right')
                        #print(i, j,searchline, left, right,  (left >= j-1 and left <= j+1) or (right >= j-1 and right <= j+1))
                        #print(words[searchline])
                    if (left >= j-1 and left <= j+1) or (right >= j-1 and right <= j+1):
                        if number1 == 0:
                            idx = word.find('_')
                            if idx > 0:
                                word = word[:idx]
                            number1 = int(word)
                        elif number2 == 0:
                            #print("added " + str(i) +"," + str(j), str(number1) + ";" + str(word))
                            idx = word.find('_')
                            if idx > 0:
                                word = word[:idx]
                            number2 = int(word)
                            br = True
                            break
                        else:
                            number2 = 0
                            break
                    elif left > j+1:
                        break
            if number1 > 0 and number2 > 0:
                endsum += number1 * number2
            if number1==0 or number2 ==0:
                print("not added " + str(i) +", "+ str(j))
                #print(line)

print(endsum)
pyperclip.copy(endsum)