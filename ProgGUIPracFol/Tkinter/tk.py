import tkinter
from tkinter import *

win = Tk() #Creating window
"""Canvas"""
c= Canvas(win,height=500,width=500,bg='light blue')
#creating arc in canvas
coord = 210,300,360,370
#arc = c.create_arc(coord,start=0,extent=90,fill='red')

"""functions"""
def pr():
    print("Hello")

"""Adding Dimension"""
#win.geometry("500x500")

"""Creating button widget and showing them"""
b = Button(win,text='Button',command=pr,padx=5,pady=5,activeforeground='blue')
b1 = Button(win,text='Button1',padx=5,pady=5)

#pack function shows button(widget) wherever it can
#b.pack()

#Grid Method requires Row and column
#b.grid(row = 1,column=1)
#b1.grid(row = 1,column=2)

#Place method takes x,y axis
b.place(x = 100,y=150)
b1.place(x = 160,y=150)

c.pack()
win.mainloop() #Ends