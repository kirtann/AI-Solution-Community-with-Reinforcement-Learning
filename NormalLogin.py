from tkinter import *
from tkinter.ttk import Treeview
import database
import Search2
import Search

def askquerymed():
    Search2.searchPage()

def askqueryedu():
    Search.searchPage()

def topquerymed():
    win=Toplevel()
    win.title('Top Medicine queries')
    # win.geometry("800x300+270+180")
    win.configure(bg="#00EEEE", bd=9)
    icon = PhotoImage(file="lpu.png")
    win.iconphoto(False, icon)
    win.resizable(False,False)
    treeview=Treeview(win,columns=("Disease","Medicine","Reward"),show='headings')
    treeview.heading("Disease", text="Disease")
    treeview.heading("Medicine", text="Medicine")
    treeview.heading("Reward", text="Reward")
    treeview.column("Disease", anchor='center')
    treeview.column("Medicine", anchor='center')
    treeview.column("Reward", anchor='center')
    index=0
    iid=0
    database.connectdb()
    database.cur.execute('SELECT * FROM QueryHospital ORDER BY query_pointer DESC')
    details=database.cur.fetchall()
    for row in details:
        treeview.insert("",index,iid,value=row)
        index=iid=index+1
    treeview.pack()
    win.mainloop()
    database.closedb()

def topqueryedu():
    win=Toplevel()
    win.title('Top Education queries')
    # win.geometry("800x300+270+180")
    win.configure(bg="#00EEEE", bd=9)
    icon = PhotoImage(file="lpu.png")
    win.iconphoto(False, icon)
    win.resizable(False,False)
    treeview=Treeview(win,columns=("Name","Package","Ranking","Criteria","Reward"),show='headings')
    treeview.heading("Name", text="Name")
    treeview.heading("Package", text="Package")
    treeview.heading("Ranking", text="Ranking")
    treeview.heading("Criteria", text="Criteria")
    treeview.heading("Reward", text="Reward")
    treeview.column("Name", anchor='center')
    treeview.column("Package", anchor='center')
    treeview.column("Ranking", anchor='center')
    treeview.column("Criteria", anchor='center')
    treeview.column("Reward", anchor='center')
    index=0
    iid=0
    database.connectdb()
    database.cur.execute('SELECT * FROM QueryEducation ORDER BY query_pointer DESC')
    details=database.cur.fetchall()
    for row in details:
        treeview.insert("",index,iid,value=row)
        index=iid=index+1
    treeview.pack()
    win.mainloop()
    database.closedb()

def logout():
    win.destroy()


def nor():
    window=Tk()
    window.withdraw()
    global win,b1,b2,b3,b4,b5,logoname
    win=Toplevel()
    win.title('Normal User Dashboard')
    win.geometry("480x370+480+180")
    icon = PhotoImage(file="lpu.png")
    win.iconphoto(False, icon)
    win.configure(bg="#00EEEE", bd=9)
    win.resizable(False,False)
    logoname=Label(win,text="SocioAI Community", bg=	"#3A5FCD",fg="#98F5FF",height=1, width=20,font='Arial 15 bold')
    b1=Button(win, height=2,width=40,text=' Ask Nursing related Query ',command=askquerymed)
    b2=Button(win, height=2,width=40,text=' Ask Education related Query ',command=askqueryedu)
    b3=Button(win, height=2,width=40,text=' View Top Asked Nursing related Queries ',command=topquerymed)
    b4=Button(win, height=2,width=40,text=' View Top Asked Education related Queries ',command=topqueryedu)
    b5=Button(win, height=2,width=40,text=' LogOut ',command=logout)
    logoname.place(x=110,y=20)
    b1.place(x=85,y=60)
    b2.place(x=85,y=110)
    b3.place(x=85,y=160)
    b4.place(x=85,y=210)
    b5.place(x=85,y=260)
    win.mainloop()
