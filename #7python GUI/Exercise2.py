from tkinter import *

from_instance = Tk()

from_instance.geometry("1200x700")

frame_name = Frame(from_instance, bg="cyan",borderwidth=5, relief=SUNKEN)
frame_name.pack(side=TOP, fill=X)

label_name = Label(frame_name, text="My Inforamtion from tkinter", fg="magenta", borderwidth=3, relief=GROOVE, font="comicsansms 12 bold")
label_name.pack()


from_instance.mainloop()