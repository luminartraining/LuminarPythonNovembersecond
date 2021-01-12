# tkinter
from tkinter import *



root=Tk() #root reference root
root.title("main window")
label1=Label(root,text="username")
label2=Label(root,text="emailaddress")
label3=Label(root,text="password")
entry1=Entry(root)
label1.pack()
entry1.pack()
label2.pack()
label3.pack()


root.mainloop()

