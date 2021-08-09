import tkinter
from tkinter import *
from functools import partial

win = Tk() #Creating window
#win.geometry("300x300")

#defing sum
def sum(label,x1,x2):
    n1 = int(x1.get())
    n2 = int(x2.get())
    sum = n1 + n2
    label.config(text='Value is %d'%sum)
    return
#Label for Numbers
l1 = Label(win,text='First Number')
l1.grid(row=1,column=0)
l2 = Label(win,text='Second Number')
l2.grid(row=2,column=0)

#Label for result
Label = Label(win)
Label.grid(row=6,column=2)

#Entries
x1=StringVar()
x2=StringVar()

e1 = Entry(win,textvariable=x1)
e1.grid(row=1,column=2)
e2 = Entry(win,textvariable=x2)
e2.grid(row=2,column=2)

#Button
sum = partial(sum,Label,x1,x2)
B1 = Button(win,text='Calculate', command=sum)
B1.grid(row=3,column=0)

win.mainloop() #end