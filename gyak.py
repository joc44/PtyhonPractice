from tkinter import *

ablak1 = Tk()

text1 = Label(ablak1, text ="Jónapot kívánok", fg='red')
text1.pack()

gomb1 = Button(ablak1,text="Kilép", command = ablak1.destroy)
gomb1.pack()
ablak1.mainloop()
