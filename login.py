# SocioAI
from tkinter import *
from tkinter import messagebox
import webbrowser
from mybanner import bannerTop
import database
import AdminLogin
import RegisterUser
import NormalLogin
import ProLogin
import RegisterPro

print(bannerTop())

def loginAdmin():
    if e1.get()=='admin' and e2.get()=='admin':
        AdminLogin.admin();
    else: 
        messagebox.showinfo("Error", "Wrong password cannot login as admin") 


def loginNormal():
    global window
    database.connectdb()
    for i in range(database.cur.rowcount):
        data=database.cur.fetchone() 
        if e1.get().strip()==str(data[0]) and e2.get().strip()==str(data[2]):
            messagebox.showinfo("Welcome", "Welcome user "+ data[1])
            database.closedb()
            NormalLogin.nor()
            break
        elif e1.get().strip()==str(data[0]) and e2.get().strip()!=str(data[2]):
            messagebox.showinfo("Error", "Wrong Password")
            database.closedb()
            break
    else:
        # window.withdraw()
        messagebox.showinfo("Register", "New User detected kindly register with community")
        database.closedb()
        RegisterUser.registerUser()

def loginPro():
    global window
    database.connectdb()
    database.cur.execute('SELECT * FROM ProUser')
    for i in range(database.cur.rowcount):
        data=database.cur.fetchone() 
        if e1.get().strip()==str(data[0]) and e2.get().strip()==str(data[2]):
            messagebox.showinfo("Welcome", "Welcome Pro User "+ data[1])
            database.closedb()
            ProLogin.pro()
            break
        elif e1.get().strip()==str(data[0]) and e2.get().strip()!=str(data[2]):
            messagebox.showinfo("Error", "Wrong Password")
            database.closedb()
            break
    else:
        # window.withdraw()
        messagebox.showinfo("Register", "No Pro User detected kindly register with advanced services")
        database.closedb()
        RegisterPro.registerPro()



def callback(url):
    webbrowser.open_new(url)

def home():
    try:
        global window,b1,b2,b3,b4,e1,e2,e3
        window=Tk()
        window.iconbitmap()
        window.resizable(False,False)
        window.title('SocioAI Login')
        icon = PhotoImage(file="lpu.png")
        window.iconphoto(False, icon)
        window.geometry("400x480+480+180")
        window.configure(bg="#00EEEE", bd=9)
        logoname=Label(window,text="SocioAI Login", bg=	"#3A5FCD",fg="#98F5FF",height=1, width=11,font='Arial 15 bold')
        usid=Label(window,text='USER ID')
        paswrd=Label(window,text='PASSWORD')
        e1=Entry(window,width=24)
        e2=Entry(window,width=24)
        e2.config(show="*")
        b1=Button(window,text=' LOGIN AS NORMAL' ,bg="#104E8B",fg="#F8F8FF",height=2,width=20,command=loginNormal)
        b2=Button(window,text=' LOGIN AS PRO ' ,bg="#104E8B",fg="#F8F8FF",height=2,width=20,command=loginPro)
        b3=Button(window,text=' REGISTER WITH SOCIOAI ' ,bg="#104E8B",fg="#F8F8FF",height=2,width=20,command=RegisterUser.registerUser)
        b4=Button(window,text=' LOGIN AS ADMIN ',bg="#104E8B",fg="#F8F8FF", height=2,width=20,command=loginAdmin)
        e3=Label(window,text=' VIEW DEVELOPER CODE ', fg="blue", cursor="hand2", font='Helvetica 5 underline')
        logoname.place(x=130,y=30)
        usid.place(x=70,y=100)
        paswrd.place(x=70,y=140)
        e1.place(x=180,y=100)
        e2.place(x=180,y=140)
        b1.place(x=165,y=190)
        b2.place(x=165,y=237)
        b3.place(x=165,y=285)
        b4.place(x=165,y=355)
        e3.place(x=140,y=450)
        e3.bind("<Button-1>", lambda e: callback("https://github.com/kirtann/AI-Solution-Community-with-Reinforcement-Learning"))
        window.mainloop()
    except Exception:
        window.destroy()

# home()
