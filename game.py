from random import randint
import sys
while True:
    try:
        n = int(input("Level: "))
        if (n < 1):
            raise ValueError
        else:
            break
    except ValueError:
        print("Not a number")
g = randint(1, n)
while True:
    try:
        x = int(input("Guess: "))
    except ValueError:
        print("Not a number")
    else:
        if (x < 1):
            continue
        elif (x < g):
            print("Too small!")
        elif (x > g):
            print ("Too large!")
        else:
            sys.exit("Just right!")
