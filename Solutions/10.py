from collections import defaultdict
from itertools import *
import re, math

with open("input.txt") as f:
    s = f.read().split('\n')[:-1]

done = []


valueLine = re.compile('value (\d+) goes to bot (\d+)', flags=0)
botLine = re.compile('bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)', flags=0)

def can_process(line, store):
    if line[0] == 'v':
        return True
    else:
        value = botLine.match(line)
        return len(store["bot"][value.group(1)]) > 1

def applyLine(line, store):
    if line[0] == 'v':
        value = valueLine.match(line)
        store["bot"][value.group(2)].add(int(value.group(1)))

    else:
        value = botLine.match(line)

        h = max(store["bot"][value.group(1)])
        l = min(store["bot"][value.group(1)])

        #print 'Bot {} gives {} to {} {}, and {} to {} {}'.format(value.group(1), l, value.group(2), value.group(3), h, value.group(4), value.group(5))

        store[value.group(2)][value.group(3)].add(l)
        store[value.group(4)][value.group(5)].add(h)
        #print '\t' + value.group(2) + ' ' + value.group(3)+':', '\t' + str(store[value.group(2)][value.group(3)])
        #print '\t' + value.group(4) + ' ' + value.group(5)+':', '\t' + str(store[value.group(4)][value.group(5)])

store = {"bot": defaultdict(set), "output":defaultdict(set)}

insts = 0

while len(s) > len(done):
    processed_any = False
    for line in s:
        if line not in done and can_process(line, store):
            processed_any = True
            applyLine(line, store)
            done.append(line)
            insts += 1

for bot in store["bot"]:
    if 61 in store["bot"][bot] and 17 in store["bot"][bot]:
        print bot

print [i for i in store["output"]["0"]][0] * [i for i in store["output"]["1"]][0] * [i for i in store["output"]["2"]][0]



#passed!
