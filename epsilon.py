x = 36
epsilon = 1
guess = 0.0
increment = 1
num_guesses = 0

while (abs(guess**2 - x) >= epsilon and guess**2 <= x):
    guess += increment
    num_guesses += 1

print(num_guesses, "guesses")
print(guess," is close to being the sqrt of", x)

