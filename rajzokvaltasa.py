from tkinter import *

def circle (x, y, r, color = 'black'):
    vaszon.create_oval(x -r, y - r, x + r, y + r, outline = color)
    

def figure_1():
    vaszon.delete(ALL)
    vaszon.create_line(100, 0, 100, 200, fill = 'blue')
    vaszon.create_line(0, 100, 200, 100, fill = 'blue')

    radius = 15
    while radius < 100:
        circle(100, 100, radius)
        radius += 15

def figure_2():
    vaszon.delete(ALL)
    korok = [
             [100, 100, 80, 'red'],
             [70, 70, 15, 'blue'],
             [130, 70, 15, 'blue'],
             [70, 70, 5, 'black'],
             [130, 70, 5, 'black'],
             [44, 115, 20, 'red'],
             [156, 115, 20, 'red'],
             [100, 95, 15, 'purple'],
             [100, 145, 30, 'purple'],
             ]
    i = 0
    while i < len(korok):
        elem = korok[i]
        circle(elem[0], elem[1], elem[2], elem[3])
        i += 1

#Főprogram

ablak = Tk()

vaszon = Canvas(ablak, width = 200, height = 200, bg = 'ivory')
vaszon.pack(side = TOP, padx = 5, pady = 5)

button = Button(ablak, text = '1.ábra', command = figure_1)
button.pack(side = LEFT, padx = 3, pady = 3)

button1 = Button(ablak, text = '2.ábra', command = figure_2)
button1.pack(side = RIGHT, padx = 3, pady = 3)

ablak.mainloop()