with open("input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

operators = lines[-1].split()
res = [int(num) for num in lines[0].split()]
lines = lines[1:-1]


for line in lines:
    nums = [int(num) for num in line.split()]
    for idx in range(len(nums)):
        match operators[idx]:
            case "*":
                res[idx] *= nums[idx]
            case "+":
                res[idx] += nums[idx]

print(sum(res))
