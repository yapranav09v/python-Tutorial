#making a simple gui to say ready

from tkinter import *

simple_root = Tk()

simple_root.minsize(500,400)
simple_root.maxsize(500,400)

ready_text = Label(text="Ready", bg="blue", fg="orange", font="comicsansms 14 bold", borderwidth=3, relief=RIDGE)

ready_text.pack(side="bottom", fill=X)
simple_root.mainloop()
