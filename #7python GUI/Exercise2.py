from tkinter import *

from_instance = Tk()

from_instance.geometry("1200x500")
from_instance.maxsize(1200,500)
def name():
    print("pranav")

def father_name():
    print("Ananda")

def sirename():
    print("Yadav")

def favorite_number():
    print(9)

def exit_function():
    exit()

frame_name = Frame(from_instance, bg="cyan",borderwidth=5, relief=SUNKEN)
frame_name.pack(side=TOP, fill=X)

label_name = Label(frame_name, text="My Inforamtion from tkinter", fg="magenta", borderwidth=3, relief=GROOVE, font="comicsansms 12 bold")
label_name.pack()

frame_name2 = Frame(from_instance, bg="magenta", borderwidth=4, relief=RIDGE)
frame_name2.pack(side=TOP, fill=X)

button_firsname = Button(frame_name2, bg="grey", fg="yellow", text="Name", borderwidth=3, relief=GROOVE, command=name, font="comicsansms 12 bold")
button_firsname.pack(anchor="nw",fill=X,pady=35)

button_firsname = Button(frame_name2, bg="grey", fg="yellow", text="father name", borderwidth=3, relief=GROOVE, command=father_name, font="comicsansms 12 bold")
button_firsname.pack(anchor="nw",side=TOP,fill=X,pady=35)

button_firsname = Button(frame_name2, bg="grey", fg="yellow", text="sirename", borderwidth=3, relief=GROOVE, command=sirename, font="comicsansms 12 bold")
button_firsname.pack(anchor="nw",side=TOP,fill=X,pady=35)

button_firsname = Button(frame_name2, bg="grey", fg="yellow", text="favorite number", borderwidth=3, relief=GROOVE, command=favorite_number, font="comicsansms 12 bold")
button_firsname.pack(anchor="nw",side=TOP,fill=X,pady=35)

button_firsname = Button(frame_name2, bg="purple", fg="cyan", text="Exit", borderwidth=3, relief=GROOVE, command=exit_function, font="comicsansms 12 bold")
button_firsname.pack(anchor="nw",side=TOP,fill=X)


from_instance.mainloop()