#frames in tkinter
from tkinter import *
from turtle import left

at_root = Tk()

at_root.geometry("1100x700")

#making a small text size frame the attibutes only applay on frame
f1 = Frame(at_root, bg="grey", borderwidth=6,relief=SUNKEN)
f1.pack(side=LEFT,fill=Y)

#making a secound frame
f2 = Frame(at_root, bg = "grey", borderwidth=6,relief=SUNKEN)
f2.pack(side=TOP, fill=X)

#making a text label in frame, attributes only applay on text
l1 = Label(f1, text="my GUI of tkinter", fg="yellow", borderwidth=6, relief=SUNKEN,pady=42,bg="blue",font="algeriun 15 bold")
l1.pack( fill=Y)

#making label in f1
l1_1 =Label(f1, text="Gui files of tkinter",borderwidth=3,relief=RIDGE,font="comicsansms 12 bold",bg='grey',fg="black")
l1_1.pack(padx=42)

#making secound label
l2 = Label(f2, text="Heading of GUI", fg='red', borderwidth=6, relief=SUNKEN, font="comicsansms 12 bold")
l2.pack(padx=142,fill=X)


at_root.mainloop()