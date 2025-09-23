from tkinter import *
w=Tk()
w.title("Intro to Tkinter")
w.geometry("500x400")

greetings=Label(text="Hello user",fg='white',bg='orange')
button=Button(text="Click Me",bg='blue',fg='green')
entry=Entry(fg='lightblue',bg='black')

greetings.pack()
button.pack()
entry.pack()

frame = Frame(master=w, relief=RAISED, borderwidth=6)
frame.pack()
label=Label(master=frame,text="frame disply")
label.pack()

textbox=Text(fg='yellow',bg='black')
textbox.pack()

w.mainloop()