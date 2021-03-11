class Dog:
    def walk(self):
        print('walk')

class Cat:
    def walk(self):
        print('walk')

'''
Observe the above 2 class have same method and same 
functions are repeated to avoid these repeatations in methods , we wil use the inheritance.
Inheritance is when a class inherits or acquires the property of another class , 
this is known as in Inheritance 
'''

#-----------Inheritance-------------------
class animal:
    def walk(self):
        print('walk')

class Dog(animal):
    def bark(self):
        print('bark')


class Cat(animal):
    def be_annoying(self):
        print('annoying')

class Elephant(animal):
    pass

dog1 = Dog()
dog1.walk()
dog1.bark()

cat1= Cat()
cat1.be_annoying()
cat1.walk()

elephant1 = Elephant()
elephant1.walk()