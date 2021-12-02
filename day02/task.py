
with open('input.txt', 'r') as f:
    input = list(map(lambda x: x.split(' '), f.read().split('\n')))


def first():
    pos = sum([int(x[1]) for x in input if x[0] == "forward"])
    depth = sum([int(x[1]) for x in input if x[0] == "down"]) - sum([int(x[1]) for x in input if x[0] == "up"])
    print(f"pos {pos}")
    print(f"depth {depth}")

    print(f"ans {pos*depth}")


def second():
    def move(prev, el):
        if el[0] == "forward":
            return [prev[0]+int(el[1]), prev[1]+int(el[1])*prev[2], prev[2]]
        elif el[0] == "up":
            return [prev[0], prev[1], prev[2] - int(el[1])]
        elif el[0] == "down":
            return [prev[0], prev[1], prev[2] + int(el[1])]

    from functools import reduce
    res = reduce(move, input, [0, 0, 0])
    print(f"pos {res[0]}")
    print(f"depth {res[1]}")

    print(f"ans {res[0] * res[1]}")


first()
second()
