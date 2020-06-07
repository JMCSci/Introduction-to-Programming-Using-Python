''' Chapter 5.38 '''

import time

seconds = int(input("Enter the number of seconds: "))

while(seconds > 0):
    time.sleep(1);
    seconds = seconds - 1;
    if(seconds > 1):
        print(seconds, "seconds remaining");
    elif(seconds == 1):
        print(seconds, "second remaining");
    else:
        print("Stopped");