time = int(input("How long would you like the timer to run for?(seconds): "))

while time >= 0:
    print(time, "Seconds remaining")
    time -= 1
    

print("Timer has reached 0!!")