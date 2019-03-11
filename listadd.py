import numpy as np

height  = [ 2,3,4,5 ]
wieght  = [ 6,7,8,10 ] 

np_height   = np.array(height)
np_wieight  = np.array(wieght)


print(np_height)

#Numpy type.
print(type(np_height))

#Calculating BMI
bmi = (np_wieight) / (np_height ** 2)

print(bmi)
