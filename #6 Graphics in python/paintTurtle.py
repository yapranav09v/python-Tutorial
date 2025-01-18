#making a paint using a turtle
#importing a turtle
from turtle import *

#declaring a turtle and screen as an object t & wn
t = Turtle()
wn = Screen()

#giving canavas title paint & pencolor red
wn.title("paint")
t.pencolor("blue")
#using -1 for maximum speed
t.speed(-1)

#making a function that used to paint
def paint(x, y):
    #ondrag is used to bind this function to mouse event
    t.ondrag(None) #using none to clear previous one

    #setting heading and calling a towards function on x, y cordinates 
    t.setheading(t.towards(x, y))
    #goto will goto x, y cordinate
    t.goto(x, y)
    #calling a paint inside a onedrag 
    t.ondrag(paint)

#making a function to erase after we finish
#by clicking right click it will clear all screen
def erase(x, y):
    #clear used in erase to clear screen
    t.clear()

#defining main function to calling all all fuction in it
def main():
    wn.listen
    t.ondrag(paint)
    wn.onscreenclick(erase, 3) #  3 is a nothing but right click
    done() #done is used to hold the screen

#it is used to run the screen
main()