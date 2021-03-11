class Greetings:
    def __init__(self, name1, name2): # intialise method is constructor in python
        self.name1 = name1
        self.name2 = name2

    def Morn(self):
        print('Good Morning')

    def noon(self):
        print('Good afetrnoon')

greet1 = Greetings('vidya', 'shri')
print(greet1.name2)
greet1.name1 =10
print(greet1.name1)
greet1.name1 = 'vidya'
print(greet1.name1)

#----------------------Example 2------------------------------
class Person:
    def __init__(self, name):# constructor
        self.name= name


    def talk(self):
        print(f"Hi I'm {self.name}")


vidya = Person('Boss')
print(vidya.name)
vidya.talk()

Ram = Person('Ram krishna')
Ram.talk()