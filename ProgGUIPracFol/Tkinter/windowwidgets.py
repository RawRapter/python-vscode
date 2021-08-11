import tkinter
from tkinter import *
from tkinter import messagebox


win = Tk() #Creating window

#creating Menu
mb = Menubutton(win,text='File')
mb.grid()
mb.menu = Menu(mb)
mb['menu']=mb.menu

x1=IntVar()
x2=IntVar()

mb.menu.add_checkbutton(label='open',variable=x1)
mb.menu.add_checkbutton(label='close',variable=x2)
mb.pack()

#function for message popup
def hello():
    messagebox.showinfo('from computer','Hellooo Sir')

#Frames
frame = Frame(win)
frame.pack()

frame2 = Frame(win)
frame2.pack(side=BOTTOM)

#Buttons in Frames
rb = Button(frame,text='frame1button',fg='red',command=hello) #creating command to use message popup
rb.pack(side=LEFT)
bb = Button(frame,text='frame2button',fg='blue')
bb.pack(side=LEFT)
gb = Button(frame2,text='green',fg='green')
gb.pack(side=LEFT)

#Creating Notes
lb  = Listbox(frame2)
lb.insert(1,'python')
lb.insert(2,'C++')
lb.insert(3,'java')
lb.pack()

win.mainloop() #Ends