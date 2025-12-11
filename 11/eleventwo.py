from dataclasses import dataclass
from dataclasses import field
from typing import Tuple

with open("input.txt", "r") as file:
    data = [line.replace(":", "").strip().split() for line in file.readlines()]

devices = {}


@dataclass
class Visitor:
    count_dict: dict[Tuple[bool, bool], int] = field(default_factory=dict)

    def add_path(self, count: int, dac: bool, fft: bool):
        dac_and_fft = (dac, fft)
        self.count_dict[dac_and_fft] = self.count_dict.get(dac_and_fft, 0) + count


for line in data:
    devices[line[0]] = line[1:]

paths = {}
if "svr" in devices:
    for start_node in devices["svr"]:
        is_dac = start_node == "dac"
        is_fft = start_node == "fft"
        paths[start_node] = Visitor()
        paths[start_node].add_path(1, is_dac, is_fft)

outs = 0
while len(paths) > 0:
    next_paths = {}
    for last_path, visitor in paths.items():
        if last_path not in devices:
            continue

        for new_path in devices[last_path]:
            for (dac_status, fft_status), count in visitor.count_dict.items():
                if new_path == "out":
                    if dac_status and fft_status:
                        outs += count
                    continue

                new_dac = dac_status or (new_path == "dac")
                new_fft = fft_status or (new_path == "fft")

                if new_path not in next_paths:
                    next_paths[new_path] = Visitor()
                next_paths[new_path].add_path(count, new_dac, new_fft)

    paths = next_paths

print(outs)
