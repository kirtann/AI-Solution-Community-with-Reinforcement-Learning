from tkinter import *
import pymysql as p
from tkinter import messagebox
from tkinter.ttk import Treeview
import database



def admin():
    window=Tk()
    window.withdraw()
    global win,b1,b2,b3,b4,b5,b6,b7,b8,cur,con
    win=Toplevel()
    win.title('Admin')
    win.geometry("400x480+480+180")
    win.configure(bg="#00EEEE", bd=9)
    icon = PhotoImage(file="lpu.png")
    win.iconphoto(False, icon)
    win.resizable(False,False)
    b1=Button(win, height=2,width=25,text=' View User ',command=viewNormaluser)
    b2=Button(win, height=2,width=25,text=' View Pro User ',command=viewProuser)
    b3=Button(win, height=2,width=25,text=' Pro User Requests ',command=permitProuser)
    b4=Button(win, height=2,width=25,text=' Approve Pro', command=approvePro)
    b5=Button(win, height=2,width=25,text=' Delete User ',command=deleteuser)
    b6=Button(win, height=2,width=25,text=' View Query Requests ',command=queryReq)
    b7=Button(win, height=2,width=25,text=' Approve Query from Pro ',command=approveReq)
    b8=Button(win, height=2,width=25,text=' LogOut ',command=logout)
    b1.place(x=110,y=40)
    b2.place(x=110,y=90)
    b3.place(x=110,y=140)
    b4.place(x=110,y=190)
    b5.place(x=110,y=240)
    b6.place(x=110,y=290)
    b7.place(x=110,y=340)
    b8.place(x=110,y=390)
    win.mainloop()

def logout():
    win.destroy()
    try:
        database.closedb()
    except:
        print("Logged Out")
    # home()

def queryReq():
    win=Toplevel()
    win.title('Query Add Requests')
    win.geometry("650x300+270+180")
    win.configure(bg="#00EEEE", bd=9)
    icon = PhotoImage(file="lpu.png")
    win.iconphoto(False, icon)
    win.resizable(False,False)
    treeview=Treeview(win,columns=("ID","Query","Solution"),show='headings')
    treeview.heading("ID", text="ID")
    treeview.heading("Query", text="Query")
    treeview.heading("Solution", text="Solution")
    treeview.column("ID", anchor='center')
    treeview.column("Query", anchor='center')
    treeview.column("Solution", anchor='center')
    index=0
    iid=0
    database.connectdb()
    database.cur.execute('SELECT * FROM AddQuery')
    details=database.cur.fetchall()
    for row in details:
        treeview.insert("",index,iid,value=row)
        index=iid=index+1
    treeview.pack()
    win.mainloop()
    database.closedb()


def approveReq():
    global win
    win.destroy()
    win=Toplevel()
    win.title('Add Query To Backend')
    win.geometry("400x400+480+180")
    win.configure(bg="#00EEEE", bd=9)
    icon = PhotoImage(file="lpu.png")
    win.iconphoto(False, icon)
    win.resizable(False,False)
    usid=Label(win,text='Query ID')
    paswrd=Label(win,text='ADMIN \n PASSWORD')
    global e10
    e10=Entry(win)
    global e11,b2
    e11=Entry(win)
    b1=Button(win, height=2,width=25,text=' APPROVE QUERY IN NURSING ',command=addReqNursing)
    b2=Button(win, height=2,width=25,text=' APPROVE QUERY IN EDUCATION  ',command=addReqEducation)
    b3=Button(win, height=2,width=25,text=' DISAPPROVE QUERY ',command=cancelReq)
    b4=Button(win, height=2,width=25,text=' CLOSE ',command=closeusers)
    usid.place(x=80,y=100)
    paswrd.place(x=70,y=140)
    e10.place(x=180,y=100)
    e11.place(x=180,y=142)
    b1.place(x=180,y=180)
    b2.place(x=180,y=230)
    b3.place(x=180,y=280)
    b4.place(x=180,y=330)
    win.mainloop()

def addReqNursing():
    database.connectdb()

    if e11.get()=='admin':
        database.cur.execute('SELECT * FROM AddQuery')
        for i in range(database.cur.rowcount):
            data1=database.cur.fetchone()
            if(data1[0]==int(e10.get())):
                q1='INSERT INTO QueryHospital VALUE("%s","%s","%i")'
                database.cur.execute(q1%(data1[1],data1[2],0))
                database.con.commit()
                q='DELETE FROM AddQuery WHERE id="%i"'
                database.cur.execute(q%(int(e10.get())))
                database.con.commit()
                win.destroy()
                messagebox.showinfo("NURSING DATASET UPDATED", "Query Approved")
                database.closedb()
                break
        else:
            win.destroy()
            messagebox.showinfo("No Request", "Request not found with given id")
            database.closedb()
        admin()
    else:
        win.destroy()
        messagebox.showinfo("Error", "Incorrect Password")
        database.closedb()
        admin()

