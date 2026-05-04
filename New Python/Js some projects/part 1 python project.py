import time
import threading
import os

print("Hello world!")

# This is a comment, it will not be executed by the Python interpreter.
# You can use comments to explain your code, or to temporarily disable a line of code.
one = 1
two = 2

print("One plus two equals", one + two)

Multiply = input("Enter the first number to multply: ")
Multiply2 = input("Enter the second number to multiply: ")
#The two inputs are stored by the computer and the computer will multiply them.
Answer = int(Multiply) * int(Multiply2)
print ("Your answer is: ", Answer)

print("Another multiplication problem!")
print("Now you will be multiplying this time.")
350 == 350
450 == 450

print ("What is 350 multiplied by 450?")
time.sleep(4)
#This code will make the computer to wait for exactly 10 seconds before it will ask the user
inpu67 = input("Enter your answer here: ")

#This code will make the computer to wait for exactly 10 seconds before it will ask the user
if int(inpu67) == 350 * 450:
    print("Correct")
else:    print("Incorrect, the correct answer is", 350 * 450)
# This time the code will now use if and else statements to check if user answer is correct or not.
# The second question will be the same math problems but with division.
time.sleep(1)
print("Now you will be doing some division problems.")
time.sleep(0.75)
print("Ready?")
time.sleep(0.75)
print("What is 100 divided by 25?")
time.sleep(5)
hahah = 100
haha2 = 25
Answer999 = int(hahah) / int(haha2)
answer67 = input("Enter your answer here: ")
if int(67) == Answer999:
    print("Nice Job!")
else:   print("Incorrect, the correct answer is", Answer999)




print("Now you will be doing some multiplication up to 15x")
time.sleep(1)
print("First question, ready?")
time.sleep(0.75)
print("What is 15 multiplied by 15?")
time.sleep(0.5)


timeout_event = threading.Event()

def timeout(seconds: int):
    if not timeout_event.wait(seconds):
        print("\nTime's up! No input received.")
        os._exit(1)  # forcefully end the process

# start timer thread for 5 seconds
threading.Thread(target=timeout, args=(8,), daemon=True).start()

# get input and signal the timer that input arrived
answer_text = input("Enter your answer here: ")
timeout_event.set()

# validate and respond
try:
    if int(answer_text) == 15 * 15:
        print("Correct answer!")
    else:
        print("Incorrect, the correct answer is", 15 * 15)
except ValueError:
    print("Invalid input. The correct answer is", 15 * 15)

#Adding a time.sleep
time.sleep(0.5)
print("Next")
time.sleep(0.25)
print("What is 8X5")


timeout_event = threading.Event()

def timeout(seconds: int):
    if not timeout_event.wait(seconds):
        print("\n Time is up!")
        os._exit(1) #Letraelly end the process

threading.Thread(target=timeout, args=(8,), daemon=True).start()
#The input
answer_text = input("Enter your answer here: ")
timeout_event.set()
# Validate means to check if it is correct.

try:
    if int(answer_text) == 8 * 5:
        print("Correct answer!")
    else:
        print("Incorrect, the answer is", 8 * 5)
except ValueError:
    print("Invalid input. The correct answer is", 8 * 5)


#Adding a time.sleep
time.sleep(0.5)
print("Next one")
time.sleep(0.25)
print("What is 9X12")


timeout_event = threading.Event()

def timeout(seconds: int):
    if not timeout_event.wait(seconds):
        print("\n Time is up!")
        os._exit(1) #Letraelly end the process

threading.Thread(target=timeout, args=(8,), daemon=True).start()
#The input
answer_text = input("Enter your answer here: ")
timeout_event.set()
# Validate means to check if it is correct.

try:
    if int(answer_text) == 12 * 9:
        print("Correct answer!")
    else:
        print("Incorrect, the answer is", 12 * 9)
except ValueError:
    print("Invalid input. The correct answer is", 12 * 9)