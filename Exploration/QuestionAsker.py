budget = int(input("How much is your budget? "))
carType = input("What type of car do you like (cabrio, coupe etc.)? ") 
age = int(input("How old are you "))
isFirstcar = None
if (input("Have you owned any cars befor? ").lower() == "no"):
    isFirstcar = True
    print ("so ist your first car")
else:
    isFirstcar = False
    print ("so its not your first car")
