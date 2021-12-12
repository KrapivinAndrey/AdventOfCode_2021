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
        if v.islower():
            new_visited.append(v)
        s = 0
        for to in paths[v]:
            if to not in new_visited:
                s += countPath(to, new_visited)
        return s


v = ["start"]
print(countPath("start", v))
