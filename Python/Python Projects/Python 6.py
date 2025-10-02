
from tkinter import *
import random,string

def Random():
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(chars, k=12))
    textbox.delete("1.0", END)
    textbox.insert(END, password)

w=Tk()
w.title("Random password generator")
w.geometry("700x600")
button=Button(text="Click for a random password",bg='orange',fg='black', command=Random)

button.pack()
textbox=Text(w, fg='White',bg='black')
textbox.pack()
w.mainloop()