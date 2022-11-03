#importing tkinter for python gui
from cProfile import label
from tkinter import * 

#taking a instance from a gui class
main_root = Tk()


#windows api will handle tkinter gui also with cross platform
#this used to set size of a window
#we will write in widthxheight
main_root.geometry("634x434")
                                                                #logic always coded between Tk and mainloop() 
#to write at least minimum size
#we write as width,height
main_root.minsize(900,900)

#to write at least maxsize
#we write as width,height
main_root.maxsize(1200, 988)

#user will not intereact with label
#making a label
my_label = Label(text="Its my label")
#we always want to pack to displat label text
my_label.pack()

main_root.mainloop()
