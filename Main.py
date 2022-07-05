#Start
from tkinter import *
from os import system

#Variables
height = 500
width = 500

#Functions
def PvsP():
    root.destroy()
    system('python PvsP.py')

def PvsPC():
    root.destroy()
    system('python PvsPC.py')

#Canvas
root = Tk()
root.title('text')
c = Canvas(master=root, height = height, width = width)
c.pack()

c.create_text(250,150, text="Tic Tac Toe", font="Arial 40 bold")

Button(root, command=PvsP, text="Player VS Player").place(x=100, y=350)
Button(root, command=PvsPC, text="Player VS Computer").place(x=250, y=350)

#End
root.mainloop()