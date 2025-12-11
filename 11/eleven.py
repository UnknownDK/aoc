from collections import Counter
from copy import deepcopy

with open("input.txt", "r") as file:
    data = [line.replace(":", "").strip().split() for line in file.readlines()]

devices = {}


for line in data:
    devices[line[0]] = line[1:]
paths = dict(Counter(devices["you"]))

outs = 0
while len(paths.keys()) > 0:
    # print(paths)
    nextpaths = {}
    for i in range(len(paths.keys())):
        last = list(paths.keys())[i]
        newpaths = devices[last]
        for new in newpaths:
            if new == "out":
                outs += paths[last]
                continue
            if new in nextpaths:
                nextpaths[new] += paths[last]
            else:
                nextpaths[new] = paths[last]
    paths = deepcopy(nextpaths)
print(outs)
