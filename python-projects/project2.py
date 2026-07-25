# project2.py - Guess the Number Game

import random

n = random.randint(1, 100)   # Random number between 1 and 100
a = -1
guesses = 0 

while a != n:
    guesses += 1
    a = int(input("Enter the number: "))
    if a > n:
        print("Too high! Try again.")
    elif a < n:
        print("Too low! Try again.")
    else:
        print("🎉 Correct guess!")

print(f"Total guesses taken: {guesses}")
