'''This contains two functions: craps and testCraps.
craps is a function that mimics a game of craps and returns
a 1 for win or a 0 for lose. The print statements that print
out the result of the craps game have been commented out for
the purposes of using the testCraps function. The testCraps
function takes an input n and plays n number of craps games
and returns the win percentage for all games played.'''

def craps():
    import random          #import random library
    diceOne = random.randint(1,6)     #random integer 1 to 6 for 1st die
    diceTwo = random.randint(1,6)     #random integer 1 to 6 for 2nd die
    initialRoll = diceOne + diceTwo   #add two die together
    if (initialRoll == 7) or (initialRoll == 11):   #check if roll is 7 or 11
        result = 1       #result is win
        #print(result)
        return result
    elif (initialRoll == 2) or (initialRoll == 3) or (initialRoll == 6):     #check if roll is 2, 3 or 6
        result = 0     #result is lose
        #print(result)
        return result
    else:
        while True:
            diceOne = random.randint(1,6)    #random integer 1 to 6 for 1st die
            diceTwo = random.randint(1,6)    #random integer 1 to 6 for 2nd die
            newRoll = diceOne + diceTwo      #add to two die together
            if newRoll == 7:    #check if roll is 7
                result = 0      #result is lose
                #print(result)
                return result
                break
            elif newRoll == initialRoll:    #check if new roll is equal to the initial roll
                result = 1     #result is win
                #print(result)
                return result
                break
            else:
                continue


def testCraps(n):
    rounds = 0     #initialize the round
    wins = 0       #initialize the wins
    while rounds < n:     #number of rounds is based on the value n that is passed
        result = craps()     #call the craps function
        rounds += 1     #increment the round
        if result == 1:    #check if the result was win
            wins += 1      #incremenet wins
    winPercent = wins/n     #find the win percentage
    print(winPercent)       #print the win percentage
            
        
testCraps(20)       #call the testCraps function with input n for number of rounds
