from tkinter import * 
from tkinter.ttk import *

from time import strftime

clock = Tk()
clock.title("Clock")

def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text = string)
    lbl.after(1000,time)

lbl = Label(clock, font = ('calibri', 40, 'bold'),
background = 'navyblue',
foreground = 'white')

lbl.pack(anchor = 'center')
time()

mainloop()