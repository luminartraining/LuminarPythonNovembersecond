from tkinter import *
def init():
    root=Tk()
    tFrmae=Frame(root)
    bFrame=Frame(root)

    tFrmae.pack()
    bFrame.pack(side=BOTTOM)

    btn1=Button(tFrmae,text="FirstButton",fg="green")
    btn2=Button(tFrmae,text="SecondButton",fg="blue")
    btn3=Button(tFrmae,text="ThirdButton",fg="yellow")
    btn4=Button(bFrame,text="FourthButton",fg="cyan")
    btn1.pack(side=LEFT)
    btn2.pack(side=LEFT)
    btn3.pack(side=LEFT)
    btn4.pack()

    root.mainloop()