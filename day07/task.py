with open("input.txt") as f:
    input = list(map(lambda x: int(x), f.readline().split(",")))

max_pos = max(input)
min_pos = min(input)

optimal_fuel = 100000000
optimal_pos = -1


def cast(a, b):
    n = abs(a - b)
    return n * (n + 1) / 2


for i in range(min_pos, max_pos + 1):
    fuel = sum([cast(x, i) for x in input])
    if fuel < optimal_fuel:
        optimal_fuel = fuel
        optimal_pos = i

print(optimal_pos)
print(optimal_fuel)
