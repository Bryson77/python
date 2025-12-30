isRunning = True
currentBal = 0.00

while isRunning:
    print("*********************")
    print("Good day! Welcome to B's Bank")
    print("1. View Current balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    print("*********************")

    option = int(input("Choose an option: "))
    if option >= 4 or option < 0:
        print("Invalid Option Chosen")
        break
    elif option == 1:
        print("You currently have: " , currentBal)
    elif option == 2:
        depositAmnt = float(input("How much would you like to deposit?: "))
        if depositAmnt < 0:
            print("You cannot enter an amount that is negative or 0")
        else:
            currentBal = currentBal + depositAmnt
            print("Deposit was successful, your current balance is: R " , currentBal)
    elif option == 3:
        withdrawalAmnt = float(input("How much would you like to withdraw?: "))
        if withdrawalAmnt > currentBal or withdrawalAmnt <= 0:
            print("You cannot withdraw more than what you have in your account/ withdraw an amount less than 0")
        else:
            currentBal = currentBal - withdrawalAmnt
            print("Withdrawal was successful, your current balance is: R" , currentBal)
    elif option == 4:
        print("Thank you, Goodbye!")
        isRunning = False
print("done")