from collections import Counter

paths = {}

with open("input.txt", "r") as f:
    for a in f.readlines():
        b = a.strip().split("-")
        if b[0] not in paths:
            paths[b[0]] = []
        if b[1] not in paths:
            paths[b[1]] = []
        paths[b[0]].append(b[1])
        paths[b[1]].append(b[0])


def countPath(v, visited):
    if v == "end":
        return 1
    else:
        new_visited = visited.copy()
        new_visited.append(v)
        s = 0
        for to in paths[v]:
            if can_visit(to, new_visited):
                s += countPath(to, new_visited)
        return s


def can_visit(t, visited):
    if t == "end":
        return True
    elif t == "start":
        return False
    elif t.isupper():
        return True
    elif t not in visited:
        return True
    else:
        c = [visited.count(x) for x in set(visited) if x.islower()]
        return 2 not in c



w = []
print(countPath("start", w))
