import hashlib

with open("input.txt") as f:
    pwd = f.read().split("\n")[0]


res1 = ""
found = 0
i = 0
while found < 8:
    i += 1
    dgst  = hashlib.md5()
    dgst.update(pwd + str(i))
    rep = dgst.hexdigest()
    if (rep[:5] == "00000"):
        res1 += rep[5]
        found += 1

print("Part 1: {}".format(res1))


res2 = [-1,-1,-1,-1,-1,-1,-1,-1]
i = 0
while any([j == -1 for j in res2]):
    i += 1
    dgst  = hashlib.md5()
    dgst.update(pwd + str(i))
    rep = dgst.hexdigest()
    if (rep[:5] == "00000"):
        if 48 <= ord(rep[5]) <= 55:
            if res2[int(rep[5])] == -1:
                res2[int(rep[5])] = rep[6]

print("Part 2: {}".format(''.join(res2)))
