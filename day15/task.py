import numpy as np

def get_near(x, y, risk):
    near = []
    _1 = _2 = _3 = _4 = (0, 0)

    if x > 0:
        _1 = (x - 1, y)
    if y > 0:
        _2 = (x, y - 1)
    if x < len(risk[0]) - 1:
        _3 = (x + 1, y)
    if y < len(risk) - 1:
        _4 = (x, y + 1)

    if x > y:
        near = [_3, _4, _1, _2]
    else:
        near = [_2, _3, _4, _1]

    return near


def bfs(risk):
    inf = risk.sum().sum()
    total = np.ones_like(risk) * inf
    total[0, 0] = 0
    query = [(0, 0)]
    visited = 0

    while visited < len(query):
        x, y = query[visited]
        visited += 1
        for nx, ny in get_near(x, y, risk):
            if total[nx, ny] > total[x, y] + risk[nx, ny]:
                total[nx, ny] = total[x, y] + risk[nx, ny]
                query.append((nx, ny))

    print(total[-1][-1])


matrix = np.genfromtxt('input.txt', dtype=int, delimiter=1)
bfs(matrix)

width, height = matrix.shape

new_matrix = np.zeros((width * 5, height * 5), dtype=int)
for i in range(width * 5):
    for j in range(height * 5):
        inc = i // width + j // height
        new_matrix[i, j] = (matrix[i % width, j % height] + inc)
        if new_matrix[i, j] > 9:
            new_matrix[i, j] = new_matrix[i, j] % 10 + 1

bfs(new_matrix)
