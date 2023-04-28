from tkinter import *
from tkinter import messagebox
import re
import pandas as pd
from sklearn import preprocessing
from sklearn.tree import DecisionTreeClassifier, _tree
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC
import csv
import database

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

global clf, cols, txt

training = pd.read_csv('Data/Training.csv')
testing = pd.read_csv('Data/Testing.csv')
cols = training.columns
cols = cols[:-1]
x = training[cols]
y = training['prognosis']
y1 = y


reduced_data = training.groupby(training['prognosis']).max()

# mapping strings to numbers
le = preprocessing.LabelEncoder()
le.fit(y)
y = le.transform(y)


x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.33, random_state=42)
testx = testing[cols]
testy = testing['prognosis']
testy = le.transform(testy)


clf1 = DecisionTreeClassifier()
clf = clf1.fit(x_train, y_train)
# print(clf.score(x_train,y_train))
# print ("cross result========")
scores = cross_val_score(clf, x_test, y_test, cv=3)
# txt.insert(END, "\n" + "Bot -> " + str(scores.mean()))


model = SVC()
model.fit(x_train, y_train)
# txt.insert(END, "\n" + "Bot -> " + "for svm: ")
# txt.insert(END, "\n" + "Bot -> " + str(model.score(x_test,y_test)))

importances = clf.feature_importances_
indices = np.argsort(importances)[::-1]
features = cols

severityDictionary = dict()
description_list = dict()
precautionDictionary = dict()

symptoms_dict = {}

for index, symptom in enumerate(x):
    symptoms_dict[symptom] = index


def calc_condition(exp,days,txt):
    sum=0
    for item in exp:
         sum=sum+severityDictionary[item]
    if((sum*days)/(len(exp)+1)>13):
        print("You should take the consultation from doctor. ")
        txt.insert(END, "\n" + "You should take the consultation from doctor. ")
    else:
        print("It might not be that bad but you should take precautions.")
        txt.insert(END, "\n" + "It might not be that bad but you should take precautions.")
 

def getDescription():
    global description_list
    with open('MasterData/symptom_Description.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            _description = {row[0]: row[1]}
            description_list.update(_description)


def getSeverityDict():
    global severityDictionary
    with open('MasterData/symptom_severity.csv') as csv_file:

        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        try:
            for row in csv_reader:
                _diction = {row[0]: int(row[1])}
                severityDictionary.update(_diction)
        except:
            pass


def getprecautionDict():
    global precautionDictionary
    with open('MasterData/symptom_precaution.csv') as csv_file:

        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            _prec = {row[0]: [row[1], row[2], row[3], row[4]]}
            precautionDictionary.update(_prec)


def check_pattern(dis_list, inp):
    pred_list = []
    inp = inp.replace(' ', '_')
    patt = f"{inp}"
    regexp = re.compile(patt)
    pred_list = [item for item in dis_list if regexp.search(item)]
    if(len(pred_list) > 0):
        return 1, pred_list
    else:
        return 0, []


def sec_predict(symptoms_exp):
    df = pd.read_csv('Data/Training.csv')
    X = df.iloc[:, :-1]
    y = df['prognosis']
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=20)
    rf_clf = DecisionTreeClassifier()
    rf_clf.fit(X_train, y_train)

    symptoms_dict = {symptom: index for index, symptom in enumerate(X)}
    input_vector = np.zeros(len(symptoms_dict))
    for item in symptoms_exp:
        input_vector[[symptoms_dict[item]]] = 1

    return rf_clf.predict([input_vector])


def print_disease(node):
    node = node[0]
    val = node.nonzero()
    disease = le.inverse_transform(val[0])
    return list(map(lambda x: x.strip(), list(disease)))


