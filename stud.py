import numpy as np

GetData = np.loadtxt('stud.csv', delimiter=',',skiprows=1, unpack=True)

print(GetData)
