from dataclasses import dataclass

import numpy as np

with open("mini.txt") as f:
    lines = f.read().splitlines()


@dataclass
class Present:
    shape: np.ndarray


@dataclass
class Grid:
    shape: np.ndarray
    presents: list[Present]


all_presents = []
all_grids = []

doing_grid = False
cur_present = None
for line in lines:
    if line.endswith(":"):
        curr_present = []
    elif line == "" and not doing_grid:
        all_presents.append(Present(shape=np.array(curr_present)))
    elif "x" in line:
        doing_grid = True
        split_line = line.split(":")
        grid_shape = tuple(int(x) for x in split_line[0].split("x"))
        grid_present_cout = split_line[1].strip().split(" ")
        grid_presents = []
        for idx, present_count in enumerate(grid_present_cout):
            if int(present_count) > 0:
                grid_presents.extend([all_presents[idx]] * int(present_count))
        all_grids.append(Grid(shape=np.zeros(grid_shape, dtype=int), presents=grid_presents))
    else:
        curr_present.append([int(x == "#") for x in line.strip()])


def get_unique_rotations(shape):
    rotations = []
    for k in range(4):
        rotated = np.rot90(shape, k)
        if not any(np.array_equal(rotated, r) for r in rotations):
            rotations.append(rotated)
    return rotations


def can_place(grid, present_shape, top, left):
    h, w = present_shape.shape
    grid_h, grid_w = grid.shape
    if top + h > grid_h or left + w > grid_w:
        return False
    grid_slice = grid[top : top + h, left : left + w]
    return np.all((grid_slice + present_shape) <= 1)


def place(grid, present_shape, top, left, val):
    h, w = present_shape.shape
    grid[top : top + h, left : left + w] += present_shape * val  # Remove by val = -1


def solve(grid, presents, idx=0):
    if idx == len(presents):
        return True

    present = presents[idx]
    for rotation in get_unique_rotations(present.shape):
        ph, pw = rotation.shape
        # Create a sliding window view of the grid
        windows = np.lib.stride_tricks.sliding_window_view(grid, (ph, pw))
        # Find all positions where the present can be placed (no overlap)
        can_place_mask = np.all((windows + rotation) <= 1, axis=(-2, -1))
        # Get indices where placement is possible
        possible_positions = np.argwhere(can_place_mask)
        for pos in possible_positions:
            i, j = pos
            place(grid, rotation, i, j, 1)
            if solve(grid, presents, idx + 1):
                return True
            place(grid, rotation, i, j, -1)  # Remove
    return False


solutions = 0
for grid_obj in all_grids:
    grid = grid_obj.shape.copy()
    presents = grid_obj.presents
    grid_area = grid.shape[0] * grid.shape[1]
    total_present_area = sum(np.sum(p.shape) for p in presents)
    if total_present_area > grid_area:
        continue
    if solve(grid, presents):
        solutions += 1
print(f"Total solutions found: {solutions}")
