from tkinter import*
from random import randrange

#eseménykezelő függvények

def drawline():
    global x1, y1, x2, y2, color
    vaszon1.create_line(x1, y1, x2, y2, width = 2, fill = color)

    y2, y1 = y2 + 10, y1 - 10

def changecolor():
    global color
    paletta =['purple', 'cyan', 'maroon', 'green', 'red', 'blue', 'orange', 'yellow']
    c = randrange(8)
    color =paletta[c]
#Fő program

x1, y1, x2, y2 = 10, 190, 190, 10
color = 'dark green'

ablak1 = Tk()
vaszon1 = Canvas(ablak1, bg = 'dark grey', height = 200, width = 200)
vaszon1.pack(side = LEFT)


gomb1 = Button(ablak1, text = "Kilép", command = ablak1.quit)
gomb1.pack(side = BOTTOM)

gomb2 = Button(ablak1, text = "Vonalat rajzol", command = drawline)
gomb2.pack()

gomb3 = Button(ablak1, text = 'Más szín', command = changecolor)
gomb3.pack()

ablak1.mainloop()

