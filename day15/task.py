matrix = []
with open("input.txt") as f:
    for line in f.readlines():
        matrix.append(list(map(lambda x: int(x), [x for x in line.strip()])))

min_risk = sum(matrix[-1]) + sum([matrix[i][0] for i in range(len(matrix))]) - matrix[0][0] - matrix[-1][0]
min_path = []

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
        near = [_4, _3, _1, _2]
    else:
        near = [_2, _3, _4, _1]

    return near


def risk(vertex):
    return sum([matrix[j][i] for i, j in vertex])


def dfs(x, y, visited = None):
    global min_risk
    global min_path

    if visited is None:
        visited = []

    visited.append((x, y))

    if risk(visited) >= min_risk:
        return None
    elif x == len(matrix[0]) - 1 and y == len(matrix) - 1:
        min_risk = risk(visited)
        print(min_risk)
        min_path = visited
        return None

    for next_x, next_y in get_near(x, y):
        if (next_x, next_y) not in visited:
            dfs(next_x, next_y, visited.copy())
    return visited


dfs(0, 0)
print(min_risk - matrix[0][0])
