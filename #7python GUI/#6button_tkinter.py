#using buttons in tkinter
from tkinter import *

tk_instance = Tk()

tk_instance.geometry("850x499")

#making a command for button1
def hello():
    print("hello, tkinter button!")

my_frame = Frame(tk_instance, bg="sky blue", borderwidth=6, relief=SUNKEN)
my_frame.pack(fill=X)

my_l1 =Label(my_frame, text="parameter", background="blue", borderwidth=6, relief=RIDGE, font="comicsansms 18 bold")
my_l1.pack()

my_frame2 = Frame(tk_instance, bg="sky blue", borderwidth=7, relief=SUNKEN)
my_frame2.pack(anchor="nw", fill=Y, side="top")

#making a button and adding it in my_frame2
#adding a command(function logic) to exucute when button get clicked(only add function name)
button1 = Button(my_frame2, text="click here", fg="black", bg="grey", font="comicsansms 12 bold", borderwidth=4, relief=RIDGE, command=hello)
button1.pack()

tk_instance.mainloop()
