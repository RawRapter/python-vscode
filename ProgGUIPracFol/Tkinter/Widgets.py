import tkinter
from tkinter import *

win = Tk() #Creating window
win.geometry("500x500")
"""Creating Check button"""
c1 = IntVar()
c2 = IntVar()

cb = Checkbutton(win,text='Gym',offvalue=0,onvalue=1,height=5,width=5,variable=c1)
cb1 = Checkbutton(win,text='Sleep',offvalue=0,onvalue=1,height=5,width=5,variable=c2)
cb.pack()
cb1.pack()

"""Creating Radio button"""
var = IntVar()
r1 = Radiobutton(win,text='Gym1',variable=var,value=1)
r1.pack()
r2 = Radiobutton(win,text='Gym2',variable=var,value=2)
r2.pack()
r3 = Radiobutton(win,text='Gym3',variable=var,value=3)
r3.pack()

"""Label and Entry and text"""
l = Label(win,text='Username')
l.pack(side=LEFT)
e = Entry(win)
e.pack()
t = Text(win)
t.insert(INSERT,'Anant Arun')
t.pack(side=BOTTOM)

win.mainloop() #Ends