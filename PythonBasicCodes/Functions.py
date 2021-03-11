def sayHi(sName, iAge):
    print("Hello "+ sName+ " You are! : "+str(iAge))

print("******Start************")
sayHi("vidya", 27)
sayHi("pavani", 12)
print("******End**************")


#-----------------------Functions-parameterized---------------------
def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard')

greet_user("vidya", "Shri")
greet_user("vidya", 1234)

print("Finish")

#------------------Keyword arguments---------------
greet_user("vidya", last_name="shriKEY")
greet_user(last_name="vidya", first_name="qwerty")
