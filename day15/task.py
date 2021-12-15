import numpy as np

def get_near(x, y):
    near = []
    _1 = _2 = _3 = _4 = (0, 0)

    if x > 0:
        _1 = (x - 1, y)
    if y > 0:
        _2 = (x, y - 1)
    if x < len(matrix[0]) - 1:
        _3 = (x + 1, y)
    if y < len(matrix) - 1:
        _4 = (x, y + 1)

    if x > y:
        near = [_3, _4, _1, _2]
    else:
        near = [_2, _3, _4, _1]

    return near

def bfs():

    total = np.ones_like(matrix) * inf
    total[0, 0] = 0
    query = [(0, 0)]
    visited = 0

    while visited < len(query):
        x, y = query[visited]
        visited += 1
        for nx, ny in get_near(x, y):
            if total[nx, ny] > total[x, y] + matrix[nx, ny]:
                total[nx, ny] = total[x, y] + matrix[nx, ny]
                query.append((nx, ny))

    print(total[-1][-1])

matrix = np.genfromtxt('input.txt', dtype=int, delimiter=1)
inf = matrix.sum().sum()

bfs()
