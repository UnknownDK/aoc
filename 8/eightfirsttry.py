from collections import Counter
from dataclasses import dataclass

import numpy as np


@dataclass
class jbox:
    point: np.ndarray
    circuit: int


circuitcount = {}

with open("mini.txt", "r") as file:
    data = [line.strip().split(",") for line in file.readlines()]
    jboxes = [jbox(point=np.array((int(x), int(y), int(z))), circuit=0) for x, y, z in data]

dist_cache = {}

newCircuit = 1
conns = 0
for _ in range(9):
    prevDist = None
    minBoxes = (0, 0)
    for i, compbox in enumerate(jboxes):
        for j in range(i + 1, len(jboxes)):
            otherbox = jboxes[j]
            if np.array_equal(compbox.point, otherbox.point) or (
                compbox.circuit != 0 and compbox.circuit == otherbox.circuit
            ):
                continue
            key = tuple(sorted((i, j)))
            if key in dist_cache:
                dist = dist_cache[key]
            else:
                dist = np.linalg.norm(otherbox.point - compbox.point)
                dist_cache[key] = dist
            if prevDist is None or dist < prevDist:
                prevDist = dist
                minBoxes = (i, j)
    circuit = [x for x in [jboxes[minBoxes[0]].circuit, jboxes[minBoxes[1]].circuit] if x != 0]

    if len(circuit) == 1:
        circuit = circuit[0]
    elif len(circuit) > 1:
        circuitToMigrate = max(circuit)
        for box in jboxes:
            if box.circuit == circuitToMigrate:
                box.circuit = min(circuit)
        circuit = min(circuit)
    else:
        circuit = newCircuit
        newCircuit += 1
    for box in minBoxes:
        jboxes[box].circuit = circuit

circuit_counts = dict(Counter(jbox.circuit for jbox in jboxes))
# Sort by count (value), descending
del circuit_counts[0]
sorted_circuits = sorted(circuit_counts.items(), key=lambda item: item[1], reverse=True)
mulsum = 1
for item in sorted_circuits[:3]:
    mulsum *= item[1]
print(mulsum)
