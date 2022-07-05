#Start
from tkinter import *
from os import system
from random import randint

#Variables
height = 550
width = 470
Player = "x"
Player_win = 0
moves = [
    ['-','-','-'],
    ['-','-','-'],
    ['-','-','-']
]
count = 0

def Reset():
    root.destroy()
    system('python PvsPC.py')

def Circle(value):
    if value == 1:
        print("ahoj")


def Create_game_table():
    c.create_rectangle(10,50,460,500, fill="white")

def Create_rectangles():
    #Vertical
    c.create_line(160,50,160,500)
    c.create_line(310,50,310,500)
    #Horizontal
    c.create_line(10,200,460,200)
    c.create_line(10,350,460,350)

def Check_X(x,y):
    global Player, count
    #First row
    if 10 < x < 160 and 50 < y < 200 and moves[0][0] == '-':
        moves[0][0] = 'x'
        Player = 'o'
        count += 1
        c.create_line(10,50,160,200, fill="red", width=3)
        c.create_line(10,200,160,50, fill="red", width=3)
    elif 160 < x < 310 and 50 < y < 200 and moves[0][1] == '-':
        moves[0][1] = 'x'
        Player = 'o'
        count += 1
        c.create_line(160,50,310,200, fill="red", width=3)
        c.create_line(160,200,310,50, fill="red", width=3)
    elif 310 < x < 460 and 50 < y < 200 and moves[0][2] == '-':
        moves[0][2] = 'x'
        Player = 'o'
        count += 1
        c.create_line(310,50,460,200, fill="red", width=3)
        c.create_line(310,200,460,50, fill="red", width=3)
    
    #Second Row
    elif 10 < x < 160 and 200 < y < 350 and moves[1][0] == '-':
        moves[1][0] = 'x'
        Player = 'o'
        count += 1
        c.create_line(10,200,160,350, fill="red", width=3)
        c.create_line(10,350,160,200, fill="red", width=3)
    elif 160 < x < 310 and 200 < y < 350 and moves[1][1] == '-':
        moves[1][1] = 'x'
        Player = 'o'
        count += 1
        c.create_line(160,200,310,350, fill="red", width=3)
        c.create_line(160,350,310,200, fill="red", width=3)
    elif 310 < x < 460 and 200 < y < 350 and moves[1][2] == '-':
        moves[1][2] = 'x'
        Player = 'o'
        count += 1
        c.create_line(310,200,460,350, fill="red", width=3)
        c.create_line(310,350,460,200, fill="red", width=3)

    #Third Row
    elif 10 < x < 160 and 350 < y < 500 and moves[2][0] == '-':
        moves[2][0] = 'x'
        Player = 'o'
        count += 1
        c.create_line(10,350,160,500, fill="red", width=3)
        c.create_line(10,500,160,350, fill="red", width=3)
    elif 160 < x < 310 and 350 < y < 500 and moves[2][1] == '-':
        moves[2][1] = 'x'
        Player = 'o'
        count += 1
        c.create_line(160,350,310,500, fill="red", width=3)
        c.create_line(160,500,310,350, fill="red", width=3)
    elif 310 < x < 460 and 350 < y < 500 and moves[2][2] == '-':
        moves[2][2] = 'x'
        Player = 'o'
        count += 1
        c.create_line(310,350,460,500, fill="red", width=3)
        c.create_line(310,500,460,350, fill="red", width=3)