def addReqEducation():
    database.connectdb()

    if e11.get()=='admin':
        database.cur.execute('SELECT * FROM AddQuery')
        for i in range(database.cur.rowcount):
            data1=database.cur.fetchone()
            if(data1[0]==int(e10.get())):
                q1='INSERT INTO QueryEducation VALUE("%s","%s","%i")'
                database.cur.execute(q1%(data1[1],data1[2],0))
                database.con.commit()
                q='DELETE FROM AddQuery WHERE id="%i"'
                database.cur.execute(q%(int(e10.get())))
                database.con.commit()
                win.destroy()
                messagebox.showinfo("EDUCATION DATASET UPDATED", "Query Approved")
                database.closedb()
                break
        else:
            win.destroy()
            messagebox.showinfo("No Request", "Request not found with given id")
            database.closedb()
        admin()
    else:
        win.destroy()
        messagebox.showinfo("Error", "Incorrect Password")
        database.closedb()
        admin()

def cancelReq():
    database.connectdb()
    if e11.get()=='admin':
        
        q='DELETE FROM AddQuery WHERE id="%i"'
        database.cur.execute(q%(int(e10.get())))
        database.con.commit()
        win.destroy()
        messagebox.showinfo("Cancelled", "Query addition request cancelled")
        database.closedb()
        admin()
    else:
        messagebox.showinfo("Error", "Incorrect Password")
        database.closedb()

def permitProuser():
    win=Toplevel()
    win.title('Pro User Requests')
    win.geometry("800x300+270+180")
    win.configure(bg="#00EEEE", bd=9)
    icon = PhotoImage(file="lpu.png")
    win.iconphoto(False, icon)
    win.resizable(False,False)
    treeview=Treeview(win,columns=("User ID","Name","Password","Mobile No","Favourite Query"),show='headings')
    treeview.heading("User ID", text="User ID")
    treeview.heading("Name", text="Name")
    treeview.heading("Password", text="Password")
    treeview.heading("Mobile No", text="Mobile No")
    treeview.column("User ID", anchor='center')
    treeview.column("Name", anchor='center')
    treeview.column("Password", anchor='center')
    treeview.column("Mobile No", anchor='center')
    index=0
    iid=0
    database.connectdb()
    database.cur.execute('SELECT * FROM Adminpermit')
    details=database.cur.fetchall()
    for row in details:
        treeview.insert("",index,iid,value=row)
        index=iid=index+1
    treeview.pack()
    win.mainloop()
    database.closedb()

def approvePro():
    global win
    win.destroy()
    win=Toplevel()
    win.title('Approve Pro')
    win.geometry("400x400+480+180")
    win.configure(bg="#00EEEE", bd=9)
    icon = PhotoImage(file="lpu.png")
    win.iconphoto(False, icon)
    win.resizable(False,False)
    usid=Label(win,text='USER ID')
    paswrd=Label(win,text='ADMIN \n PASSWORD')
    global e1
    e1=Entry(win)
    global e2,b2
    e2=Entry(win)
    e2.config(show="*")
    b1=Button(win, height=2,width=17,text=' APPROVE ',command=addPro)
    b2=Button(win, height=2,width=17,text=' DISAPPROVE ',command=cancelPro)
    b3=Button(win, height=2,width=17,text=' CLOSE ',command=closeusers)
    usid.place(x=80,y=100)
    paswrd.place(x=70,y=140)
    e1.place(x=180,y=100)
    e2.place(x=180,y=142)
    b1.place(x=180,y=180)
    b2.place(x=180,y=230)
    b3.place(x=180,y=280)
    win.mainloop()


