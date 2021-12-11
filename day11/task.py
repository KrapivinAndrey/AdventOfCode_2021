import itertools

class octopus:
    def __init__(self, power):
        self.power = power
        self.shine = False

    def __str__(self):
        return str(self.power)

    def __repr__(self):
        return str(self)

    def inc_power(self):
        self.power += 1

    def is_flashes(self):
        if self.shine:
            return False
        elif self.power > 9:
            self.shine = True
            return True

        return False

    def check(self):
        if self.shine:
            self.shine = False
            self.power = 0
            return 1
        else:
            return 0


with open("input.txt", "r") as f:
    matrix = []
    for row in f.readlines():
        matrix_row = []
        for a in row.strip():
            matrix_row.append(octopus(int(a)))
        matrix.append(matrix_row)

steps = 100
height = width = 10

flashing = 0

for step in range(steps):

    # phase 1: Adding power and flashing

    queue = list(itertools.product(range(10), range(10)))

    while queue:
        x, y = queue.pop()
        matrix[y][x].inc_power()
        if matrix[y][x].is_flashes():
            if x - 1 >= 0:
                queue.append((x - 1, y))

            if x + 1 < width:
                queue.append((x + 1, y))

            if y - 1 >= 0:
                queue.append((x, y - 1))

            if y + 1 < height:
                queue.append((x, y + 1))

            if x - 1 >= 0 and y - 1 >= 0:
                queue.append((x - 1, y - 1))

            if x + 1 < width and y + 1 < height:
                queue.append((x + 1, y + 1))

            if x + 1 < width and y - 1 >= 0:
                queue.append((x + 1, y - 1))

            if x - 1 >= 0 and y + 1 < height:
                queue.append((x - 1, y + 1))

    # phase 2: count flashing

    for i in range(10):
        for j in range(10):
            flashing += matrix[i][j].check()

    print(flashing)
