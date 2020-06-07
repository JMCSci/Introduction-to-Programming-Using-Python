''' Chapter 5.40 '''

import random

# Heads = 0, Tails = 1

numberHeads = 0;
numberTails = 0;
i = 0;

while(i < 1000000):
    coinFlip = random.randint(0,1);
    if(coinFlip == 0):
        numberHeads = numberHeads + 1;
    else:
        numberTails = numberTails + 1;
    i = i + 1;
    
print("Heads was flipped", numberHeads, "times")
print("Tails was flipped", numberTails, "times")