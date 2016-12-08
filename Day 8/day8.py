from collections import Counter
import re, math

with open("input.txt") as f:
    s = f.read().split('\n')[:-1]

rect = re.compile("rect (\d+)x(\d+)")
rotate = re.compile("rotate (\w+) (\w)=(\d+) by (\d+)")

def init_screen(width, height):
    v = []
    for i in range(height):
        r = []
        for j in range(width):
            r.append(False)
        v.append(r)

    return v

def copy_screen(screen):
    v = []
    for i in range(len(screen)):
        r = []
        for j in range(len(screen[0])):
            r.append(True if screen[i][j] == True else False)
        v.append(r)

    return v


def init_rect(screen, width, height):
    for i in range(height):
        for j in range(width):
            screen[i][j] = True

def do_rotation(screen, item, index, by):
    new = copy_screen(screen)
    if item == 'x': #rotating a column
        for i in range(len(screen)):
            new[(i + by) % len(screen)][index] = screen[i][index]
    else: #rotating a row
        for i in range(len(screen[0])):
            new[index][(i + by) % len(screen[0])] = screen[index][i]

    return new

def get_lit(screen):
    return sum(row.count(True) for row in screen)



scr = init_screen(50,6)

for line in s:
    cmd  = rect.match(line)
    if cmd is not None:
        init_rect(scr, int(cmd.group(1)), int(cmd.group(2)))
    else:
        cmd = rotate.match(line)
        scr = do_rotation(scr, cmd.group(2), int(cmd.group(3)), int(cmd.group(4)))

print 'Part 1: {} lit pixels'.format(get_lit(scr))

for line in scr:
    print ''.join(['*' if e else ' ' for e in line])
