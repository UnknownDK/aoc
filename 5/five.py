with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

ranges = []
ingredients = []

for line in lines:
    if "-" in line:
        first, second = line.split("-")
        first, second = int(first), int(second)
        ranges.append((first, second))
    elif line != "":
        ingredients.append(int(line))


def minify_ranges(ranges):
    ranges.sort(key=lambda range: range[0])
    minified = [ranges[0]]
    for currRange in ranges[1:]:
        lastRange = minified[-1]
        if currRange[0] <= lastRange[1] + 1:
            minified[-1] = (lastRange[0], max(lastRange[1], currRange[1]))
        else:
            minified.append(currRange)
    return minified


num_ranges = 0
while len(ranges) != num_ranges:
    num_ranges = len(ranges)
    ranges = minify_ranges(ranges)

fresh = 0
for ingredient in ingredients:
    for currRange in ranges:
        if currRange[0] <= ingredient and ingredient <= currRange[1]:
            fresh = fresh + 1
            break
print(fresh)

total = 0
for currRange in ranges:
    total = total + (currRange[1] - currRange[0] + 1)
print(total)
