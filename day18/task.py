import re


def magnitude(value:str)->int:
    regexp = r"(\[(\d+),(\d+)\])"
    result = re.findall(regexp, value)
    while result:
        for block in result:
            value = value.replace(block[0], str(3 * int(block[1]) + 2 * int(block[2])), 1)
        result = re.findall(regexp, value)

    return int(value)


print(magnitude("[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]"))
