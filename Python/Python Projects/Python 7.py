import random
from tkinter import *

player_score = 0
computer_score = 0

def play(user_choice):
    global player_score, computer_score

    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)

    result = ""
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        result = "You win!"
    else:
        result = "You lose!"

    if result == "You win!":
        player_score += 1
    elif result == "You lose!":
        computer_score += 1

    score_label.config(text=f"Player: {player_score}  Computer: {computer_score}")
    result_label.config(text=f"You chose {user_choice}\nComputer chose {computer_choice}\n{result}")

def reset():
    result_label.config(text="")
    score_label.config(text="Player: 0  Computer: 0")
    global player_score, computer_score
    player_score = 0
    computer_score = 0

w = Tk()
w.title("Rock Paper Scissors Game")
w.geometry("400x300")
w.config(bg="teal")

Label(w, text="Choose your move!!!", font=("Arial", 14)).pack(pady=10)

Button(w, text="Rock", command=lambda: play('rock'), bg="Black", fg="White").pack()
Button(w, text="Paper", command=lambda: play('paper'), bg="White").pack()
Button(w, text="Scissors", command=lambda: play('scissors'), bg="blue").pack()

result_label = Label(w, text="", fg="blue")
result_label.pack(pady=20)

score_label = Label(w, text="Player: 0  Computer: 0", fg="white", bg="teal")
score_label.pack()

Button(w, text="Reset", command=reset, bg="red", fg="white").pack(pady=5)

w.mainloop()