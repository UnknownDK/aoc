import re
from collections import deque
from dataclasses import dataclass

with open("input.txt", "r") as file:
    manual = [page.strip() for page in file.readlines()]


@dataclass
class Machine:
    indicator_lights: list[int]
    buttons: list[list[int]]
    joltage_requirements: list[int]


machines = []

for page in manual:
    indicator_match = re.search(r"\[([^\]]+)\]", page)
    indicator_lights = indicator_match.group(1) if indicator_match else None

    buttons = re.findall(r"\(([^)]+)\)", page)
    buttons = [list(map(int, btn.split(","))) for btn in buttons]

    joltage_math = re.search(r"\{([^}]+)\}", page)
    joltage_requirements = joltage_math.group(1) if joltage_math else None
    indicator_lights = [int(x == "#") for x in indicator_lights]
    joltage_requirements = list(map(int, joltage_requirements.split(",")))
    machines.append(
        Machine(
            indicator_lights=indicator_lights,
            buttons=buttons,
            joltage_requirements=joltage_requirements,
        )
    )


def solve_machine(machine):
    target = tuple(machine.indicator_lights)
    n_lights = len(target)
    start = tuple([0] * n_lights)

    queue = deque([(start, 0)])
    visited = {start}

    while queue:
        state, presses = queue.popleft()

        for button in machine.buttons:
            new_state = list(state)
            for light_index in button:
                if light_index < n_lights:
                    new_state[light_index] = 1 - new_state[light_index]

            new_state = tuple(new_state)

            if new_state == target:
                return presses + 1

            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, presses + 1))

    return -1


sum = 0
for i, machine in enumerate(machines):
    sum += solve_machine(machine)
print(sum)
