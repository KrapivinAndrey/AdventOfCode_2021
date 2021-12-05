import regex as re
import numpy as np
import math

with open("input.txt") as f:
    input = list(map(lambda x: x.strip(), f.readlines()))

coord = list(map(lambda x: re.findall(r"(\d+),(\d+) -> (\d+),(\d+)", x)[0], input))
coord = list(map(lambda x: [int(x[0]), int(x[1]), int(x[2]), int(x[3])], coord))

width = max([max(x[0], x[2]) for x in coord]) + 1
height = max([max(x[1], x[3]) for x in coord]) + 1

deeps = np.zeros((width, height))

for x in coord:
    # Вертикаль
    if x[0] == x[2]:
        for a in range(min(x[1], x[3]), max(x[1], x[3]) + 1):
            deeps[x[0], a] += 1
    # Горизонт
    elif x[1] == x[3]:
        for a in range(min(x[0], x[2]), max(x[0], x[2]) + 1):
            deeps[a, x[1]] += 1
    # Диагональ
    elif abs(x[1] - x[3]) == abs(x[1] - x[3]):
        dx = math.copysign(1, x[2] - x[0])
        dy = math.copysign(1, x[3] - x[1])
        for l in range(0, abs(x[1] - x[3]) + 1):
            deeps[int(x[0] + l * dx), int(x[1] + l * dy)] += 1


print(len(np.where(deeps >= 2)[0]))
