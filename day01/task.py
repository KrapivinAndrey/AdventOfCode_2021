
with open('input.txt', 'r') as f:
    input = list(map(int, f.read().split('\n')))

res = sum([1 if x < y else 0 for x, y in zip(input, input[1:])])
print(res)