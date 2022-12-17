#learing about canvas widget
from tkinter import *
can_root = Tk()
can_root.title("canvas")

#making height and width variable
Canvas_width = 800
Canvas_height = 400
#using f string
can_root.geometry(f"{Canvas_width}x{Canvas_height}")

#using Canvas function and giving tk height and width to it
can_canvas = Canvas(can_root, width=Canvas_width, height=Canvas_height)
can_canvas.pack()

#making line using canvas function
#the line goes from x1, y1 to x2, y2
can_canvas.create_line(50, 200, 200, 50, fill="red")
can_canvas.create_line(60, 100, 100, 60, fill="green")

#creating rectangle
#to create a rectangle give top left and bottom right cordinate
can_canvas.create_rectangle(3, 5, 700, 300, fill="blue")

#creating text
can_canvas.create_text(200, 200, text="pranav")

#creating oval(earth shaped circle)
#giving top left and botton right cordinate
can_canvas.create_oval(200, 233, 344, 333)

can_root.mainloop()