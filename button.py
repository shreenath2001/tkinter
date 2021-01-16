from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text = "You Clicked!!")
    myLabel.pack()

myButton = Button(root, text = "Click Me!", fg = "white", bg = "black", padx = 20, pady = 20, command=myClick)
myButton.pack()

root.mainloop()