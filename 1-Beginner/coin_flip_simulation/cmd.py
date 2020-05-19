# coin flip
import random

def counter(n):
    head = 0
    tails = 0
    while n > 0:
        choice = random.randint(1,2)
        if choice == 1:
            head += 1
        if choice == 2:
            tails += 1
        n -= 1
    print("Head",head)
    print("Tail",tails)
    return head,tails

try:
    number_of_rotations = int(input("ENTER THE NUMBER_OF_ROTATION\n"))
    print(counter(number_of_rotations))
except ValueError or NameError:
    print("Wrong Value!\nRestart")


