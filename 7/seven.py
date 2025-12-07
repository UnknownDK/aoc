from copy import deepcopy

with open("mini.txt", "r") as file:
    data = [line.strip() for line in file.readlines()]

start = (0, 0)

for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == "S":
            start = (y, x)
            break
    if start != (0, 0):
        break

lines = [start[1]]
splits = 0

for y in range(len(data[1:])):
    nextlines = deepcopy(lines)
    for i, line in enumerate(lines):
        if data[y][line] == "^":
            splits += 1
            nextlines.remove(line)
            nextlines.insert(i, line - 1)
            nextlines.insert(i, line + 1)
    lines = list(set(nextlines))
print(splits)
