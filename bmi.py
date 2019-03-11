import numpy as np

height  = [ 2,3,4,5 ]
wieght  = [ 6,7,8,10 ] 

np_height   = np.array(height)
np_wieight  = np.array(wieght)

#Calculating BMI
bmi = (np_wieight) / (np_height * np_height)

print(bmi)