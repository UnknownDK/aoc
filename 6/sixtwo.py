with open("input.txt", "r") as file:
    matrix = [list(line.rstrip("\n")) for line in file]

operators = [op for op in matrix[-1] if op != " "]
opiter = 0
matrix = matrix[:-1]

maxlen = max(len(row) for row in matrix)
for row in matrix:
    row += [" "] * (maxlen - len(row) + 1)


numbs = []
sum = 0
for x in range(len(matrix[1])):
    numstr = ""
    for y in range(len(matrix)):
        try:
            int(matrix[y][x])
            numstr += matrix[y][x]
        except Exception:
            pass
    if numstr == "":
        rollsum = numbs[0]
        match operators[opiter]:
            case "+":
                for num in numbs[1:]:
                    rollsum += num
            case "*":
                for num in numbs[1:]:
                    rollsum *= num
        numbs = []
        sum += rollsum
        opiter += 1
    else:
        numbs.append(int(numstr))

print(sum)
