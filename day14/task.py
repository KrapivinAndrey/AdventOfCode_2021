from collections import Counter
from functools import reduce

with open("input.txt") as f:
    recipe = f.readline().strip()

    f.readline()
    formula = dict(
        map(lambda x: (x.split(" -> ")[0], x.split(" -> ")[1].strip()), f.readlines())
    )


def magic(elem):
    new = formula.get(elem)
    return elem[0] + new, new + elem[1]


def new_step(my_set):
    new = {}
    for ch, val in my_set.items():
        new1, new2 = magic(ch)
        new[new1] = new.get(new1, 0) + val
        new[new2] = new.get(new2, 0) + val

    return new


drop = dict(Counter([recipe[i : i + 2] for i in range(0, len(recipe) - 1)]))

for i in range(40):
    drop = new_step(drop)

stats = {}
for sym, val in drop.items():
    stats[sym[0]] = stats.get(sym[0], 0) + val
    stats[sym[1]] = stats.get(sym[1], 0) + val

print((max(stats.values()) - min(stats.values())) / 2)
