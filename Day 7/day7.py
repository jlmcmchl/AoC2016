from collections import Counter
import re, math

with open("input.txt") as f:
    s = f.read().split('\n')[:-1]



def has_abba(text):
    for i in range(len(text) - 3):
        if text[i] == text[i+3] and text[i+1] == text[i+2] and  text[i] != text[i+1] :
            return True
    return False

def supports_tls(ip):
    line = ip.replace(']','[').split('[')

    has_in = False
    has_out = False
    for i in range(len(line)):
        if i % 2 == 0:
            if has_abba(line[i]):
                has_out = True
        else:
            if has_abba(line[i]):
                return False

    return has_out


def find_abas(line):
    found = []
    for i in range(len(line) - 2):
        if line[i] == line[i+2] and line[i] != line[i+1] and line[i+1] != '[' and line[i+1] != ']':
            found.append(line[i:i+3])
    return found

def has_bab(line, aba):
    bab = aba[1:3]+aba[0]
    return bab in line


def supports_ssl(ip):
    line = ip.replace(']','[').split('[')

    abas = []
    babs = []
    for i in range(len(line)):
        if i % 2 == 0:
            abas.extend(find_abas(line[i]))
        else:
            babs.extend(find_abas(line[i]))

    for aba in abas:
        if aba[1]+aba[0]+aba[1] in babs:
            return True
    return False

cnt = 0
for l in s:
    if supports_tls(l):
        cnt += 1

print("Part 1: {}".format(cnt))

cnt = 0
for l in s:
    if supports_ssl(l):
        cnt += 1

print("Part 2: {}".format(cnt))
