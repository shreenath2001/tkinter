from tkinter import *

root = Tk()

myLabel1 = Label(root, text = "hello")
myLabel2 = Label(root, text = "world")
myLabel3 = Label(root, text = "Everyone including me!!")

myLabel1.grid(row = 0, column = 0)
myLabel2.grid(row = 1, column = 5)
myLabel3.grid(row = 1, column = 2)

root.mainloop()