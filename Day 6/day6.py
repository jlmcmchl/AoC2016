from collections import Counter

with open("input.txt") as f:
    s = f.read().split('\n')[:-1]

print ' Part 1', ' Part 2'
for col in zip(*s):
    print '  ', Counter(col).most_common(1)[0][0], '\t  ', Counter(col).most_common(26)[-1][0]
