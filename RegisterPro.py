from tkinter import *
import pymysql as p
from tkinter import messagebox
import database
import re


def isValid(s):
     
    Pattern = re.compile("[0-9]{9}")
    return Pattern.match(s)

def register():
    num2=e7.get()
    if(isValid(num2)):
        database.connectdb()
        database.cur.execute('SELECT * FROM ProUser')
        for i in range(database.cur.rowcount):
            data=database.cur.fetchone() 
            if e4.get().strip()==str(data[0]):
                win.destroy()
                messagebox.showinfo("Kindly Login", "This user id already exists login or register with different id")
                database.closedb()
                break
        else:
            q='INSERT INTO Adminpermit VALUE("%i","%s","%s","%i","%i","%s","%s")'
            database.cur.execute(q%(int(e4.get()),e5.get(),e6.get(),int(e7.get()),0,"NULL","NULL"))
            database.con.commit()
            win.destroy()
            messagebox.showinfo("Pro", "Request sent, waiting for confirmation")
            database.closedb()
            # destroy()
    else:
        messagebox.showerror('Number not valid', 'Error: This is a not valid mobile number!')

def registerPro():
    window=Tk()
    window.withdraw()
    global win,e4,e5,e6,e4,e7,b5,b6
    win=Toplevel()
    win.title('Register Pro Page')
    win.geometry("600x600+300+50")
    icon = PhotoImage(file="lpu.png")
    win.iconphoto(False, icon)
    win.configure(bg="#00EEEE", bd=9)
    win.resizable(False,False)
    logoname=Label(win,text="JOIN OUR ADVANCED SERVICE", bg="#3A5FCD",fg="#98F5FF",height=1, width=40,font='Arial 15 bold')
    usid=Label(win,text='USER ID')
    name=Label(win,text='NAME')
    paswrd=Label(win,text='PASSWORD')
    ph_no=Label(win,text='PHONE NUMBER')
    e4=Entry(win,width=24)
    e5=Entry(win,width=24)
    e6=Entry(win,width=24)
    e6.config(show="*")
    e7=Entry(win,width=24)
    b5=Button(win, height=2,width=25,text=' REGISTER ',command=register)
    b6=Button(win, height=2,width=25,text=' HOME ',command=destroy)
    logoname.place(x=60,y=40)
    usid.place(x=100,y=100)
    name.place(x=100,y=140)
    paswrd.place(x=100,y=180)
    ph_no.place(x=100,y=220)
    e4.place(x=250,y=100)
    e5.place(x=250,y=140)
    e6.place(x=250,y=180)
    e7.place(x=250,y=220)
    b5.place(x=200,y=270)
    b6.place(x=200,y=330)
    win.mainloop()

def destroy():
    win.destroy()
