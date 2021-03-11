Guess_Count = 1
while Guess_Count <=  10:
    print(Guess_Count)
    Guess_Count += 1

print("Done with loop")

#*************************************************************************************
j =1
while j <= 5:
    #print(j)
    print('* ' * j)
    j = j + 1

print('Done')

#---------Guess Game --------------
secret_number =9
Guess_Count=0
Guess_limit = 3

while Guess_Count< Guess_limit:
    Guess = int(input('Guess: '))
    Guess_Count += 1
    if Guess == secret_number:
        print(' You Won!')
        break
    #else:
     #   print('Failed!!!!')
else:
    print('Sorry You Failed!')


#---------------Car Game--------------------
command = ""
started = False
#while True: // it will give the loop untill u quit
while command != "quit":
    command = input(">").lower()
    if command == "start":
        if started:
            print("car is already started!")
        else:
            started = True
            print("Car started.........")
    elif command == "stop":
        if not started:
            print("car is already stopped!")
        else:
            started = False
            print("car stopped.")
    elif command == "help":
        print("""
Start - to start the car 
stop - to stop the car
quit -to quit
        """)
    elif command == "quit":
        break
    else:
        print("Sorry I don't understand that command...")
