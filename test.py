import tkinter
from tkinter import *

win = Tk()
win.title("Simple Calculator- FahimF")
win.geometry("570x600+100+200")
win.resizable(False, False)
win.configure(bg="#17161b")

label_result = Label(win, width=25, height=2,
                     text="", font=("arial", 30))
label_result.pack()

# First Row.....
Button(win, text="AC", width=5, height=1, font=("ariall", 30, "bold"),
       bd=10, fg="#fff", bg="red").place(x=10, y=100)
Button(win, text="/", width=5, height=1, font=("ariall", 30, "bold"),
       bd=8, fg="#fff", bg="#2a2d36").place(x=150, y=100)


win.mainloop()
