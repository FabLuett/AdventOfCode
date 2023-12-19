import pyperclip
import sys
import math
import string
import re

endsum = 0
readRules = True
rules = {}
values = []

file = sys.argv[1]
if '.txt' not in file:
    file += '.txt'
    
with open(file) as f:
    endsum = 0
    for line in f.readlines():
        line = line.strip()
        if(line == ""):
            readRules = False
            continue

        if readRules:
            idx = line.split("{")
            conditions = idx[1][:-1].split(",")
            rules[idx[0]] = []
            for c in conditions:
                d = {}
                if ":" in c:
                    splitted = c[2:].split(":")
                    d[c[0]] = [c[1], int(splitted[0]), splitted[1]]
                else:
                    d[''] = c
                rules[idx[0]].append(d)
        else:
            d = {}
            parts = line[1:-1].split(",")
            for part in parts:
                splitted= part.split("=")
                d[splitted[0]] = int(splitted[1])
            values.append (d)
'''
for rule in rules:
    print(rule, rules[rule])
'''

for value in values:
    rule = "in"

    while rule != "A" and rule != "R":
        shouldbebroken = False
        currentrule = rules[rule]
        #rule: letter = < compare nextstep
        for checks in currentrule:
            for letter in checks:
                r = checks[letter]
                if letter == "":
                    rule = r
                elif r[0]== "<":
                    if value[letter] < r[1]:
                        rule = r[2]
                        shouldbebroken = True
                        break
                elif r[0] == ">":
                    if value[letter] > r[1]:
                        rule = r[2]
                        shouldbebroken = True
                        break
            if shouldbebroken:
                break
    if rule == "A":
        endsum += sum(value[x] for x in value)
        
        
print(endsum)
pyperclip.copy(endsum)