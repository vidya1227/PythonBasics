bIsMale = True
bIsTall = False

if bIsMale and bIsTall:
    print("You are a male or tall or both")
elif bIsMale and not(bIsTall):
     print("You are a short male")
elif not(bIsMale) and bIsTall:
    print("You are not a male but are tall")
else:
    print("You not s male and not a tall")

#If Statements and comparisions ==. != , <=, >=

def maxNum(iNum1, iNum2, iNUm3):
    if iNum1 >= iNum2 and iNum1 >= iNUm3:
        return iNum1
    elif iNum2>=iNum1 and iNum2 >= iNUm3:
        return iNum2
    else:
        return iNUm3

print(maxNum(3, 4, 5))
