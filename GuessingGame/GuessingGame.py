from itertools import count
import random
from timeit import repeat
from tkinter import YES
print("Guess the number!")
number = random.randint(1,10)
print("I am thinking of a number from 1 to 10.")
guess = 0
while guess != number:
    guess = int(input("Your guess: "))
    if (guess < number):
        print("Too low!")
    elif (guess > number):
        print("Too high!")
    else:
        print("You got it!")
                       
                                   
                