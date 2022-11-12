#making a travel form in python tkinter gui
#using checkbox
from tkinter import *
import time

#declairing the screen tk and screen size
travel_root = Tk()
travel_root.geometry("420x344")

#writting a function to add data to file and show some text after submitting data
def getvels():
    print("submitting form...")
    
    print(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), emergencyvalue.get(), pymentvalue.get(), foodservisevalue.get()}")
    #adding a traavel agent data to the file
    #using append(a) mode isteda of write(w) mode because w mode rewriting our data
    with open("records.txt", "a") as f:
        f.write(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), emergencyvalue.get(), pymentvalue.get(), foodservisevalue.get()}\n")
       

    #deleting entere text in entry
    nameentry.delete(0, END)
    phoneentry.delete(0, END)
    genderentry.delete(0, END)
    emergencyentry.delete(0, END)
    pymententry.delete(0, END)
    foodentry.delete(0, END)

    Label(text="Succefull submited", fg="green", font="calibri 12 bold").grid(row=8, column=3)
    time.sleep(0.5)
    print("Succefully submited")

#writing a exit function
def exit_fun():
    exit()

#giving the trevel form heading
Label(travel_root, text="Welcome To Pranav Travels", font="comicsansms 14 bold", fg="red", pady=14).grid(row=0, column=3)

#making basic information label
name = Label(travel_root, text="Name")
phone = Label(travel_root, text="phone")
gender = Label(travel_root, text="Gender")
emergency = Label(travel_root, text="Emergency")
pyment = Label(travel_root, text="Pyment Mode")

#intilizing basic iformation label in grid row and column
name.grid(row=1 , column =2)
phone.grid(row=2 , column =2)
gender.grid(row=3 , column =2)
emergency.grid(row=4 , column =2)
pyment.grid(row=5 , column =2)

#declaring the vairables for basic information and adding new foodservice variable at last
namevalue = StringVar()
phonevalue = StringVar() 
gendervalue = StringVar()
emergencyvalue = StringVar()
pymentvalue = StringVar()
foodservisevalue = IntVar()

#making entry(inpute)
nameentry = Entry(travel_root, textvariable=namevalue )
phoneentry = Entry(travel_root, textvariable=phonevalue )
genderentry = Entry(travel_root, textvariable=gendervalue )
emergencyentry = Entry(travel_root, textvariable=emergencyvalue )
pymententry = Entry(travel_root, textvariable=pymentvalue )
foodentry = Entry(travel_root, textvariable=foodservisevalue )

nameentry.grid(row=1 , column =3)
phoneentry.grid(row=2 , column =3)
genderentry.grid(row=3 , column =3)
emergencyentry.grid(row=4 , column =3)
pymententry.grid(row=5 , column =3)

#ading chekbox
#using a checkbutton()
#we give variable as its variable input of entry
foodservise = Checkbutton(text="Want to prebook Your Meals?", variable=foodservisevalue, pady=8)
foodservise.grid(row=6, column=3)

#assinging a button and giving it command
button = Button(text="Submit to pranav travels", fg="blue",bg="silver", command=getvels)
button.grid(row=7, column=3)
Label(text="").grid(row=9, column=3)
Button(text="Exit", fg="red", bg="grey", font="calibri 15 bold",width=9,relief=RIDGE, borderwidth=3, command=exit_fun).grid(row=10, column=3)


travel_root.mainloop()

