from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Tkinter")
root.iconbitmap('favicon.ico')

img = ImageTk.PhotoImage(Image.open('1.jpg'))
label = Label(image=img)
label.pack()

button_quit = Button(root, text = "Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()