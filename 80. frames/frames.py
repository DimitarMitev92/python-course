from tkinter import *

window = Tk()

frame = Frame(window, bg="lightblue", bd=5, relief=SUNKEN)
frame.place(x=0, y=0, width=300, height=300)
# frame.pack(side=BOTTOM)

Button(frame, text="W",font=("Consolas",25),width=3).pack(side=TOP)
Button(frame, text="A",font=("Consolas",25),width=3).pack(side=LEFT)
Button(frame, text="S",font=("Consolas",25),width=3).pack(side=LEFT)
Button(frame, text="D",font=("Consolas",25),width=3).pack(side=LEFT)


window.mainloop()