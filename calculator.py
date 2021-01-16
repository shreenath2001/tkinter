from tkinter import *
from typing import Match

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row = 0, column = 0, columnspan=3, padx=10, pady=10)

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_num = e.get()
    global f_num
    global math 
    math = "addition" 
    f_num = float(first_num)
    e.delete(0, END)

def button_subtract():
    first_num = e.get()
    global f_num
    global math 
    math = "subtract" 
    f_num = float(first_num)
    e.delete(0, END)

def button_multiply():
    first_num = e.get()
    global f_num
    global math 
    math = "multiply" 
    f_num = float(first_num)
    e.delete(0, END)

def button_divide():
    first_num = e.get()
    global f_num
    global math 
    math = "divide" 
    f_num = float(first_num)
    e.delete(0, END)

def button_equal():
    second_num = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num+int(second_num))
    if math == "subtract":
        e.insert(0, f_num-int(second_num))
    if math == "multiply":
        e.insert(0, f_num*int(second_num))
    if math == "divide":
        e.insert(0, f_num/int(second_num))

button_1 = Button(root, text="1", command=lambda:button_click(1), pady=20, padx=40)
button_2 = Button(root, text="2", command=lambda:button_click(2), pady=20, padx=40)
button_3 = Button(root, text="3", command=lambda:button_click(3), pady=20, padx=40)
button_4 = Button(root, text="4", command=lambda:button_click(4), pady=20, padx=40)
button_5 = Button(root, text="5", command=lambda:button_click(5), pady=20, padx=40)
button_6 = Button(root, text="6", command=lambda:button_click(6), pady=20, padx=40)
button_7 = Button(root, text="7", command=lambda:button_click(7), pady=20, padx=40)
button_8 = Button(root, text="8", command=lambda:button_click(8), pady=20, padx=40)
button_9 = Button(root, text="9", command=lambda:button_click(9), pady=20, padx=40)
button_0 = Button(root, text="0", command=lambda:button_click(0), pady=20, padx=40)
button_add = Button(root, text="+", command=button_add, pady=20, padx=39)
button_equal = Button(root, text="=", command=button_equal, pady=20, padx=90)
button_clear = Button(root, text="Clear", command=button_clear, pady=20, padx=79)
button_subtract = Button(root, text="-", command=button_subtract, pady=20, padx=41)
button_multiply = Button(root, text="x", command=button_multiply, pady=20, padx=40)
button_divide = Button(root, text="/", command=button_divide, pady=20, padx=40)

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
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=4, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

root.mainloop()