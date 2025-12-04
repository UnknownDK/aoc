import copy

with open("input.txt", "r") as f:
    lines = [list(line.strip()) for line in f.readlines()]


def AtOrOut(y, x):
    paper = False
    if x < 0 or y < 0:
        return paper
    try:
        paper = lines[y][x] == "@"
    except IndexError:
        pass
    return paper


nextlines = copy.deepcopy(lines)
last_accessible = -1
accessible = 0
while accessible != last_accessible:
    last_accessible = accessible
    lines = copy.deepcopy(nextlines)
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] == "@":
                nearby = 0
                counter = 0
                for yiter in range(y - 1, y + 2):
                    for xiter in range(x - 1, x + 2):
                        if (xiter == x) and (yiter == y):
                            pass
                        else:
                            nearby += AtOrOut(yiter, xiter)
                if nearby < 4:
                    accessible += 1
                    nextlines[y][x] = "."


print(accessible)
