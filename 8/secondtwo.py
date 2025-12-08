from collections import Counter
from dataclasses import dataclass

import numpy as np


@dataclass
class jbox:
    point: np.ndarray
    circuit: int


with open("input.txt", "r") as file:
    data = [line.strip().split(",") for line in file.readlines()]
    jboxes = [jbox(point=np.array((int(x), int(y), int(z))), circuit=0) for x, y, z in data]

points = np.array([box.point for box in jboxes])
dists = np.linalg.norm(points[:, None, :] - points[None, :, :], axis=-1)

pairs = [((i, j), dists[i, j]) for i in range(len(jboxes)) for j in range(i + 1, len(jboxes))]
pairs.sort(key=lambda x: x[1])
shortest_dist = pairs[:10000]

newCircuit = 1
for (i, j), dist in shortest_dist:
    circuit = [x for x in [jboxes[i].circuit, jboxes[j].circuit] if x != 0]

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

    jboxes[i].circuit = circuit
    jboxes[j].circuit = circuit

    circuit_counts = len(dict(Counter(jbox.circuit for jbox in jboxes)).keys())
    if circuit_counts == 1:
        break
print(jboxes[i].point[0] * jboxes[j].point[0])