def tree_to_code(tree, feature_names, txt):
    tree_ = tree.tree_
    feature_name = [
        feature_names[i] if i != _tree.TREE_UNDEFINED else "undefined!"
        for i in tree_.feature
    ]

    chk_dis=",".join(feature_names).split(",")
    symptoms_present = []

    while True:

        print("\nEnter the symptom you are experiencing  \t\t",end="->")
        disease_input = input("")
        conf,cnf_dis=check_pattern(chk_dis,disease_input)
        if conf==1:
            print("searches related to input: ")
            for num,it in enumerate(cnf_dis):
                print(num,")",it)
            if num!=0:
                print(f"Select the one you meant (0 - {num}):  ", end="")
                conf_inp = int(input(""))
            else:
                conf_inp=0

            disease_input=cnf_dis[conf_inp]
            break
            # print("Did you mean: ",cnf_dis,"?(yes/no) :",end="")
            # conf_inp = input("")
            # if(conf_inp=="yes"):
            #     break
        else:
            print("Enter valid symptom.")

    while True:
        try:
            num_days=int(input("Okay. From how many days ? : "))
            break
        except:
            print("Enter valid input.")
    def recurse(node, depth):
        global present_disease
        indent = "  " * depth
        if tree_.feature[node] != _tree.TREE_UNDEFINED:
            name = feature_name[node]
            threshold = tree_.threshold[node]

            if name == disease_input:
                val = 1
            else:
                val = 0
            if  val <= threshold:
                recurse(tree_.children_left[node], depth + 1)
            else:
                symptoms_present.append(name)
                recurse(tree_.children_right[node], depth + 1)
        else:
            present_disease = print_disease(tree_.value[node])
            # print( "You may have " +  present_disease )
            red_cols = reduced_data.columns 
            symptoms_given = red_cols[reduced_data.loc[present_disease].values[0].nonzero()]
            # dis_list=list(symptoms_present)
            # if len(dis_list)!=0:
            #     print("symptoms present  " + str(list(symptoms_present)))
            # print("symptoms given "  +  str(list(symptoms_given)) )
            print("Are you experiencing any ")
            symptoms_exp=[]
            for syms in list(symptoms_given):
                inp=""
                print(syms,"? : ",end='')
                while True:
                    inp=input("")
                    if(inp=="yes" or inp=="no"):
                        break
                    else:
                        print("provide proper answers i.e. (yes/no) : ",end="")
                if(inp=="yes"):
                    symptoms_exp.append(syms)

            second_prediction=sec_predict(symptoms_exp)
            # print(second_prediction)
            calc_condition(symptoms_exp,num_days,txt)
            if(present_disease[0]==second_prediction[0]):
                print("You may have ", present_disease[0])
                txt.insert(END, "\n" + "Bot -> You may have :\t"+ present_disease[0])
                print(description_list[present_disease[0]])
                # txt.insert(END, "\n" + description_list[present_disease[0]])
                # readn(f"You may have {present_disease[0]}")
                # readn(f"{description_list[present_disease[0]]}")

            else:
                print("You may have ", present_disease[0], "or ", second_prediction[0])
                txt.insert(END, "\n" + "Bot -> You may have :\t"+ present_disease[0]+ " or "+ second_prediction[0])
                print(description_list[present_disease[0]])
                # txt.insert(END, "\n" + description_list[present_disease[0]])
                print(description_list[second_prediction[0]])
                # txt.insert(END, "\n" + description_list[second_prediction[0]])

            # print(description_list[present_disease[0]])
            precution_list=precautionDictionary[present_disease[0]]
            print("Take following measures : ")
            for  i,j in enumerate(precution_list):
                print(i+1,")",j)

            # confidence_level = (1.0*len(symptoms_present))/len(symptoms_given)
            # print("confidence level is " + str(confidence_level))

    recurse(0, 1)

def searchdb(user, txt):
    database.connectdb()
    database.cur.execute('SELECT * FROM QueryHospital')
    for i in range(database.cur.rowcount):
        data=database.cur.fetchone()
        if user==str(data[0]):
            txt.insert(END, "\n" + "Bot -> You are suggested " + str(data[1]) + " pill.")
            a = data[2]
            a += 1
            q='UPDATE QueryHospital set query_pointer="%i" WHERE disease="%s"'
            database.cur.execute(q%(int(a),str(user)))
            database.con.commit()
            # database.closedb()
            break
    else:
        # window.withdraw()
        txt.insert(END, "\n" + "Bot -> No data found in hospital database.")
        txt.insert(END, "\n" + "Bot ->  be pro user to upload data.")


    database.cur.execute('SELECT * FROM QueryEducation')
    for i in range(database.cur.rowcount):
        data=database.cur.fetchone()
        if user==str(data[0]):
            txt.insert(END, "\n" + "Bot -> Average package of university is " + str(data[1]))
            txt.insert(END, "\n" + "Bot -> NIRF ranking of university is " + str(data[2]))
            txt.insert(END, "\n" + "Bot -> Admission criteria of university is " + str(data[3]))
            a = int(data[4])
            a += 1
            q1='UPDATE QueryEducation set query_pointer="%i" WHERE name="%s"'
            database.cur.execute(q1%(int(a), str(user)))
            database.con.commit()
            break
    else:
        # window.withdraw()
        txt.insert(END, "\n" + "Bot -> No data found in education database.")
        txt.insert(END, "\n" + "Bot ->  be pro user to upload data.")
    database.closedb()


