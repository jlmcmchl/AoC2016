from collections import Counter
from itertools import *
import re, math

with open("input.txt") as f:
    s = f.read().split('\n')[:-1]

tests = [
    "(3x3)XYZ",
    "X(8x2)(3x3)ABCY",
    "(27x12)(20x12)(13x14)(7x10)(1x12)A",
    "(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN"
]

compress = re.compile('\((\d+)x(\d+)\)', flags=0)

def findProcessedLen(text):
    i = 0
    lengths = []
    match = compress.search(text, i)
    if match is not None:
        lengths.append(match.start(0))

    while i < len(text):
        match = compress.search(text, i)
        if match is None:
            break
        found = True

        blocklen = int(match.group(1))
        copies = int(match.group(2))

        decompLen = findProcessedLen(text[match.end(0):match.end(0) + blocklen])

        lengths.append(decompLen * copies)
        i = match.end(0) + blocklen
    return sum(lengths) + len(text) - i

nums = re.compile(r'(\d+)')

notLeft = lambda c : c != '('
notRight = lambda c : c != ')'

def decompress(gen):
    count = 0
    try:
        while True:
            count += len(list(takewhile(notLeft, gen)))
            marker = ''.join(takewhile(notRight, gen))
            [numChars, numRepeat] = map(int, nums.findall(marker))
            count += decompress(islice(gen, numChars)) * numRepeat
    except:
        return count


for test in tests:
    print findProcessedLen(test)

#passed!
for line in s:
    print decompress(iter(line))
    length = findProcessedLen(line)
    print(length)
