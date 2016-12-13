import re
from collections import Counter

with open("input.txt") as f:
    s = f.read().split('\n')

rx = re.compile('^(?P<name>.*)-(?P<id>\d+)\[(?P<order>.*)\]$')

def shift(to_shift, dist):
    return ''.join([chr((ord(c)-97+dist)%26+97) for c in to_shift])

good = 0
for l in s[:-1]:
    line = rx.match(l)

    ctr = Counter(line.group("name").replace('-',''))
    common = ''.join([v[0] for v in sorted(ctr.iteritems(), key=lambda(k, v): (-v, k))][:5])
    shifted = '-'.join([shift(ph, int(line.group('id'))) for ph in line.group("name").split('-')])

    if common == line.group('order'):
        good += int(line.group('id'))

    if shifted.find('north') > -1:
        print('Part 2: {} @  {}'.format(shifted, line.group('id')))

print('Part 1: {} real rooms found'.format(good))
