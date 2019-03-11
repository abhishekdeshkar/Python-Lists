import numpy as np
from scipy import stats

arr = np.empty((0,1), int)

for i in range(4):
    arr = np.append(arr,np.random.randint(low=1, high=100, size=1)[0])


#Mean
print("Mean is =",np.mean(arr))

#Mod
print("Mod is =",stats.mode(arr)[0][0])

#Median
print("Median is =",np.median(arr))

#Standard deviation.
print("Standard deviation is = ",np.std(arr,axis=0))



