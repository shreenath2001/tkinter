from tkinter import *

root = Tk()

e = Entry(root, borderwidth=5)
e.pack()
e.insert(0, "Enter your Name")

def click():
    greeting = "Hello " + e.get()
    label = Label(root, text = greeting)
    label.pack()

button = Button(root, text = "Click Me!", command = click)
button.pack()

root.mainloop()