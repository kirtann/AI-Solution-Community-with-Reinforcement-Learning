from tkinter import *
import pymysql as p
from tkinter import messagebox
from tkinter.ttk import Treeview
import database

def addbook():
    pass
def issuebook():
    pass
def returnbook():
    pass
def viewbook():
    pass
def issuedbook():
    pass
def deletebook():
    pass
def logout():
    win.destroy()


def nor():
    window=Tk()
    window.withdraw()
    global win,b1,b2,b3,b4
    win=Tk()
    win.title('Library')
    win.geometry("400x400+480+180")
    win.configure(bg="#00EEEE", bd=9)
    win.resizable(False,False)
    b1=Button(win, height=2,width=25,text=' Ask Query ',command=addbook)
    b2=Button(win, height=2,width=25,text=' Issue Book ',command=issuebook)
    b3=Button(win, height=2,width=25,text=' Return Book ',command=returnbook)
    b4=Button(win, height=2,width=25,text=' View Book ',command=viewbook)
    b5=Button(win, height=2,width=25,text=' Issued Book ',command=issuedbook)
    b6=Button(win, height=2,width=25,text=' Delete Book ',command=deletebook)
    b7=Button(win, height=2,width=25,text=' LogOut ',command=logout)
    b1.place(x=110,y=30)
    b2.place(x=110,y=80)
    b3.place(x=110,y=130)
    b4.place(x=110,y=180)
    b5.place(x=110,y=230)
    b6.place(x=110,y=280)
    b7.place(x=110,y=330)
    win.mainloop()