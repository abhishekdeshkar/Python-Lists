import numpy as np

height  = [ 2,3,4,5 ]
wieght  = [ 6,7,8,10 ]
age     = [5,10,12,15]

#Creating two dimension array.
two_dime    = np.array([height,wieght],dtype=np.int64)
two_dime    = np.array([height,wieght],dtype=np.float)

#Creating three dimension array.
three_dim   = np.array([height,wieght,age],dtype=np.int64)

#Arranging an array. - Printing from 7 to 100.
arrange_array   = np.arange(7,100)

#1-D Zero matrix
OneDMatrix  = np.zeros(4)

#2-D Zeros Matrix.
TwoDMatrix  = np.zeros((4,4))

#Create an array of evenly spaced values.

# Equally spaced values from 0 to 2 and AND total 9 SAMPLES.
EquallySpacedValue = np.linspace(0,2,9)


#Array with random numbers ranging from 0 to 10.
RandomNumber    = np.random.rand(3,10)

#=========== Uncomment these print statements print individual methods.==========

#print(two_dime)
#print(three_dim)
#print(arrange_array)
#print(OneDMatrix)
#print(TwoDMatrix)
#print(EquallySpacedValue)
print(RandomNumber)