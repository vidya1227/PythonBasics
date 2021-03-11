import random

for i in range(3):
    print(random.random())
    print(random.randint(10, 20))

members= ['vidya', 'supritha', 'pavani', 'krutika', 'hema']
leader = random.choice(members)
print(leader)


def roll():
    first = random.randint(1, 6)
    second = random.randint(1,6)
    return  first, second


class Dice:
    pass

dice = Dice()
print(roll())
