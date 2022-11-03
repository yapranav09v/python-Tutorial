#displyaing image using tkinter label and photoimage class
from tkinter import *

root = Tk()

#declaring size of window
root.geometry("944x444")

#declaring photo as image file instace
#we need a image always in same folder
#tkinter supports both png and jpg formate
photo = PhotoImage(file="bg.png")
#photo = PhotoImage(file="bc.jpg")

win_name = Label(text="showing image")

#every image is always run as label 
photo_image = Label(image=photo)
photo_image.pack()
win_name.pack()

root.mainloop()