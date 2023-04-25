from tkinter import *
import pymysql as p
from tkinter import messagebox
from tkinter.ttk import Treeview
import database
import Search2
import Search

def askquerymed():
    Search2.searchPage()

def askqueryedu():
    Search.searchPage()

def topquerymed():
    pass
def topqueryedu():
    pass
def alterdb():
    global win
    win.destroy()
    win=Toplevel()
    win.title('Add query ans solution to dataset')
    win.geometry("400x400+480+180")
    icon = PhotoImage(file="lpu.png")
    win.iconphoto(False, icon)
    win.configure(bg="#00EEEE", bd=9)
    win.resizable(False,False)
    usid=Label(win,text='Query')
    paswrd=Label(win,text='Solution')
    global e1
    e1=Entry(win)
    global e2,b2
    e2=Entry(win)
    b1=Button(win, height=2,width=17,text=' Add Query ',command=addQuery)
    # b2=Button(win, height=2,width=17,text=' DISAPPROVE ',command=cancelPro)
    b2=Button(win, height=2,width=17,text=' Back to dashboard ',command=closeusers)
    usid.place(x=80,y=100)
    paswrd.place(x=70,y=140)
    e1.place(x=180,y=100)
    e2.place(x=180,y=142)
    b1.place(x=180,y=180)
    b2.place(x=180,y=230)
    win.mainloop()

def addQuery():
    database.connectdb()
    q='INSERT INTO AddQuery(alter_query,alter_solution) VALUE("%s","%s")'
    database.cur.execute(q%(e1.get(),e2.get()))
    database.con.commit()
    win.destroy()
    messagebox.showinfo("Query Request", "Request sent, waiting for admin to confirm data")
    database.closedb()
    pro()
            # destroy()


def closeusers():
    win.destroy()
    pro()

def logout():
    win.destroy()


def pro():
    window=Tk()
    window.withdraw()
    global win,b1,b2,b3,b4,b5,b6,logoname
    win=Toplevel()
    win.title('Pro User Dashboard')
    win.geometry("480x410+480+180")
    win.configure(bg="#00EEEE", bd=9)
    icon = PhotoImage(file="lpu.png")
    win.iconphoto(False, icon)
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
