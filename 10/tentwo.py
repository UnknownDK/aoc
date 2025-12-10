import re
from dataclasses import dataclass

import numpy as np
from scipy.optimize import LinearConstraint
from scipy.optimize import milp

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


total = 0
for i, machine in enumerate(machines):
    positions = len(machine.joltage_requirements)
    buttons = len(machine.buttons)

    # Objective function, all 1
    # Coefficients are all 1, minimize total button presses
    c = np.ones(buttons)

    # constraint matrix A and bounds b
    # sum(count_i * button_i) == joltage_requirements
    A_eq = np.zeros((positions, buttons), dtype=int)
    b_eq = np.array(machine.joltage_requirements, dtype=int)
    for pos in range(positions):
        for button_idx, button in enumerate(machine.buttons):
            count = button.count(pos)
            A_eq[pos, button_idx] = count

    constraints = LinearConstraint(A_eq, b_eq, b_eq)

    # Whole numbers
    integrality = np.ones(buttons)

    result = milp(c=c, constraints=constraints, integrality=integrality)
    total += int(np.sum(result.x))

print(total)
