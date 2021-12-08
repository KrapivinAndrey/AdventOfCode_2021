def first():
    with open("input.txt") as f:
        input = list(map(lambda x: x.split("|")[1].strip(), f.readlines()))
    input2 = list(map(lambda x: [len(a) in (2, 4, 3, 7) for a in x.split(" ")], input))
    res = sum([sum(x) for x in input2])
    print(res)


def decrypt(signal, text):
    res = [None] * 10
    work = list(map(lambda x: set(x.strip()), signal.strip().split(" ")))

    res[1] = next(x for x in work if len(x) == 2)
    res[4] = next(x for x in work if len(x) == 4)
    res[7] = next(x for x in work if len(x) == 3)
    res[8] = next(x for x in work if len(x) == 7)

    res[6] = next(x for x in work if len(x) == 6 and (res[8] - x).issubset(res[1]))
    res[5] = next(x for x in work if len(x) == 5 and x.issubset(res[6]))
    res[2] = next(x for x in work if len(x) == 5 and len(res[5] - x) == 2)
    res[3] = next(x for x in work if len(x) == 5 and x != res[2] and x != res[5])
    res[9] = next(x for x in work if len(x) == 6 and len(x - res[3]) == 1)
    res[0] = next(x for x in work if x not in res)

    result = 0
    for a in list(map(set, text.strip().split(" "))):
        result = result * 10 + res.index(a)

    return result


def second():
    with open("input.txt") as f:
        input = list(map(lambda x: x.split("|"), f.readlines()))

    print(sum([decrypt(x[0], x[1]) for x in input]))


first()
second()
