from tkinter import *
from tkinter import messagebox
import nltk



def create_noun_frame(nouns):
    # Create a new top-level window (i.e. a new frame)
    noun_frame = Toplevel(sroot)
    noun_frame.title("Nouns")
    noun_frame.geometry("400x400")
    noun_frame.resizable(False, False)

    # Create a label with the list of nouns
    noun_label = Label(noun_frame, text="\n".join(nouns), font=('Ink Free', 15))
    noun_label.pack(pady=10)

    # Create an "OK" button to close the window
    ok_button = Button(noun_frame, text="OK", font=('Ink Free', 15), bg="orange", command=noun_frame.destroy)
    ok_button.place(x=170,y=350)

def tokenize_words():
    # Get the text from the search Entry widget
    text = search.get()

    # Tokenize the text into individual words using nltk
    words = nltk.word_tokenize(text)

    # Use the NLTK part-of-speech tagger to tag each word with its part of speech
    tagged_words = nltk.pos_tag(words)

    # Extract only the nouns from the tagged words
    nouns = [word for (word, pos) in tagged_words if pos.startswith('NN')]

    # Create a new frame with the list of nouns
    create_noun_frame(nouns)


def searchPage():
    global sroot, search, l1, enter, icon, sbg, window 
    window = Tk()
    window.withdraw()
    sroot = Toplevel()
    sroot.title("SocioAI-Search Engine")
    sroot.geometry("900x600")
    sroot.resizable(False, False)
    sroot.config(background="cyan")
    sbg = PhotoImage(file="Home_bg.png")
    icon = PhotoImage(file="lpu.png")
    sroot.iconphoto(False, icon)
    l1 = Label(sroot, image=sbg, bg="cyan")
    l1.pack()

    search = Entry(sroot, font=('Ink Free', 17), bg="white", width=50)
    search.insert(0, "Hello I am SocioAI, how can I help you?")
    search.place(x=70, y=300)

    enter = Button(sroot, text="Help Me", font=('Ink Free', 15), bg="orange", command=tokenize_words)
    enter.place(x=750, y=300, height=32)

    options = ["Search", "My Account", "Contact Us", "Logout"]
    clicked = StringVar()
    clicked.set("Search")
    drop = OptionMenu(sroot, clicked, *options)
    drop.place(x=750, y=20)

    sroot.mainloop()

# searchPage()
