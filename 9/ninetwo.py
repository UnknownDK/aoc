import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon as MplPolygon
from shapely.geometry import Polygon

with open("input.txt", "r") as file:
    tiles = [tile.strip().split(",") for tile in file.readlines()]
    tiles = np.array([np.array([int(x) for x in tile]) for tile in tiles])

# Find edges and calc areas
diffs = np.abs(tiles[:, None, :] - tiles[None, :, :]) + 1
areas = np.prod(diffs, axis=-1)

# Get indices of all point pairs
indices = [(i, j) for i in range(len(tiles)) for j in range(len(tiles)) if i != j]
area_values = [areas[i, j] for i, j in indices]

# Sort by area (largest to smallest) and keep track of point pairs
sorted_indices = sorted(range(len(area_values)), key=lambda k: area_values[k], reverse=True)
sorted_rectangles = [(indices[i], area_values[i]) for i in sorted_indices]

# Polygon from red tiles
tilegon_coords = [tuple(tile) for tile in tiles]
tilegon = Polygon(tilegon_coords)

for i, ((idx1, idx2), area) in enumerate(sorted_rectangles):
    # Define rectangle corners
    rectangle_coords = [
        (tiles[idx1][0], tiles[idx1][1]),
        (tiles[idx1][0], tiles[idx2][1]),
        (tiles[idx2][0], tiles[idx2][1]),
        (tiles[idx2][0], tiles[idx1][1]),
    ]
    rectangle = Polygon(rectangle_coords)
    if tilegon.covers(rectangle):
        print(f"Largest area: {area}")
        fig, ax = plt.subplots()
        ax.add_patch(MplPolygon(rectangle_coords, closed=True, facecolor="green", edgecolor="black"))
        ax.add_patch(MplPolygon(tilegon_coords, closed=True, facecolor="lightblue", edgecolor="black", alpha=0.5))
        x_coords = [coord[0] for coord in tilegon_coords + rectangle_coords]
        y_coords = [coord[1] for coord in tilegon_coords + rectangle_coords]
        padding = 2
        ax.set_xlim(min(x_coords) - padding, max(x_coords) + padding)
        ax.set_ylim(min(y_coords) - padding, max(y_coords) + padding)
        ax.set_aspect("equal", adjustable="box")
        plt.show()
        break
