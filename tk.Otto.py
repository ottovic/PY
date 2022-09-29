from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinterweb import HtmlFrame
from PIL import ImageTk, Image
import random
from random import randrange

class Ember:
    Genere = 1
    Name = ""
    Allel1 = []
    Allel2 = []
    Gender = "X"
    Color = 0
    Kids = 1000
    Partners = 2
    Seq = 0
    Partner = 0

    def __init__(self,Name,Gender,pAllel1,pAllel2):
        global Sequence
        self.Seq = Sequence
        Sequence = Sequence + 1

        self.Allel1 = []
        self.Allel2 = []

        for i in range(len(pAllel1)):
            self.Allel1.append(pAllel1[i])
            self.Allel2.append(pAllel2[i])
            self.Gender = Gender
        self.Name = Name
        self.colorize()

    def colorize(self):
        color = 0
        for i in range(len(self.Allel1)):
            if(self.Allel1[i]=="B" or self.Allel2[i] == "B"):
                color = color + 1
        self.Color = color

    def diversity(self):
        diversity = 0
        for i in range(len(self.Allel1)):
            if(self.Allel1[i] != self.Allel2[i]):
                diversity = diversity + 1
        return(diversity)

    def display(self):
        text = self.Name
        if(self.Gender=="M"):
            text = text + ", MALE "
        else:
            text = text + ", FEMALE "
        text = text + ":" + self.ColorStr
        return(text)

    def displayGenom(self):
        genom = self.Allel1[0]+self.Allel1[1]+self.Allel1[2]+"/"+self.Allel2[0]+self.Allel2[1]+self.Allel2[2]
        return(genom)

    def getImageFile(self):
        if (self.Color == 0):
            text = self.Gender + "WWW.png"
        elif(self.Color == 1):
            text = self.Gender + "BWW.png"
        elif(self.Color == 2):
            text = self.Gender + "BBW.png"
        else:
            text = self.Gender + "BBB.png"

        return(text)

    def displayHtmlImage(self):
        text = "<img src=\"" + self.getImageFile()+ "\" width=\"30\" height=\"70\">"
#        print(text)
        return(text)
        
CYCLE = 1
print("*** STARTING")
random.seed(a=None, version=2)

#----------------------------------
# Marriage, random kid is generated
#----------------------------------
def birth(Name,Apa,Anya):
    global CYCLE
    global NextGen

#    print("*** KID CREATION ***")
#    print("apa: " + Apa.Seq +  ":" + Apa.Gender +  ":" + Apa.Allel1[0]  + Apa.Allel1[1]  + Apa.Allel1[2]  + "/" +  Apa.Allel2[0]  + Apa.Allel2[1]  + Apa.Allel2[2])
#    print("anya:" + Anya.Seq + ":" + Anya.Gender + ":" + Anya.Allel1[0] + Anya.Allel1[1] + Anya.Allel1[2] + "/" +  Anya.Allel2[0] + Anya.Allel2[1] + Anya.Allel2[2])
    
    if(Anya.Kids == 0):
        return(-1)

    kid = Ember(Name = "",Gender="X",pAllel1="XXX",pAllel2="XXX")
    dice = random.randint(0,1)
    if dice == 0:
        kid.Gender = "M"
    else:
        kid.Gender = "F"

    for j in range(len(Apa.Allel1)):
        dice = random.randint(0,1)

        if(dice == 0):
            kid.Allel1[j] = Apa.Allel1[j]
        else:
            kid.Allel1[j] = Apa.Allel2[j]
        dice = random.randint(0,1)
        if(dice == 0):
            kid.Allel2[j] = Anya.Allel1[j]
        else:
            kid.Allel2[j] = Anya.Allel2[j]
    kid.colorize()

#   print (kid.display() + "-" + kid.Allel1[0] + kid.Allel1[1] + kid.Allel1[2] + "/" + kid.Allel2[0] + kid.Allel2[1] + kid.Allel2[2])
    Anya.Kids = Anya.Kids - 1
    NextGen.append(kid)
    return(kid)

# --------------------------------
# Dye due to unpleasant conditions
# --------------------------------
def dye():
    global CurrentGen
    global Cycle
    DYE_0 = 0
    DYE_1 = 10
    DYE_2 = 50
    DYE_3 = 70
    i=0
    print("ENTER IN DYE:"+str(len(CurrentGen)))
    if(Cycle > 3):
        i = 0
        l = len(CurrentGen)
        while(i<l):
#            print("Die or not:" + str(CurrentGen[i].Seq))
            dice = random.randint(0,100)
            if(CurrentGen[i].Color == 0):
                if(dice < DYE_0):
                    print("Dead:"+str(CurrentGen[i].Seq)+"("+str(CurrentGen[i].Color)+")"+str(dice))
                    CurrentGen.pop(i)
            elif(CurrentGen[i].Color == 1):
                if(dice < DYE_1):
                    print("Dead:"+str(CurrentGen[i].Seq)+"("+str(CurrentGen[i].Color)+")"+str(dice))
                    CurrentGen.pop(i)
            elif(CurrentGen[i].Color == 2):
                if(dice < DYE_2):
                    print("Dead:"+str(CurrentGen[i].Seq)+"("+str(CurrentGen[i].Color)+")"+str(dice))
                    CurrentGen.pop(i)
            elif(CurrentGen[i].Color == 3):
                if(dice < DYE_3):
                    print("***Dead:"+str(CurrentGen[i].Seq)+"("+str(CurrentGen[i].Color)+")"+str(dice))
                    CurrentGen.pop(i)
            l = len(CurrentGen)
            i = i + 1
    print("EXIT FROM DYE:"+str(len(CurrentGen)))
    return()

