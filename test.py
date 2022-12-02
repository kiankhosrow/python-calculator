import tkinter
from tkinter import *

win = Tk()

win.title("This is just for test")
win.geometry("570x600+100+200")
win.resizable(False, False)
win.configure(bg="red")

Button(win, text="Fardin", width=2, height=1,
       bd=1, bg="#2a2d36").place(x=100, y=200)


win.mainloop()
