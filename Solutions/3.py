with open("input.txt") as f:
    s = f.read().split('\n')


print("Part 1")
good = 0
for t in s[:-1]:
    l = t.replace('  ', ' ').replace('  ', ' ').replace('  ', ' ').split(' ')
    line = []
    for c in l:
        if c != '':
            line.append(int(c))

    if line[0] + line[1] > line[2]:
        if line[0] + line[2] > line[1]:
            if line[1] + line[2] > line[0]:
                good = good + 1

print("{} real triangles".format(good))


print("Part 2")
good = 0
lines = []
for t in s[:-1]:
    l = t.replace('  ', ' ').replace('  ', ' ').replace('  ', ' ').split(' ')
    line = []
    for c in l:
        if c != '':
            line.append(int(c))
    lines.append(line)

for i in range(len(lines)//3):
    tup = zip(lines[3*i], lines[3*i+1], lines[3*i+2])
    print(tup)

    for line in tup:
        if line[0] + line[1] > line[2]:
            if line[0] + line[2] > line[1]:
                if line[1] + line[2] > line[0]:
                    good = good + 1

print("{} real triangles".format(good))
