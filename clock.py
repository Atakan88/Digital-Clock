from tkinter import *
from tkinter.ttk import *
from time import strftime
import datetime

root = Tk()
root.resizable(width=False, height=False)


def clock():
    a = strftime("%H:%M:%S ")
    label.config(text=a)
    label.after(1000, clock)


def date():
    b = datetime.datetime.now().strftime("%x")
    label2.config(text=b)


root.title("Digital Clock")
label = Label(root, font=("Helvetica", 80), background="black", foreground="White")
label2 = Label(
    root,
    font=("Helvetica", 80),
    background="black",
    foreground="White",
    anchor="center",
)
label.grid(row=0, column=0, columnspan=3)
label2.grid(row=1, column=0, columnspan=3, sticky=W + E)
clock()
date()
root.mainloop()
