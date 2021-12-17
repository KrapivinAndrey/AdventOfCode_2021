import math
import re

with open("input.txt") as f:
    target = f.readline().strip()

x0, x1, y0, y1 = list(
    map(lambda x: int(x), re.findall(r"x=(\d+)\.\.(\d+), y=(-\d+)..(-\d+)", target)[0])
)

vx_min = int((math.sqrt(8 * x0) + 1) / 2)


def get_time(vx0):
    t = 0
    x = 0
    while x < x1:
        t += 1
        x += vx0
        vx0 -= 1
        if vx0 == 0:
            return t

    return t


def all_dots(vx, vy):
    x_new = y_new = 0
    x_y = [(x_new, y_new)]
    t = 0
    while y_new > y0:

        x_new = x_y[t - 1][0] + vx
        y_new = x_y[t - 1][1] + vy
        vx = max(vx - 1, 0)
        vy -= 1
        x_y.append((x_new, y_new))

    return x_y


y_max = []
all_possible = set()
for vx in range(vx_min, x1+1):
    for vy in range(y0, -y0+1):
        x_y = all_dots(vx, vy)
        for x, y in x_y:
            if x0 <= x <= x1 and y0 <= y <= y1:
                all_possible.add((vx, vy))
                y_max.append(max([i[1] for i in x_y]))
                break

print(max(y_max))
print(len(all_possible))
