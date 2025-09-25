from tkinter import *
from PIL import Image, ImageTk

root =Tk()
root.title("Images")
root.geometry('350x250')

u =Image.open("Disk drive.png")
image=ImageTk.PhotoImage(u)

label =Label(root,image=image, height=200,width=300)
label.pack()

label=Label(root, text="This is how we add images")
label.pack()

root.mainloop()