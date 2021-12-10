with open("input.txt") as f:
    input = list(map(lambda x: x.strip(), f.readlines()))


def check_error(brackets, return_queue = False):
    queue = []
    opens = {"(", "[", "{", "<"}
    for char in brackets:
        if char in opens:
            queue.append(char)
        else:
            last = queue.pop()

            if not (
                last == "(" and char == ")"
                or last == "[" and char == "]"
                or last == "{" and char == "}"
                or last == "<" and char == ">"
            ):
                return char
    if return_queue:
        return queue


def first():
    coast = {None: 0, ')': 3, ']': 57, '}': 1197, '>': 25137}
    result = sum([coast[check_error(x)] for x in input])
    print(result)




