import numpy as np

arr = np.empty((0,2), int)

for i in range(4):
    val1 = np.random.randint(low=1, high=100, size=1)[0]
    val2 = np.random.randint(low=1, high=100, size=1)[0]
    arr = np.append(arr, np.array([[val1,val2]]), axis=0)

print(arr)