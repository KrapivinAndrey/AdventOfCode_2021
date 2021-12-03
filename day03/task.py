from functools import reduce
with open('input.txt', 'r') as f:
    input = list(map(lambda x: x.strip(), f.readlines()))


def first():
    matrix = list(map(list, zip(*input)))

    gamma = int("".join(max(set(lst), key=lst.count) for lst in matrix), 2)
    epsilon = int("".join(min(set(lst), key=lst.count) for lst in matrix), 2)

    print(f"gamma {gamma}")
    print(f"epsilon {epsilon}")
    print(f"ans = {gamma * epsilon}")


def second():
    i = 0

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

    oxy = int(input1[0], 2)
    co2 = int(input2[0], 2)

    print(f"Oxy = {oxy}")
    print(f"CO2 = {co2}")
    print(f"ans = {oxy * co2}")


first()
second()