def addPro():
    database.connectdb()

    if e2.get()=='admin':
        database.cur.execute('SELECT * FROM Adminpermit')
        for i in range(database.cur.rowcount):
            data=database.cur.fetchone()
            if(data[0]==int(e1.get())):
                q1='INSERT INTO ProUser VALUE("%i","%s","%s","%i","%i","%s","%s")'
                database.cur.execute(q1%(data[0],data[1],data[2],data[3],data[4],data[5],data[6]))
                database.con.commit()
                q='DELETE FROM Adminpermit WHERE u_id="%i"'
                database.cur.execute(q%(int(e1.get())))
                database.con.commit()
                win.destroy()
                messagebox.showinfo("PRO ADDED", "Pro User Added")
                database.closedb()
                break
        else:
            win.destroy()
            messagebox.showinfo("No Request", "Request not found with given id")
            database.closedb()
        admin()
    else:
        win.destroy()
        messagebox.showinfo("Error", "Incorrect Password")
        database.closedb()
        admin()

def cancelPro():
    database.connectdb()
    if e2.get()=='admin':
        
        q='DELETE FROM Adminpermit WHERE u_id="%i"'
        database.cur.execute(q%(int(e1.get())))
        database.con.commit()
        win.destroy()
        messagebox.showinfo("Cancelled", "Pro request cancelled")
        database.closedb()
        admin()
    else:
        messagebox.showinfo("Error", "Incorrect Password")
        database.closedb()

def viewProuser():
    win=Toplevel()
    win.title('View User')
    win.geometry("800x300+270+180")
    win.configure(bg="#00EEEE", bd=9)
    icon = PhotoImage(file="lpu.png")
    win.iconphoto(False, icon)
    win.resizable(False,False)
    treeview=Treeview(win,columns=("User ID","Name","Password","Mobile No","Favourite Query"),show='headings')
    treeview.heading("User ID", text="User ID")
    treeview.heading("Name", text="Name")
    treeview.heading("Password", text="Password")
    treeview.heading("Mobile No", text="Mobile No")
    treeview.column("User ID", anchor='center')
    treeview.column("Name", anchor='center')
    treeview.column("Password", anchor='center')
    treeview.column("Mobile No", anchor='center')
    index=0
    iid=0
    database.connectdb()
    database.cur.execute('SELECT * FROM ProUser')
    details=database.cur.fetchall()
    for row in details:
        treeview.insert("",index,iid,value=row)
        index=iid=index+1
    treeview.pack()
    win.mainloop()
    database.closedb()

def viewNormaluser():
    win=Toplevel()
    win.title('View User')
    win.geometry("800x300+270+180")
    win.configure(bg="#00EEEE", bd=9)
    icon = PhotoImage(file="lpu.png")
    win.iconphoto(False, icon)
    win.resizable(False,False)
    treeview=Treeview(win,columns=("User ID","Name","Password","Mobile No","Favourite Query"),show='headings')
    treeview.heading("User ID", text="User ID")
    treeview.heading("Name", text="Name")
    treeview.heading("Password", text="Password")
    treeview.heading("Mobile No", text="Mobile No")
    treeview.column("User ID", anchor='center')
    treeview.column("Name", anchor='center')
    treeview.column("Password", anchor='center')
    treeview.column("Mobile No", anchor='center')
    index=0
    iid=0
    database.connectdb()
    details=database.cur.fetchall()
    for row in details:
        treeview.insert("",index,iid,value=row)
        index=iid=index+1
    treeview.pack()
    win.mainloop()
    database.closedb()

def closeusers():
    win.destroy()
    admin()

def deleteuser():
    global win
    win.destroy()
    win=Toplevel()
    win.title('Delete user')
    win.geometry("400x400+480+180")
    win.configure(bg="#00EEEE", bd=9)
    icon = PhotoImage(file="lpu.png")
    win.iconphoto(False, icon)
    win.resizable(False,False)
    usid=Label(win,text='USER ID')
    paswrd=Label(win,text='ADMIN \n PASSWORD')
    global e1
    e1=Entry(win)
    global e2,b2
    e2=Entry(win)
    e2.config(show="*")
    b1=Button(win, height=2,width=17,text=' DELETE ',command=deleteusers)
    b2=Button(win, height=2,width=17,text=' CLOSE ',command=closeusers)
    usid.place(x=80,y=100)
    paswrd.place(x=70,y=140)
    e1.place(x=180,y=100)
    e2.place(x=180,y=142)
    b1.place(x=180,y=180)
    b2.place(x=180,y=230)
    win.mainloop()

def deleteusers():
    database.connectdb()
    if e2.get()=='admin':
        
        q='DELETE FROM NormalUser WHERE u_id="%i"'
        database.cur.execute(q%(int(e1.get())))
        database.con.commit()
        win.destroy()
        messagebox.showinfo("Delete", "User Deleted")
        database.closedb()
        admin()
    else:
        messagebox.showinfo("Error", "Incorrect Password")
        database.closedb()
