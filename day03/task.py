from functools import reduce
with open('input.txt', 'r') as f:
    input = list(map(lambda x: x.strip(), f.readlines()))

def bin_dec(x,y):
    return int(x)*2+int(y)

def first():
    matrix = list(map(list, zip(*input)))

    gamma = reduce(bin_dec, [max(set(lst), key=lst.count) for lst in matrix], 0)
    epsilon = reduce(bin_dec, [min(set(lst), key=lst.count) for lst in matrix], 0)

    print(f"gamma {gamma}")
    print(f"epsilon {epsilon}")
    print(f"ans = {gamma * epsilon}")


def second():
    i = 0
    oxy = []
    co2 = []

    input1 = input.copy()

    while len(input1) > 1:
        lst = [x[i] for x in input1]
        a = max(sorted(set(lst), reverse=True), key=lst.count)
        input1 = list(filter(lambda x: x[i] == a, input1))
        i += 1

    input2 = input.copy()
    i = 0
    while len(input2) > 1:
        lst = [x[i] for x in input2]
        a = min(sorted(set(lst)), key=lst.count)
        input2 = list(filter(lambda x: x[i] == a, input2))
        i += 1

    oxy = reduce(bin_dec, [char for char in input1[0]])
    co2 = reduce(bin_dec, [char for char in input2[0]])

    print(f"Oxy = {oxy}")
    print(f"CO2 = {co2}")
    print(f"ans = {oxy * co2}")


first()
second()
