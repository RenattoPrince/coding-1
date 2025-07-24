import random

secret_number = random.randint(1, 10)

Guess = []
Guess_results = []
print("Welcome to a number guessing game!")
print("Think of an number between 1 and 10.")
print("Try to guess it in three tries.")
print("The game will show you hints after each guess.")
while True:
    guess = input("Enter your guess: ")
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue
    guess = int(guess)
    
    if guess < 1 or guess > 10:
        print("Your guess is out of range. Please try again.")
        continue
    
    Guess.append(guess)
    
    if guess < secret_number:
        Guess_results.append("Too low!")
        print("Too low!")
    elif guess > secret_number:
        Guess_results.append("Too high!")
        print("Too high!")
    else:
        Guess_results.append("Correct!")
        print("Nice you have geussed the number!!!")
        break
    
    if len(Guess) == 3:
        print(f"You've used all your tries. The secret number was {secret_number}.")
        break