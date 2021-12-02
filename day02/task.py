
with open('input.txt', 'r') as f:
    input = list(map(lambda x: x.split(' '), f.read().split('\n')))


def first():
    pos = sum([int(x[1]) for x in input if x[0] == "forward"])
    depth = sum([int(x[1]) for x in input if x[0] == "down"]) - sum([int(x[1]) for x in input if x[0] == "up"])
    print(f"pos {pos}")
    print(f"depth {depth}")

    print(f"ans {pos*depth}")


first()
