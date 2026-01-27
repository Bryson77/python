x = 36
epsilon = 0.01
guess = 0.0
increment = 0.0001
num_guesses = 0

while (abs(guess**2 - x) >= epsilon):
    guess += increment
    num_guesses += 1
print(num_guesses, "guesses")
print(guess," is close to being the sqrt of", x)

