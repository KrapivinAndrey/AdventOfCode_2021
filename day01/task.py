
with open('input.txt', 'r') as f:
    input = list(map(int, f.read().split('\n')))

def first():
    res = sum([1 if x < y else 0 for x, y in zip(input, input[1:])])
    print(res)

def second():
    windows = [x+y+z for x,y,z in zip(input, input[1:], input[2:])]
    res = sum([1 if x < y else 0 for x, y in zip(windows, windows[1:])])
    print(res)

second()