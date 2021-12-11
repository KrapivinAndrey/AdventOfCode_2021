
with open("input.txt") as f:
    input = list(map(lambda x: x.strip(), f.readlines()))


def check_error(brackets):
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

def check_incomplete(brackets):
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
                return []

    return queue


def first():
    cost = {None: 0, ')': 3, ']': 57, '}': 1197, '>': 25137}
    result = sum([cost[check_error(x)] for x in input])
    print(result)


def second():
    def points(ending):
        cost = {'(': 1, '[': 2, '{': 3, '<': 4}
        result = 0
        while ending:
            result = result * 5 + cost[ending.pop()]

        return result

    points = list(filter((0).__ne__, [points(check_incomplete(x)) for x in input]))
    points.sort()
    print(points[len(points) // 2])


second()
