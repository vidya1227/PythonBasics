from math import *

#Variables in python-------------------------
iAge = 50 # int
sName = "Vidya1" # String
sName = "Vidya"
rating = 4.9 # float
name = True
sname = False


print(sName)

bIsMal= True # boolean
bIsFemale= False

#---------Print statements in python---------------
first = 'vidya'
last = 'shri'
print(first + ' [' + last + '] is a coder')
msg1 = f'{first} [{last}] is a coder for test'
print(msg1)

#-----------Working on Print msg in python-------------------
cource1 = "Python's Cpource for Begineers"
print(cource1)

cource2 = 'Python Cpource for "Begineers"'
another = cource1[:]
print(another)
print(cource2)
print(cource1[0:3])
print(cource1[0:])# all will print in string
print(cource1[:5])# end index is 5
name = 'Jennifer'
print(name[1:-1])

msgEmail = '''
Hi John,

Here,! is our "First" email to 'you'.

Thank you,
The support team.
'''
print(msgEmail)


#-----------Working with Strings------------------------

print("Matryx\nsoft")
print("Matryx\"soft1")
sString = "MatryxSoft"

print(sString + " is cool")
print(sString.upper()) # Lower also
print(sString.isupper())
print(sString.upper().isupper())
print(len(sString))
print(sString[0])
print(sString.index("S"))
print(sString.replace("Soft", "Tech"))
cource3 = 'Python for Beginners'
print(cource3.find('B'))

#Sequence of charecter in string
print('Python' in cource3)




#----------Working With numbers-- and math functions import (from import math *)-----------------

print(2)
print(-2.02154)
print(3+3.4)
print(3*(4+5))#3*4+5
print(10%3)#give u the remindres
iNUm = 5
print(iNUm)

#print(iNUm+ " My Fav num")#Error will come
print(str(iNUm)+ " My Fav num")
print(pow(3, 2))# it will give you square of numbers
print(max(4, 6))
print(min(4, 6))
print(round(3.7))
print(floor(3.7))
print(ceil(3.7))
print(sqrt(36))

x = 2.9
print(abs(-2.9))


#------------Operators in PYTHON---------------------
print(10//3)
#Try also (10+3), (10-3), (10/3), (10%3), (10 ** 3) it will indicate power
x=10
x=x+3
x+= 3
x -+ 3
print(x)
 # Order of Operations are
# xponentiation 2 ** 3,
# Multiplication or division,
# addition or subtraction


