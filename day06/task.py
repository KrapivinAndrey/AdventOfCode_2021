import numpy as np
from numpy import dtype

with open("input.txt") as f:
  input = list(map(lambda x: int(x), f.readline().split(",")))

arr = np.zeros(9, dtype='int64')
for x in input:
  arr[x] += 1

for day in range(1, 257):
  new_arr = np.zeros(9, dtype='int64')
  for i in range(7, -1, -1):
    new_arr[i] = arr[i+1]
  new_arr[8] += arr[0]
  new_arr[6] += arr[0]

  arr = new_arr

print(np.sum(arr))
