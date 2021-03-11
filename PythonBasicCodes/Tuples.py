#The tuples ype of data structures or containers where we can store different values in tuples
#Tuples are very similar to the lists!
'''
Tuples are similar to list but we can't modify them , cant add new item,  or existing item
tiple is totaly immutable.

'''

tuples = (1, 2, 3)
#print(tuples.count(1))
#print(tuples.index())

#----------------------------------
coordinaters = (4, 5)
print(coordinaters[0])

#coordinaters[1]=10 # we cant assing a value for tuples -->'tuple' object does not support item assignment
print(coordinaters[1])

#----------------------
lsCoordinators = [(4, 5), (6,7), (80, 34)]

#---------------------------------------------
coOrdinators = (1, 2, 3)
'''
x = coOrdinators[0]
y = coOrdinators[1]
z = coOrdinators[2]
print(x*y*z)
'''
#-------------------------Unpacking in python---------------
x, y, z = coOrdinators
print(x*y*z)
