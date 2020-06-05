''' Chapter 4.14 '''

import random 

coinFlip = random.randint(0,1)

myGuess = input("Heads (0) or tails (1)?\n")

print "Coin flip:", coinFlip

if(myGuess == 0 and coinFlip == 0):
    print "You guessed correctly. Heads is displayed."
elif(myGuess == 0 and coinFlip == 1):
    print "You guessed incorrectly. Tails is displayed."
elif(myGuess == 1 and coinFlip == 1):
    print "You guessed correctly. Tails is displayed."
elif(myGuess == 1 and coinFlip == 0):
    print "You guessed incorrectly. Heads is displayed."