#grid and layout tutorial

from tkinter import *
from turtle import bgcolor

tk_instace = Tk()

tk_instace.geometry("800x400")

#creating a command for a button which will get exit when right info will submited
def getting_pass():

    #get() function is used to get information from particular variable
    #and this function will also create global variables
    var1 = uservalue.get()
    var2 = passvalue.get()

    print(f"The value of username is {var1}")
    print(f"The value of password is {var2}")

    if var1 == "pranav" and var2 == "yadav":
        exit()

#making a username and password layout
username = Label(tk_instace, text="Username")
password = Label(tk_instace, text="Password")

#using grid instead of pack and giving row and column
username.grid()
password.grid(row=1)

#types of variables in tkinter
# BooleanVar, DoubleVar, IntVar, StringVar

#declaring the user and password variable as string
uservalue = StringVar()
passvalue = StringVar()

#declaring Entry input at user and password
userentry = Entry(tk_instace, textvariable=uservalue, background="grey", borderwidth=4, relief=RIDGE, fg="yellow")
passentry = Entry(tk_instace, textvariable=passvalue, background="grey", borderwidth=4, relief=RIDGE, fg="yellow")

#griding userentry and passentry at corner
userentry.grid(row=0, column=1,)
passentry.grid(row=1, column=1)

#making a button for submit the iforamtion and giving command and adding grid with code in one line
Button(tk_instace, text="submit", command=getting_pass, bg="grey", borderwidth=3, relief=RAISED, font="comicsansms 9 bold", fg="purple").grid(column=1)


tk_instace.mainloop()