with open("input.txt", "r") as file:
    data = [line.strip() for line in file.readlines()]

start = (0, 0)

for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == "S":
            start = (y, x)
            break
    if start != (0, 0):
        break

memory = {}


def recurse(y, x):
    if y == len(data) - 1:
        return 1

    if (y, x) in memory:
        return memory[(y, x)]

    total = 0
    if data[y][x] == "^":
        total += recurse(y + 1, x - 1)
        total += recurse(y + 1, x + 1)
    elif data[y][x] == ".":
        total += recurse(y + 1, x)

    memory[(y, x)] = total
    return total


timelines = recurse(start[0] + 1, start[1])
print(timelines)
