import numpy as np

with open("input.txt", "r") as file:
    tiles = [tile.strip().split(",") for tile in file.readlines()]
    tiles = np.array([np.array([int(x) for x in tile]) for tile in tiles])

diffs = (tiles[:, None, :] - tiles[None, :, :]) + 1
areas = np.prod(diffs, axis=-1)

print(f"Max area: {np.max(areas)}")
