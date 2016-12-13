from collections import defaultdict
from itertools import *
import re, math, copy

with open("input.txt") as f:
    s = f.read().split('\n')[:-1]

tests = [
    "The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip..",
    "The second floor contains a hydrogen generator.",
    "The third floor contains a lithium generator.",
    "The fourth floor contains nothing relevant"
]


var floors = [
    ["E", "SG", "SM", "PG", "PM"],
    ["TG", "RG", "RM", "CG", "CM"],
    ["TM"],
    []
]

var testFloors = [
    ["E", "HM", "LM"],
    ["HG"],
    ["LG"],
    []
]

def solved(puzzle):
    return len(puzzle[0]) == len(puzzle[1]) == len(puzzle[2]) == 0



states_seen = set()
curr_states = [testFloors]

i=0
while True:
    new_states = []
    for state in curr_states:
        if solved(state):
            print i
            raise Exception()
            break
        for move in attempt_move(state):
            if valid(move) and move not in states_seen and move not in curr_states:
                new_states.append(move)

        states_seen.add(state)
    i += 1
