import random
number = random.randint(1,10)
print("I am thinking of a number between 1 and 10")

for guesses in range(1,5):
    print("Take a guess.")
    guess = int(input())
    if guess < number:
        print("Too low.")
    elif guess > number:
        print("Too high.")
    else:
        break

if guess == number:
    print("Correct, it took " + str(guesses) + " guesses.")
else:
    print("Nope. The correct answer is " + str(number))
