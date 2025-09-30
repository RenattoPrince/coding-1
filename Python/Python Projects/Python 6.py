import random
import string

from tkinter import *
w=Tk()
w.title("Intro to Tkinter")
w.geometry("50x40")

def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")

    # Define character pools
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Ensure password has at least one of each type
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols),
        random.choice(letters + digits + symbols)
    ]

    # Fill the rest of the password length
    password += random.choices(letters + digits + symbols, k=length - 4)
    random.shuffle(password)

    return ''.join(password)

# Example usage
print("Your random password:", generate_password(16))