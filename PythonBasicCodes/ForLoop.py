for item in 'python':
    print(item) # For each loop

for item1 in ['vidya', 'pavani', 'chethu']:
    print(item1)
for item3 in range(20):
    print(item3)

for item3 in range(5, 10):
    print(item3)

for item3 in range(1, 6, 2): # it will give u a Steps forward of a number
    print(item3)

for item3 in range(1, 6, 1):
    print(item3)
#-------------------------------Example------------------
prices = [10, 20, 30]
total = 0
for price in prices:
        total += price
print(f"Total : {total}")


#-------------Nested loops in pyhton------------------
for x in range(4):
    print(x)

#------------------------------
for x in range(4):
    for y in range(3):
        print(f"({x}, {y})")
#--------------------------------------
numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    print('X ' * x_count)
# or
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'X '
    print(output)

#--Find MAx number in list------------------------
numbers = [3, 6, 2, 8, 4, 10, 19]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

#----------- 2D List in Python-------------------
'''
  [
    123
    456
    789
 ]
'''

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[2][2])

for row in matrix:
    print(row)
    for item in row:
      print(item)

#-----------------print unique number in list-----------------
numbers = [0,2,2,6,4,3,4,1,6,7]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
        uniques.sort()
print(uniques)
