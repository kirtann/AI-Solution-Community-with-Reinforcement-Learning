# SocioAI
from tkinter import *
from tkinter import messagebox
import nltk

def create_av_frame(nouns):
    # Create a new top-level window (i.e. a new frame)
    noun_frame = Toplevel(sroot)
    noun_frame.title("ADVERB")
    noun_frame.geometry("400x400")
    noun_frame.resizable(False, False)

    # Create a label with the list of nouns
    noun_label = Label(noun_frame, text="\n".join(nouns), font=('Ink Free', 15))
    noun_label.pack(pady=10)

    # Create an "OK" button to close the window
    ok_button = Button(noun_frame, text="OK", font=('Ink Free', 15), bg="orange", command=noun_frame.destroy)
    ok_button.place(x=170,y=350)


def AV():
    # Get the text from the search Entry widget
    text = search.get()

    # Tokenize the text into individual words using nltk
    words = nltk.word_tokenize(text)

    # Use the NLTK part-of-speech tagger to tag each word with its part of speech
    tagged_words = nltk.pos_tag(words)

    # Extract only the nouns from the tagged words
    nouns = [word for (word, pos) in tagged_words if (pos.startswith('RB') or pos.startswith('RBR') or pos.startswith('RBS'))]

    # Create a new frame with the list of nouns
    create_av_frame(nouns)


def create_pn_frame(nouns):
    # Create a new top-level window (i.e. a new frame)
    noun_frame = Toplevel(sroot)
    noun_frame.title("PRONOUN")
    noun_frame.geometry("400x400")
    noun_frame.resizable(False, False)

    # Create a label with the list of nouns
    noun_label = Label(noun_frame, text="\n".join(nouns), font=('Ink Free', 15))
    noun_label.pack(pady=10)

    # Create an "OK" button to close the window
    ok_button = Button(noun_frame, text="OK", font=('Ink Free', 15), bg="orange", command=noun_frame.destroy)
    ok_button.place(x=170,y=350)
def PN():
    # Get the text from the search Entry widget
    text = search.get()

    # Tokenize the text into individual words using nltk
    words = nltk.word_tokenize(text)

    # Use the NLTK part-of-speech tagger to tag each word with its part of speech
    tagged_words = nltk.pos_tag(words)

    # Extract only the nouns from the tagged words
    nouns = [word for (word, pos) in tagged_words if (pos.startswith('PRP') or pos.startswith('PRP$'))]

    # Create a new frame with the list of nouns
    create_pn_frame(nouns)


def create_verb_frame(nouns):
    # Create a new top-level window (i.e. a new frame)
    noun_frame = Toplevel(sroot)
    noun_frame.title("VERB")
    noun_frame.geometry("400x400")
    noun_frame.resizable(False, False)

    # Create a label with the list of nouns
    noun_label = Label(noun_frame, text="\n".join(nouns), font=('Ink Free', 15))
    noun_label.pack(pady=10)

    # Create an "OK" button to close the window
    ok_button = Button(noun_frame, text="OK", font=('Ink Free', 15), bg="orange", command=noun_frame.destroy)
    ok_button.place(x=170,y=350)
def V():
    # Get the text from the search Entry widget
    text = search.get()

    # Tokenize the text into individual words using nltk
    words = nltk.word_tokenize(text)

    # Use the NLTK part-of-speech tagger to tag each word with its part of speech
    tagged_words = nltk.pos_tag(words)

    # Extract only the nouns from the tagged words
    nouns = [word for (word, pos) in tagged_words if (pos.startswith('VB') or pos.startswith('VBN') or pos.startswith('VBD') or pos.startswith('VBG') or pos.startswith('VBP'))]

    # Create a new frame with the list of nouns
    create_verb_frame(nouns)



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
def N():
    # Get the text from the search Entry widget
    text = search.get()

    # Tokenize the text into individual words using nltk
    words = nltk.word_tokenize(text)

    # Use the NLTK part-of-speech tagger to tag each word with its part of speech
    tagged_words = nltk.pos_tag(words)

    # Extract only the nouns from the tagged words
    nouns = [word for (word, pos) in tagged_words if (pos.startswith('NN') or pos.startswith('NNS') or pos.startswith('NNPS') or pos.startswith('NNP'))]

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
    l2 = Label(sroot,text="SocioAI GrammErLy",font=('Ink Free', 35),bg = 'cyan',fg = 'black')
    l2.place(x=230,y = 250)

    l3 = Label(sroot,text="Enter any Sentance and get corresponding Parts of Speech",font=('caliberi', 17),bg = 'cyan')
    l3.place(x = 150,y = 320)

    search = Entry(sroot, font=('caliberi', 17), bg="white", width=50)
    search.insert(0, "Hello!,I am SocioAI. How are You?")
    search.place(x=130, y=370)

    noun = Button(sroot,text = "Noun",font=('caliberi', 12),command=N,bg = 'orange',width = 10)
    noun.place(x = 150 , y = 450)
    verb = Button(sroot,text = "Verb",command=V,font=('caliberi', 12),bg = 'orange',width = 10)
    verb.place(x = 300 , y = 450)
    pronoun = Button(sroot,text = "Pronoun",command=PN,font=('caliberi', 12),bg = 'orange',width = 10)
    pronoun.place(x = 450 , y = 450)

    adverb = Button(sroot,text = "Adverb",command=AV,font=('caliberi', 12),bg = 'orange',width = 10)
    adverb.place(x = 600 , y = 450)
    

    

    

    sroot.mainloop()
