from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("200x200")

def msg():

    messagebox.askretrycancel("Alert","Stop! Virus found")

button = Button(root,text="Scan for Virus", command=msg)
button.pack()

root.mainloop()