def Check_O():
    global Player, count
    #First row
    if 10 < x < 160 and 50 < y < 200 and moves[0][0] == '-':
        moves[0][0] = 'o'
        Player = 'x'
        count += 1
        c.create_oval(10,50,160,200, outline="blue", width=3)
    elif 160 < x < 310 and 50 < y < 200 and moves[0][1] == '-':
        moves[0][1] = 'o'
        Player = 'x'
        count += 1
        c.create_oval(160,50,310,200, outline="blue", width=3)
    elif 310 < x < 460 and 50 < y < 200 and moves[0][2] == '-':
        moves[0][2] = 'o'
        Player = 'x'
        count += 1
        c.create_oval(310,50,460,200, outline="blue", width=3)

    #Second Row
    elif 10 < x < 160 and 200 < y < 350 and moves[1][0] == '-':
        moves[1][0] = 'o'
        Player = 'x'
        count += 1
        c.create_oval(10,200,160,350, outline="blue", width=3)
    elif 160 < x < 310 and 200 < y < 350 and moves[1][1] == '-':
        moves[1][1] = 'o'
        Player = 'x'
        count += 1
        c.create_oval(160,200,310,350, outline="blue", width=3)
    elif 310 < x < 460 and 200 < y < 350 and moves[1][2] == '-':
        moves[1][2] = 'o'
        Player = 'x'
        count += 1
        c.create_oval(310,200,460,350, outline="blue", width=3)

    #Third Row
    elif 10 < x < 160 and 350 < y < 500 and moves[2][0] == '-':
        moves[2][0] = 'o'
        Player = 'x'
        count += 1
        c.create_oval(10,350,160,500, outline="blue", width=3)
    elif 160 < x < 310 and 350 < y < 500 and moves[2][1] == '-':
        moves[2][1] = 'o'
        Player = 'x'
        count += 1
        c.create_oval(160,350,310,500, outline="blue", width=3)
    elif 310 < x < 460 and 350 < y < 500 and moves[2][2] == '-':
        moves[2][2] = 'o'
        Player = 'x'
        count += 1
        c.create_oval(310,350,460,500, outline="blue", width=3)

def Check():
    global Player_win
    #Horizontal Check
    for i in range(3):
        if ((moves[i][0] == 'x') and (moves[i][1] == 'x') and (moves[i][2] == 'x')):
            Player_win = 'x'
            c.create_line(10,125+i*150,460,125+i*150, width=8)
            return 1

        elif ((moves[i][0] == 'o') and (moves[i][1] == 'o') and (moves[i][2] == 'o')):
            Player_win = 'o'
            c.create_line(10,125+i*150,460,125+i*150, width=8)
            return 1

    #Veritcal Check
    for i in range(3):
        if ((moves[0][i] == 'x') and (moves[1][i] == 'x') and (moves[2][i] == 'x')):
            Player_win = 'x'
            c.create_line(85+i*150,50,85+i*150,500, width=8)
            return 1

        elif ((moves[0][i] == 'o') and (moves[1][i] == 'o') and (moves[2][i] == 'o')):
            Player_win = 'o'
            c.create_line(85+i*150,50,85+i*150,500, width=8)
            return 1

    #Diagonal Check        
    if ((moves[0][0] == 'x') and (moves[1][1] == 'x') and (moves[2][2] == 'x')):
        Player_win = 'x'
        c.create_line(10,50,460,500, width=8)
        return 1

    elif ((moves[0][0] == 'o') and (moves[1][1] == 'o') and (moves[2][2] == 'o')):
        Player_win = 'o'
        c.create_line(10,50,460,500, width=8)
        return 1

    elif ((moves[2][0] == 'x') and (moves[1][1] == 'x') and (moves[0][2] == 'x')):
        Player_win = 'x'
        c.create_line(10,500,460,50, width=8)
        return 1

    elif ((moves[2][0] == 'o') and (moves[1][1] == 'o') and (moves[0][2] == 'o')):
        Player_win = 'o'
        c.create_line(10,500,460,50, width=8)
        return 1

def Move(value):
    global Player
    #Check who is on move
    if Player == 'x':
        Check_X(value.x, value.y)
    elif Player == 'o':
        Check_O(value.x, value.y)

    #Check if someone win
    if Check() == 1:
        root.unbind('<Button-1>')
        c.create_text(250,25, text="Hráč "+Player_win+" vyhral!", font="Arial 20 bold")
        Button(root, command=Reset, text="Reset").pack()
    elif Check() != 1 and count == 9:
        root.unbind('<Button-1>')
        c.create_text(250,25, text="Remíza!", font="Arial 20 bold")
        Button(root, command=Reset, text="Reset").pack()


#Canvas
root = Tk()
root.title('Player VS Computer')
c = Canvas(master=root, height = height, width = width)
c.pack()

Create_game_table()
Create_rectangles()

root.bind('<Button-1>', Move)
#End
root.mainloop()

