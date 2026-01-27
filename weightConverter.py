import math


isRunning = True

while isRunning:
    print("********************************")
    print("Welcome to my Weight Converter program")
    print("********************************")
    print("Here are your options")
    print("1. KG TO POUNDS")
    print("2. POUNDS TO KG")
    print("3. End Program")
    print("********************************")

    option = int(input("1, 2 or 3?: "))
    if option < 0 or option > 3:
        print("You can only choose option 1, 2 or 3")
    elif option == 1:
        userInKG = int(input("Enter the weight in KGs: "))
        CalcPounds = userInKG * 2.20462

        print(f"Your converted weight (KG-POUNDS) is {round(CalcPounds, 1)}LBS")
    elif option == 2:
        userInLBs = int(input("Enter the weight in LBs: "))
        CalcKGs = userInLBs / 2.205
        print(f"Your converted weight (POUNDS-KG) is {round(CalcKGs, 1)}KG")
    elif option == 3:
        print("Thank you! Goodbye")
        print("********************************")
        isRunning = False
    else:
        print("Invalid Option Chosen. Only 1-3 are the valid options!")
        print("********************************")




