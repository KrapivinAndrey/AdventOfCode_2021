dots = set()
folds = []

with open("input.txt", 'r') as f:
    for r in f.readlines():
        if "fold along" in r:
            if "x" in r:
                folds.append((int(r.split("=")[1].strip()), 0))
            else:
                folds.append((0, int(r.split("=")[1].strip())))
        elif r.strip() == "":
            pass
        else:
            dots.add(tuple(map(lambda x: int(x.strip()), r.split(","))))


def fold(list_of_paper, fold_line):
    if fold_line[0] == 0:
        return fold_by_y(list_of_paper, fold_line[1])
    else:
        return fold_by_x(list_of_paper, fold_line[0])


def fold_by_y(list_of_paper, line):
    result = set()
    for dot in list_of_paper:
        if dot[1] > line:
            new_dot = (dot[0], line - (dot[1] - line))
        elif dot[1] == line:
            continue
        else:
            new_dot = (dot[0], dot[1])

        result.add(new_dot)

    return result


def print_paper(paper):
    for i in range(40):
        for j in range(80):
            if (j, i) in paper:
                print("#", end='')
            else:
                print(" ", end='')
        print("")

    print("------------------------")


def fold_by_x(list_of_paper, line):
    result = set()
    for dot in list_of_paper:
        if dot[0] > line:
            new_dot = (line - (dot[0] - line), dot[1])
        elif dot[0] == line:
            continue
        else:
            new_dot = (dot[0], dot[1])

        result.add(new_dot)

    return result


# first
print(len(fold(dots, folds[0])))


for task in folds:
    dots = fold(dots, task)

print_paper(dots)



