#mysql file upload
#%
from tkinter import messagebox
from tkinter import *

root=Tk()
import mysql.connector
from dbconnectpgm.dbconnect import get_connection
def db_connect(uername,password):
    print("inside .....................")
    db=get_connection()
    cursor=db.cursor()
    try:
        cursor.execute(("select * from users where username=%s AND password=%s"),(uername,password))
        user=cursor.fetchone()
        return user

    except Exception as e:
        print(e.args)

def authenticate_user():
    uname=uentry.get()
    pwd=pentry.get()
    user=db_connect(uname,pwd)
    if (user==None):
        messagebox.showerror("invalid user","Error")
    else:
        messagebox.showinfo("user sucessfully logged","user sucessfully logged")

ulabel=Label(root,text="username")
plabel=Label(root,text="Password")
uentry=Entry(root)
pentry=Entry(root)


btn=Button(root,text="login",command=authenticate_user)
ulabel.grid(row=0,column=0)
plabel.grid(row=1,column=0)


uentry.grid(row=0,column=1)
pentry.grid(row=1,column=1)
btn.grid(columnspan=2)
root.mainloop()







#create table students
#rol name course total
#10    ajay mca   140
#11    vjay bca   135
#12    tom  mca   145


#course wise group mca :2,bca:1

#registration

#in which course no of joiness <1  bca

#highest total course wise
#
# mca 145
# bca 135


