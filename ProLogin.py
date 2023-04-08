from tkinter import *
import pymysql as p
from tkinter import messagebox
from tkinter.ttk import Treeview
import database

def askquerymed():
    pass
def askqueryedu():
    pass
def topquerymed():
    pass
def topqueryedu():
    pass
def alterdb():
    pass
def logout():
    win.destroy()


def pro():
    window=Tk()
    window.withdraw()
    global win,b1,b2,b3,b4,b5,b6,logoname
    win=Tk()
    win.title('Pro User Dashboard')
    win.geometry("480x410+480+180")
    win.configure(bg="#00EEEE", bd=9)
    win.resizable(False,False)
    logoname=Label(win,text="SocioAI Community", bg="#3A5FCD",fg="#98F5FF",height=1, width=20,font='Arial 15 bold')
    b1=Button(win, height=2,width=40,text=' Ask Nursing related Query ',command=askquerymed)
    b2=Button(win, height=2,width=40,text=' Ask Education related Query ',command=askqueryedu)
    b3=Button(win, height=2,width=40,text=' View Top Asked Nursing related Queries ',command=topquerymed)
    b4=Button(win, height=2,width=40,text=' View Top Asked Education related Queries ',command=topqueryedu)
    b5=Button(win, height=2,width=40,text=' Upload query in database ',command=alterdb)
    b6=Button(win, height=2,width=40,text=' LogOut ',command=logout)
    logoname.place(x=110,y=20)
    b1.place(x=85,y=60)
    b2.place(x=85,y=110)
    b3.place(x=85,y=160)
    b4.place(x=85,y=210)
    b5.place(x=85,y=260)
    b6.place(x=85,y=310)
    win.mainloop()
