import tkinter
from tkinter import *

root = Tk()
root.title("Simple Calculator- FahimF")
root.geometry("570x600+100+200")
root.resizable(False, False)
root.configure(bg="#17161b")

label_result = Label(root, width=25, height=2, text="", font=("arial", 30))
label_result.pack()

# First Row.....
Button(root, text="AC", width=5, height=1, font=("ariall", 30, "bold"),
       bd=1, fg="#fff", bg="#3697f5").place(x=10, y=100)
Button(root, text="/", width=5, height=1, font=("ariall", 30, "bold"),
       bd=1, fg="#fff", bg="#2a2d36").place(x=150, y=100)
Button(root, text="%", width=5, height=1, font=("ariall", 30, "bold"),
       bd=1, fg="#fff", bg="#2a2d36").place(x=290, y=100)
Button(root, text="*", width=5, height=1, font=("ariall", 30, "bold"),
       bd=1, fg="#fff", bg="#2a2d36").place(x=430, y=100)

# Secand Row.....
Button(root, text="7", width=5, height=1, font=("ariall", 30, "bold"),
       bd=1, fg="#fff", bg="#2a2d36").place(x=10, y=200)
Button(root, text="8", width=5, height=1, font=("ariall", 30, "bold"),
       bd=1, fg="#fff", bg="#2a2d36").place(x=150, y=200)
Button(root, text="9", width=5, height=1, font=("ariall", 30, "bold"),
       bd=1, fg="#fff", bg="#2a2d36").place(x=290, y=200)
Button(root, text="-", width=5, height=1, font=("ariall", 30, "bold"),
       bd=1, fg="#fff", bg="#2a2d36").place(x=430, y=200)
# Third Row.....
Button(root, text="4", width=5, height=1, font=("ariall", 30, "bold"),
       bd=1, fg="#fff", bg="#2a2d36").place(x=10, y=300)
Button(root, text="5", width=5, height=1, font=("ariall", 30, "bold"),
       bd=1, fg="#fff", bg="#2a2d36").place(x=150, y=300)
Button(root, text="6", width=5, height=1, font=("ariall", 30, "bold"),
       bd=1, fg="#fff", bg="#2a2d36").place(x=290, y=300)
Button(root, text="+", width=5, height=1, font=("ariall", 30, "bold"),
       bd=1, fg="#fff", bg="#2a2d36").place(x=430, y=300)
# 4 Row.....
Button(root, text="1", width=5, height=1, font=("ariall", 30, "bold"),
       bd=1, fg="#fff", bg="#2a2d36").place(x=10, y=400)
Button(root, text="2", width=5, height=1, font=("ariall", 30, "bold"),
       bd=1, fg="#fff", bg="#2a2d36").place(x=150, y=400)
Button(root, text="3", width=4, height=1, font=("ariall", 30, "bold"),
       bd=1, fg="#fff", bg="#2a2d36").place(x=290, y=400)
Button(root, text="0", width=11, height=1, font=("ariall", 30, "bold"),
       bd=1, fg="#fff", bg="#2a2d36").place(x=10, y=500)

# 5 Row
Button(root, text=".", width=4, height=1, font=("ariall", 30, "bold"),
       bd=1, fg="#fff", bg="#2a2d36").place(x=290, y=500)
Button(root, text="=", width=5, height=3, font=("ariall", 30, "bold"),
       bd=1, fg="#fff", bg="#fe9037").place(x=430, y=400)


root.mainloop()
