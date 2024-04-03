from tkinter import *

root = Tk()
root.title("Simple Calculator")

# Entry widget to display input and results
input_field = Entry(root, width=35, borderwidth=5)
input_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


# Functions for calculator operations

# Function to handle button clicks
def click(number):
    current = input_field.get()
    input_field.delete(0, END)
    input_field.insert(0, str(current) + str(number))


# Function to handle addition operation
def add():
    global fnum
    fnum = int(input_field.get())
    input_field.delete(0, END)
    global math
    math = "addition"


# Function to handle subtraction operation
def sub():
    global fnum
    fnum = int(input_field.get())
    input_field.delete(0, END)
    global math
    math = "subtraction"


# Function to handle multiplication operation
def mul():
    global fnum
    fnum = int(input_field.get())
    input_field.delete(0, END)
    global math
    math = "multiplication"


# Function to handle division operation
def div():
    global fnum
    fnum = int(input_field.get())
    input_field.delete(0, END)
    global math
    math = "division"


# Function to clear the input field
def clear():
    input_field.delete(0, END)


# Function to calculate and display the result
def equal():
    snum = int(input_field.get())
    input_field.delete(0, END)
    if math == "addition":
        input_field.insert(0, fnum + snum)
    elif math == "subtraction":
        input_field.insert(0, fnum - snum)
    elif math == "multiplication":
        input_field.insert(0, fnum * snum)
    elif math == "division":
        input_field.insert(0, fnum / snum)


# Define buttons for numbers, operators, and clear
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: click(0))

button_add = Button(root, text="+", padx=39, pady=20, command=add)
button_equal = Button(root, text="=", padx=91, pady=20, command=equal)
button_clear = Button(root, text="Clear", padx=79, pady=20, command=clear)

button_sub = Button(root, text="-", padx=41, pady=20, command=sub)
button_mul = Button(root, text="*", padx=40, pady=20, command=mul)
button_div = Button(root, text="/", padx=41, pady=20, command=div)

# Place buttons on the grid
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)

button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

button_sub.grid(row=6, column=0)
button_mul.grid(row=6, column=1)
button_div.grid(row=6, column=2)

root.mainloop()
