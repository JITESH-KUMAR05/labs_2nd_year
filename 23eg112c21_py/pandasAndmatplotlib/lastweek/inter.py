from tkinter import *
parent = Tk()
w = Canvas(parent,width=40,height=60)
w.pack()
b1 = Button(parent,text="Left",)
b1.pack(side=LEFT)
b2 = Button(parent,text="Right")
b2.pack(side=RIGHT)
parent.mainloop()