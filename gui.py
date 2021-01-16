from tkinter import *
import pandas as pd

root = Tk()
root.geometry('400x200+100+100')
root.config(bg="powderblue")
root.title('Machines-2 Project')
root.iconbitmap('favicon.ico')

label1 = Label(root, text = "Input 1: ")
label2 = Label(root, text = "Input 2: ")
label3 = Label(root, text = "Input 3: ")
label4 = Label(root, text = "Input 4: ")
label5 = Label(root, text = "Input 5: ")
label6 = Label(root, text = "Input 6: ")

e1 = Entry(root, borderwidth=3)
e2 = Entry(root, borderwidth=3)
e3 = Entry(root, borderwidth=3)
e4 = Entry(root, borderwidth=3)
e5 = Entry(root, borderwidth=3)
e6 = Entry(root, borderwidth=3)

label1.grid(row=0, column=0)
label2.grid(row=1, column=0)
label3.grid(row=2, column=0)
label4.grid(row=3, column=0)
label5.grid(row=4, column=0)
label6.grid(row=5, column=0)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=4, column=1)
e6.grid(row=5, column=1)

def submit():
    if(((e1.get()!="" and e2.get()!="") and (e3.get()!="" and e4.get()!="")) and (e5.get()!="" and e6.get()!="")):
        l = []
        l.extend([e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get()])
        df = pd.DataFrame(l)
        df.to_csv('value.csv')
        label = Label(root, text="Your values are saved!")
        label.grid(row=7, column=0)
        label.after(1500, label.destroy)
        print("Value 1: ", e1.get())
        print("Value 2: ", e2.get())
        print("Value 3: ", e3.get())
        print("Value 4: ", e4.get())
        print("Value 5: ", e5.get())
        print("Value 6: ", e6.get())
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)
        e6.delete(0, END)
    else:
        label = Label(root, text="Please fill in all values")
        label.grid(row=7, column=0)
        label.after(1500, label.destroy)

submit = Button(root, text="Submit", padx=10, pady=10, command=submit)
submit.grid(row = 6, column = 1)



root.mainloop()