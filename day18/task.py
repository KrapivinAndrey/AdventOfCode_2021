import re
import itertools

def magnitude(value: str) -> int:
    regexp = r"(\[(\d+),(\d+)\])"
    result = re.findall(regexp, value)
    while result:
        for block in result:
            value = value.replace(
                block[0], str(3 * int(block[1]) + 2 * int(block[2])), 1
            )
        result = re.findall(regexp, value)

    return int(value)


def split(value: str) -> str:
    regexp = r"(\d{2,})"
    result = re.findall(regexp, value)
    if result:
        block = int(result[0])
        a = int(block / 2)
        b = block - a
        return value.replace(str(block), f"[{a},{b}]", 1)

    return value


def explode(value: str) -> str:
    deep = 0
    left = right = 0
    for i in range(len(value)):
        a = value[i]
        if a == "[":
            deep += 1
            left = i
        elif a == "]":
            if deep > 4:
                right = i
                block = value[left + 1:right].split(",")

                left_part = value[: left]
                right_part = value[right + 1:]
                value = (
                    replace_left(left_part, block[0])
                    + "0"
                    + replace_right(right_part, block[1])
                )

                return value
            else:
                deep -= 1

    return value


def replace_left(part, num):
    regexp = r"(\d+)"
    result = re.findall(regexp, part)
    if result:
        new_num = int(result[-1]) + int(num)
        head, _sep, tail = part.rpartition(result[-1])
        return head + str(new_num) + tail

    return part


def replace_right(part, num):
    regexp = r"(\d+)"
    result = re.findall(regexp, part)
    if result:
        new_num = int(result[0]) + int(num)
        return part.replace(result[0], str(new_num), 1)

    return part


with open("input.txt") as f:
    tasks = list(map(lambda x: x.strip(), f.readlines()))


def calculate(example):
    while True:
        new_mean = explode(example)
        if new_mean != example:
            example = new_mean
            continue
        else:
            new_mean = split(example)
            if new_mean != example:
                example = new_mean
                continue
        break

    return example


work = None
for task in tasks:
    if work is None:
        work = task
        continue
    else:
        work = f"[{work},{task}]"
        work = calculate(work)


print(magnitude(work))

max_mean = 0
for i in range(len(tasks)):
    for j in range(len(tasks)):

        if i == j:
            continue

        x = calculate(f"[{tasks[i]},{tasks[j]}]")
        y = calculate(f"[{tasks[j]},{tasks[i]}]")
        max_mean = max(max_mean, magnitude(x), magnitude(y))

print(max_mean)