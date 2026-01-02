def balance(currBal):
    print(f"Balance: R{currBal:.2f}")

def print_menu():
    print("*********************")
    print("Good day! Welcome to B's Bank")
    print("1. View Current balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    print("*********************")

def deposit(currBal):
    depositedAmnt = float(input("How much would you like to deposit: "))
    if depositedAmnt <= 0:
        print("You cannot deposit an amount that is equal or less than 0")
    else:
        currBal += depositedAmnt
        print("Deposit was successful")
    return currBal

def withdrawal(currBal):
    withdrawalAmnt = float(input("How much would you like to withdraw: "))
    if withdrawalAmnt > currBal:
        print("Insufficient Balance")
    else:
        currBal -= withdrawalAmnt
        print("Withdrawal was successful.")
    return currBal

def exit_program():
    global isRunning
    print("Thank you! Goodbye")
    isRunning = False

# Starting balance
currBal = 0.0
isRunning = True

while isRunning:
    print_menu()
    option = int(input("Choose an option: "))
    
    if option > 4 or option <= 0:
        print("Invalid option")
    else:
        if option == 1:
            balance(currBal)
        elif option == 2:
            currBal = deposit(currBal)
        elif option == 3:
            currBal = withdrawal(currBal)
        elif option == 4:
            exit_program()
