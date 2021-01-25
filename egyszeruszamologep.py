from  tkinter import *
from math import *

def kiertekel(event):
    chain.configure(text = "Eredmeny = " + str(eval(mezo.get())))



ablak = Tk()

mezo = Entry(ablak)
mezo.bind("<Return>",kiertekel)
mezo.pack()

chain = Label(ablak)
chain.pack()


ablak.mainloop()