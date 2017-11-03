import random
round = 0
humanScore = 0
compScore = 0
print("Let's play rock, paper, scissors. \n Use the numpad to play. \n Use \"1\" for rock, \"2\" for paper and \"3\" for scissors")
print("How many rounds would you like to play?")
rounds = int(input())
while round < rounds:
    computer = random.randint(1,3)
    print("Rock... \n paper... \n scissors.. shoot!")
    number = int(input())
    if (number != 1) and (number != 2) and (number != 3):
        print("Input error, only use 1, 2 or 3, try again.")
    elif computer == number:
        print("Tie! Let's try again.")
    elif computer == 1 and number == 2:
        print("Paper covers rock, you win.")
        humanScore += 1
        round += 1
    elif computer == 2 and number == 3:
        print("Scissors cuts paper, you win.")
        humanScore += 1
        round += 1
    elif computer == 3 and number == 1:
        print("Rock crushes scissors, you win.")
        humanScore += 1
        round += 1
    elif computer == 2 and number == 1:
        print("Paper covers rock, you lose.")
        compScore += 1
        round += 1
    elif computer == 3 and number == 2:
        print("Scissors cuts paper, you lose.")
        compScore += 1
        round += 1
    elif computer == 1 and number == 3:
        print("Rock crushes scissors, you lose.")
        compScore += 1
        round += 1
    else:
        print("Error, resetting")
        break

if compScore >> humanScore:
    print("You lost! The score is " + str(compScore) + " to " + str(humanScore) +".")
elif humanScore >> compScore:
    print("You won! The score is " + str(humanScore) + " to " + str(compScore) +".")
else:
    print("It was a tie!")