def send(txt):
    send = "You -> " + user
    txt.insert(END, "\n" + send)

    if (user == "hello"):
        txt.insert(END, "\n" + "Bot -> Hi there, how can I help?")

    elif (user == "hi" or user == "hii" or user == "hiiii"):
        txt.insert(END, "\n" + "Bot -> Hi there, what can I do for you?")

    elif (user == "how are you"):
        txt.insert(END, "\n" + "Bot -> fine! and you")

    elif (user == "fine" or user == "i am good" or user == "i am doing good"):
        txt.insert(END, "\n" + "Bot -> Great! how can I help you.")

    elif (user == "thanks" or user == "thank you" or user == "now its my time"):
        txt.insert(END, "\n" + "Bot -> My pleasure !")

    elif (user == "what do you sell" or user == "what kinds of items are there" or user == "have you something"):
        txt.insert(END, "\n" + "Bot -> We have recommendations and nursing queries")

    elif (user == "tell me a joke" or user == "tell me something funny" or user == "crack a funny line"):
        txt.insert(
            END, "\n" + "Bot -> What did the buffalo say when his son left for college? Bison.! ")

    elif (user == "goodbye" or user == "see you later" or user == "see yaa"):
        txt.insert(END, "\n" + "Bot -> Have a nice day!")

    # elif (user == "begin" or user =="initiate" or user == "start"):
    #     flag=1
    else:
        txt.insert(END, "\n" + "Bot -> Sorry! I didn't understand that")


def destroy():
    sroot.destroy()


def strconvert():
    global user, flag
    user = search.get().lower()
    if(user == "start" or user == "begin" or user == "initiate"):
        flag = 1
    elif(user == "stop" or user == "end" or user == "finish"):
        flag = 3
    elif(user == "search" or user =="find"):
        flag = 5
    elif(user == "off" or user =="close"):
        flag = 10
        

    if(flag == 3):
        txt.insert(
            END, "\n" + "\nThankyou for choosing us. Visit again soon")
        
        txt.insert(
            END, "\n" + "----------------------------------------------------------------------------------------")
        flag=0
    elif(flag==1):
        txt.insert(
            END, "\n" + "----------------------------------- SocioAI Healthcare -----------------------------------")
        txt.insert(
            END, "\n\n" + "\t visit terminal for further AI Interactions")
        # messagebox.showinfo("Terminal redirect", "Visit terminal for further Interactions !")
        tree_to_code(clf, cols, txt)
        print("Visit GUI for further interaction")
    elif(flag==5):
        txt.insert(
            END, "\n" + "----------------------------------- SocioAI Recommendation -----------------------------------")
        flag=6
    elif flag==6:
        searchdb(user ,txt)
    elif(flag==10):
        txt.insert(
            END, "\n" + "\nThankyou for choosing us. Visit again soon")
        
        txt.insert(
            END, "\n" + "----------------------------------------------------------------------------------------")
        flag=0
    else:
        send(txt)
    search.delete(0, END)
        

def searchPage():
    getSeverityDict()
    getDescription()
    getprecautionDict()
    global flag
    flag = 0
    global sroot, search, icon, window, txt, b1
    window = Tk()
    window.withdraw()
    sroot = Toplevel()
    sroot.title("SocioAI-Search Engine")

    icon = PhotoImage(file="lpu.png")
    sroot.iconphoto(False, icon)
    # sroot.geometry("900x600")
    sroot.resizable(False, False)
    sroot.config(background="cyan")
    lable1 = Label(sroot, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome", font=FONT_BOLD, width=20, pady=10, height=1).grid(
        row=0, column=0)
    b1 = Button(sroot, text=' DASHBOARD ', font=FONT_BOLD,
                command=destroy).grid(row=0, column=1)
    txt = Listbox(sroot, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT,
                  width=65, height=25, activestyle=NONE)
    txt.grid(row=1, column=0, columnspan=2)

    scrollbar = Scrollbar(txt)
    scrollbar.place(relheight=1, relx=0.974)
    txt.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=txt.yview)

    search = Entry(sroot, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=54)
    search.insert(0, "Hello I am SocioAI, how can I help you?")
    search.grid(row=2, column=0)

    send1 = Button(sroot, text=" HELP ", font=FONT_BOLD, bg=BG_GRAY,
                   command=strconvert).grid(row=2, column=1)

    sroot.mainloop()
