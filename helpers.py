TestList = [ 1,2,3,4,5,4,10,10 ]

#Remove first occorance
TestList.remove(4)
print(TestList)

#Reverse
TestList.reverse()
print(TestList)

#insert method.
TestList.insert(0,11)
print(TestList)

#Sorting.

#Ascending
TestList.sort()
#Descending
TestList.sort(reverse=True)
print(TestList)

#List length
print(len(TestList))

#Count element
print(TestList.count(10))

#Index - 
print(TestList.index(2))

