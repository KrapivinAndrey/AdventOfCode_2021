import re


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


def explode(value: str) -> str:
    deep = 0
    left = right = 0
    for i in range(len(value)):
        a = value[i]
        if a == "[":
            deep += 1
            left = i
        elif a == "]":
            if deep >= 4:
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


print(explode("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]"))
