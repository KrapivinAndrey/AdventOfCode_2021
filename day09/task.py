import near as near
import numpy as np

matrix = []
with open("input.txt") as f:
    for line in f.readlines():
        matrix.append(list(map(lambda x: int(x), [x for x in line.strip()])))


def get_near(x, y):
    near = []
    if x > 0:
        near.append((x - 1, y))
    if y > 0:
        near.append((x, y - 1))
    if x < len(matrix[0]) - 1:
        near.append((x + 1, y))
    if y < len(matrix) - 1:
        near.append((x, y + 1))

    return near


def is_lower(x, y):
    return all(matrix[y][x] < matrix[a[1]][a[0]] for a in get_near(x, y))


def find_basin(x, y):
    basin = [(x, y)]
    queue = [(x, y)]
    while queue:
        x_now, y_now = queue.pop()
        for x_new, y_new in get_near(x_now, y_now):
            if (
                matrix[y][x] < matrix[y_new][x_new] < 9
                and (x_new, y_new) not in basin
            ):
                queue.append((x_new, y_new))
                basin.append((x_new, y_new))

    return basin


def first():
    res = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if is_lower(j, i):
                res += matrix[i][j] + 1

    print(res)


def second():
    all_basin = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if is_lower(j, i):
                all_basin.append(find_basin(j, i))

    all_basin.sort(key=len, reverse=True)

    print(len(all_basin[0]) * len(all_basin[1]) * len(all_basin[2]))


second()
