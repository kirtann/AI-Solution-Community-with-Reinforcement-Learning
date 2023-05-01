# SocioAI
from tkinter import *
from tkinter import messagebox
import webbrowser
import login

def startlog():
    root.destroy()
    login.home()

def callback(url):
    webbrowser.open_new(url)

root = Tk()
root.title("SocioAI")
root.geometry("900x600")
root.resizable(False,False)
root.config(background="cyan")
icon = PhotoImage(file="lpu.png")
bg = PhotoImage(file="Home_bg.png")
root.iconphoto(False,icon)
l1 = Label(root,image=bg,bg="cyan")
l1.pack()

l2 = Label(root,text="👋Introducing SocioAI",bg="blue", fg="cyan", font=("Calibri", 25))
l2.place(x="303",y="205")

l2 = Label(root,text="आपका अपना दोस्त",bg="blue", fg="cyan", font=("Calibri", 15))
l2.pack()
l2 = Label(root,text="SocioAI is an advanced AI model designed to provide accurate information on society and social issues.\n It allows users to update and contribute to its database, making it a powerful tool for personal and professional use.\n With SocioAI, you can access a wealth of information and explore the complexities of social behavior and society.\n Welcome to the future of knowledge exploration and discovery!",bg="cyan", fg="black", font=("Ink Free", 12))
l2.pack(pady=30)

start = Button(root,text="Let's Get Started !!",bg="orange", command=startlog ,font = ("Ink Free",15))
start.pack()

end = Label(root,text="\n\n\n**If you are facing any problem related to SocioAI, or else want to give Feedback please contact our Developer Team by pressing contact us! ",fg = "black",bg = "cyan",font=("Calibri",10))
end.pack(pady=5)

contact = Button(root,text="Contact us!",bg="blue",fg="cyan",font = ("Calibri",13))
contact.pack(side="bottom")
contact.bind("<Button-1>", lambda e: callback("https://github.com/kirtann/AI-Solution-Community-with-Reinforcement-Learning"))
root.mainloop()
