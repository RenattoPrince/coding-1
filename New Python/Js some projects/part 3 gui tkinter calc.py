import tkinter as tk
import os               # All the essential imports to import!
import customtkinter as ctk
# This project im going to be starting a calc GUI on Tkinter

root = tk.Tk()
root.title("Simple Calc")
root.geometry("300x432") #Width x Height
def my_function(number):
    current = display.get() # Get what's already there
    display.delete(0, tk.END) # Clear the box
    display.insert(0, str(current) + str(number)) # Put old + new back in


display = tk.Entry(root, width=35, borderwidth=5)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
# the first button
# Example of one button
button_1 = tk.Button(root, text="1", padx=40, pady=20, command= lambda:my_function(1))
button_2 = tk.Button(root, text="2", padx=40, pady=20, command= lambda:my_function(2))
button_3 = tk.Button(root, text="3", padx=40, pady=20, command= lambda:my_function(3))
button_4 = tk.Button(root, text="4", padx=40, pady=20, command= lambda:my_function(4))
button_5 = tk.Button(root, text="5", padx=40, pady=20, command= lambda:my_function(5))  #this is the button commands of what the user input should do and to display the numbers
button_6 = tk.Button(root, text="6", padx=40, pady=20, command= lambda:my_function(6))
button_7 = tk.Button(root, text="7", padx=40, pady=20, command= lambda:my_function(7))
button_8 = tk.Button(root, text="8", padx=40, pady=20, command= lambda:my_function(8))
button_9 = tk.Button(root, text="9", padx=40, pady=20, command= lambda:my_function(9))
button_ZerO = tk.Button(root, text="0", padx=40, pady=20, command= lambda:my_function(0))

button_ZerO.grid(row=4, column=1)
button_9.grid(row=3, column=2)
button_8.grid(row=3, column=1)
button_7.grid(row=3, column=0)
button_6.grid(row=2, column=2)   #The Button Packs to actually display the numbers
button_5.grid(row=2, column=1)
button_4.grid(row=2, column=0)
button_3.grid(row=1, column=2)
button_2.grid(row=1, column=1)
button_1.grid(row=1, column=0)

#Putting the backspace def function
def button_backspace():
    current = display.get()
    # This will takes everything exept the last character
    new_text = current[:-1]

    display.delete(0, tk.END)
    display.insert(0, new_text)

#Actually putting the backspace

button_back = tk.Button(root, text="⌫", padx=40, pady=20, command=button_backspace)
button_back.grid(row=4, column=2)
# "Next putting the CE" next putting the all delete key which is the clear entry
def CE_the_clear_entry():
    display.delete(0, tk.END)
#Next Create the button!!!!!!
button_CE = tk.Button(root, text="CE", padx=40, pady=20, command=CE_the_clear_entry)
# then the button pack!
button_CE.grid(row=4, column=0)
#Now Finally the addition and then more code
button_add = tk.Button(root, text="+", padx=40, pady=20, command=lambda: my_function("+"))
#Then the addition button pack
button_add.grid(row=5, column=2)
#The equal sign
# 1. The Logic (The Function)
def button_equal_logic():
    try:
        # eval() takes the string "1+1" and turns it into the math result 2
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# 2. The UI (The Button) - Move this OUTSIDE the function
# Also changed the text to "=" instead of "+"
my_equal_btn = tk.Button(root, text="=", padx=40, pady=20, command=button_equal_logic)
my_equal_btn.grid(row=6, column=0)
#Next we are doing the multipcation button
Button_multiply = tk.Button(root, text="X", padx=40, pady=20, command=lambda: my_function("*"))
Button_multiply.grid(row=5, column=1)
#Next the Division
button_divide = tk.Button(root, text="÷", padx=40, pady=20, command=lambda: my_function("/"))
button_divide.grid(row=5, column=0)
root.mainloop()