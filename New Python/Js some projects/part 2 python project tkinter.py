
import os
import threading
from tkinter import *
import string, random
# Project two is gonna be doing a random password Genarator which also saves the password securely.
# Also adding the input of what the character size should be the user puts.
Variable_1 = 16
Variable_2 = 12 # These are the Variables that the user will press for the size of the password characters.
Variable_3 = 24

def Random(size=8):
    """
    On the first line Chars means strings and adding the strings
    Password is were the chars is bundled up and is created as a random password.
    """
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(chars, k=size))
    textbox.delete("1.0", END)                                  #These are the structure for the random password
    textbox.insert(END, password)
def Savepassword():
    password =textbox.get(1.0, END).strip()
    if password:
        with open("Saved password", "a" ) as file:
            file.write(password + "\n")
w=Tk()
w.title("Random password generator")
w.geometry("700x600")                       #Adding the Tkinter ui now
button=Button(text="Click for a random password(Typically 8 chars)",bg='Green',fg='White', command=Random)
button3=Button(text="Do want 12 characters", bg='yellow',fg='black', command=lambda:Random(Variable_2))
button2=Button(text="Do you want 16 cahracters",bg='orange',fg='black', command=lambda: Random(Variable_1)) #These are the buttons that the user might press
button4=Button(text="Do you want 24 characters", bg='red', fg='black', command=lambda:Random(Variable_3))
savebutton = Button( text="Save password", bg='dark green', fg='white', command=Savepassword)
savebutton.pack(pady=10) 

button4.pack()
button2.pack()
button3.pack() #These are the button packs that creates the buttons to exist
button.pack()
textbox=Text(w, fg='White',bg='black', width=40, height=10)
textbox.pack()
w.mainloop() #End of code