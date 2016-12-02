with open("input.txt") as f:
    s = f.read().split('\n')

permitted = ['DR', 'D', 'DL',
             'R', 'UDLR', 'L'
             'UR', 'U', 'UL']

coords = [1,2,3,
          4,5,6,
          7,8,9]

x = 1
y = 1
print('Part 1')
for line in s[:-1]:
    for c in line:
        if c in permitted[3*y + x]:
            if c == 'U':
                y = y-1
            elif c == 'D':
                y = y+1
            elif c == 'L':
                x = x-1
            elif c == 'R':
                x = x+1
    print(coords[3 * y + x])


permitted = ['',      '',    'D',     '',   '',
             '',     'DR',  'UDLR',  'DL',  '',
             'R',   'UDLR', 'UDLR', 'UDLR', 'L',
             '',     'UR',  'UDLR',  'UL',  '',
             '',      '',    'U',     '',   '',]

coords = [0 ,    0,      1,      0,     0,
          0,     2,      3,      4,     0,
          5,     6,      7,      8,     9,
          0,    'A',    'B',    'C',    0,
          0,     0,     'D',     0,     0]

x = 0
y = 2
print('Part 2')
for line in s[:-1]:
    for c in line:
        if c in permitted[5*y + x]:
            if c == 'U':
                y = y-1
            elif c == 'D':
                y = y+1
            elif c == 'L':
                x = x-1
            elif c == 'R':
                x = x+1
    print(coords[5 * y + x])
