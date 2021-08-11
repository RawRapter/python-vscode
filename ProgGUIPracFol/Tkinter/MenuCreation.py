import tkinter
from tkinter import *

win = Tk() #Creating window

#creating command for all menu options
def nothing():
    file = Toplevel(win)
    button = Button(file,text='nothing')
    button.pack()

#creating menu
menubar = Menu(win)
"""first menu"""
filemenu = Menu(menubar)
#creating menu inside menu options with seprator line
filemenu.add_command(label='New Window',command=nothing)
filemenu.add_command(label='New File',command=nothing)
filemenu.add_separator()
filemenu.add_command(label='Open',command=nothing)
filemenu.add_command(label='Close',command=nothing)
filemenu.add_separator()
filemenu.add_command(label='Exit',command=win.quit)
#adding options menu to the main menu bar in 1 menu option  
menubar.add_cascade(label='File',menu=filemenu)

"""Second Menu"""
editmenu=Menu(menubar)
editmenu.add_command(label='Undo',command=nothing)
editmenu.add_command(label='Redo',command=nothing)
editmenu.add_separator()
editmenu.add_command(label='Cut',command=nothing)
editmenu.add_command(label='Copy',command=nothing)
menubar.add_cascade(label='Edit',menu=editmenu)

win.config(menu=menubar)

"""Scroll Widget"""
s = Scale(win)
s.pack()

sb = Spinbox(win,from_=0, to=10)
sb.pack()

Scrollbar = Scrollbar(win)
Scrollbar.pack(side=RIGHT,fill=Y)
list = Listbox(win,yscrollcommand=Scrollbar.set)
for line in range(50):
    list.insert(END,'Line No. '+str(line))
list.pack(side=LEFT,fill=BOTH)



win.mainloop() #Ends