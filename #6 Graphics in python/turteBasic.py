#Using a turtle graphics
#importing turtle
from turtle import *
 
#declaring Turtle() class in turtle as t 
t = Turtle()
#declaring a Screen class as wn
wn = Screen() 
wn.title("my first turtle graphics window") #title method is used to change  title of screen from screen()
#we can use bgpic method to background  gif image instead of bgcolor
#bgcolor method is used to change back ground color of screen from Screen()
wn.bgcolor("yellow")

#we can change a curser into a turtle shape using shape()
t.shape("turtle")
#changing color of turtle from color method
#First is border color of turtle and Secound is inside color of turtle
t.color("black", "red")

#Changing a speed of a turtle
t.speed(0) # 0 is the fastest speed and 1 is the slowest speed

#hiding a turtle
t.hideturtle()

#coloring a square that we created 
#begin_fill at first
t.begin_fill() #we already given a color red and black in t.color

#moving turtle using forward() method
for i in range(4):
    t.forward(100) #The values are in pixels
    t.left(90)

#making a another square

t.penup() #penup and pendown is used to hide forwed line between the circles
t.forward(200) #using a forward to make a distance between two cicles
t.pendown() 

for i in range(4):
    t.forward(100)
    t.left(90)


#and end_fill at after square coding copleted
t.end_fill()



done() #it is used to hold the screen