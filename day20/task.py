import numpy as np

with open("input.txt", "r") as f:
    algorithm = list(map(lambda x: int(x == "#"), f.readline().strip()))
    f.readline()

    image = np.array([[int(x == "#") for x in row.strip()] for row in f.readlines()])


def enhancement(small_matrix):
    num = 0
    for i in range(3):
        for j in range(3):
            num = num * 2 + small_matrix[i, j]

    return algorithm[num]


common = 0
for n in range(50):
    image = np.pad(image, (2, 2), "constant", constant_values=(common, common))
    new_matrix = image.copy()

    width, height = image.shape
    for x in range(1, width - 1):
        for y in range(1, height - 1):
            new_matrix[x, y] = enhancement(image[x - 1: x + 2, y - 1: y + 2])
    common = (common + 1) % 2

    for x in range(width):
        new_matrix[x, 0] = common
        new_matrix[x, -1] = common

    for y in range(height):
        new_matrix[0, y] = common
        new_matrix[-1, y] = common

    image = new_matrix[1:-1, 1:-1]

print(np.count_nonzero(image))