# --------------------------
# One generation (Monogamic)
# --------------------------
def genMonogamic():
    global htmlText
    global NextGen
    global CurrentGen
    global Populacio
#    print("ENTER MONOGAMIC MATCH:" + str(len(CurrentGen)))
#    NextGen = []
    for man in CurrentGen:
        for woman in CurrentGen:
            if(man.Gender == "M" and man.Partner == 0):
                if(woman.Gender == "F" and woman.Partner == 0):
                    man.Partner = woman.Seq
                    woman.Partner = man.Seq
#                    print("...match:" + str(woman.Seq) + "-" + str(man.Seq))
                    i = 0
                    while i < 5:
                        kid = birth(Name="",Apa=man,Anya=woman)
                        i = i + 1

    i = 0
    CurrentGen = []
    while i<len(NextGen) :
        CurrentGen.append(NextGen[i])
        i = i + 1
    NextGen = []
    print("COMPLETED MONOGAMIC MATCH:" + str(len(CurrentGen)))
                        
    diversity = 0
    for human in CurrentGen:
        diversity = diversity + human.diversity()


# -----------------------------
# Action when button is pressed
# -----------------------------
def doSomething():
    global CurrentGen
    global Cycle
    global htmlText
    Cycle = Cycle + 1
    dye()
    genMonogamic()

#    print("Printing CurrentGen" + str(len(CurrentGen)))
    diversity = 0
    for human in CurrentGen:
        diversity = diversity + human.diversity()

    if(len(CurrentGen)==0):
        htmlText = htmlText + "<tr><td><b>E X T I N C T</b></td>"
    else:

        htmlText = htmlText + "<tr>"
        if(len(CurrentGen)==0):
            htlText = htmlText + "<td>-</td>"
        else:
            htmlText = htmlText + "<td>" +  str(int(diversity/len(CurrentGen)*100)/100) + "</td>"

        for human in CurrentGen:
            htmlText = htmlText + "<td>" + human.displayHtmlImage() + "</td>"

    htmlText = htmlText + "</tr>"
    displayHtml()

# -------------
# Displays HTML
# -------------
def displayHtml():
    global htmlText
    global myhtmlframe
#    htmlTextFinal = htmlText + "</table>"
    htmlTextFinal = htmlText
#    print(htmlText)
    myhtmlframe.load_html(htmlTextFinal)
    myhtmlframe.pack(fill="both", expand=True)
    return()

# -----------------------------------------------------
# Displays an image of a human at the given coordinates
# -----------------------------------------------------
def displayMan(pEmber,pX,pY):
    global tk
#    filename = "r" + pEmber.getImageFile()
    filename = pEmber.getImageFile()
#    print(filename)
    man = Image.open(filename)
    test = ImageTk.PhotoImage(man)
    label1 = tk.Label(image=test)
    label1.image = test
    label1.place(x=pX, y=pY)

#    htmlText = htmlText + "<tr>"
    print("Diversity:"+str(diversity)+" population:"+str(len(CurrentGen)))
    if(len(CurrentGen)!=0):
        htmlText = htmlText + "<tr><td>" +  str(int(diversity/len(CurrentGen)*100)/100) + "</td>"
    else:
        htmlText = htmlText + "<tr><td> - </td>"

    for human in CurrentGen:
#        htmlText = htmlText + "<td><table><tr><td>" + human.displayHtmlImage() + "</td></tr>" + "<tr><td>" + human.displayGenom() + "</td></tr></table></td>"
        htmlText = htmlText + "<td>" + human.displayHtmlImage() + "</td>"
        Populacio.append(human)

    htmlText = htmlText + "</tr>"

    displayHtml()

# --------------------------------------------------
# ----------------- MAIN ---------------------------
# --------------------------------------------------
root = tk.Tk()
root.geometry("1500x700")

Sequence = 1
Cycle = 0

myhtmlframe = HtmlFrame(root,messages_enabled = False,horizontal_scrollbar = "auto") #create HTML browser
htmlText = "<h1>Populáció genetikai szimuláció</h1><table>"

displayHtml()

Populacio = []
NextGen = []
CurrentGen = []

Adam = Ember(Name = "Adam",pAllel1 = "WBW", pAllel2 = "BWB",Gender = "M")
Eva  = Ember(Name = "Eva", pAllel1 = "BWB", pAllel2 = "WWB",Gender = "F")
Populacio.append(Adam)
Populacio.append(Eva)
CurrentGen.append(Adam)
CurrentGen.append(Eva)

diversity = 0
for human in Populacio:
    diversity = diversity + human.diversity()

htmlText = htmlText + "<tr><td>" +  str(diversity/len(Populacio)) + "</td>"

for human in Populacio:
    htmlText = htmlText + "<td>" + human.displayHtmlImage() + "</td>"

htmlText = htmlText + "</tr>"
displayHtml()
print("*** FINISH MAIN ***")

#root.title('Populáció genetikai szimuláció')
#root.resizable(width=True, height=True)

root.title('Populáció genetikai szimuláció')
root.resizable(width=True, height=True)

# Random displaying human images
# displayMan(Adam,300,200)
# displayMan(Eva,400,300)

# man = Image.open(r"BBB.jpg")
# test = ImageTk.PhotoImage(man)
# label1 = tk.Label(image=test)
# label1.image = test
# label1.place(x=10, y=30)

button = Button(text="PressMe",command=doSomething)
button.place(x=500, y=50)

print("DONE (" + str(len(Populacio)) + ")")

root.mainloop()
