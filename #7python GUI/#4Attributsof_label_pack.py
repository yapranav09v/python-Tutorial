from tkinter import *
from tkinter.font import BOLD

user_root = Tk()

#window size
user_root.geometry("944x499")

#minimum window size
user_root.minsize(499,299)

#changing title of window
user_root.title("my GUI with pranav")

#important label option
#text = adds a text
#bd = Background
#fg = foreground
#font = sets the font
    #method1--> font=("comicsansms", 11, "bold")
    #method2--> font="comincsansms 11 bold"
#padx = x _Padding
#pady = y _Padding
#relief = border styling = SUNKEN, RAISED, GROOVE, RIDGE

#creating a two lines of text and adding background and foreground(text colour) color to it and adding padding and giving font and font size
text_label = Label(text="the full form of gui is graphical user interface\nit is used to make attractice programs",
bg="yellow",fg="red",padx=44,pady=44,font=("comicsansms", 11, "bold"),borderwidth=3,relief=RIDGE)

next_label = Label(text="the full form of gui is graphical user interface\nit is used to make attractice programs",
bg="red",fg="yellow",padx=88,pady=88,font="comicsansms 30 italic",borderwidth=3,relief=GROOVE)

#important pack options
#anchor = we can change it by sounth, north in top
#anchor="ne"
#side = top, bottom, left, right

#moving text_label to the North-East at top it will fill at y
text_label.pack(anchor="ne",fill=Y, padx=85, pady=59)
#moving next_label to the South-East but it will not go at bottom(because its always at top/midle by default) without specifing side's
#using fill it will fill at x when we pull a window at x
next_label.pack(side=BOTTOM, anchor="se", fill=X)
user_root.mainloop()