from collections import Counter

with open("input.txt") as f:
    s = f.read().split('\n')[:-1]

for col in zip(*s):
    print Counter(col).most_common(1)[-1], Counter(col).most_common(26)[-1]
