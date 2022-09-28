
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
    Gender = "M"
    Color = 0
    ColorStr = ""
    Kids = 5
    Partners = 2

    def __init__(self,Name,Gender,pAllel1,pAllel2):
        color = 0
        print("INIT: " + Name + ":" + pAllel1 + "/" + pAllel2)

        self.Allel1 = []
        self.Allel2 = []

        for i in range(len(pAllel1)):
            self.Allel1.append(pAllel1[i])
#            self.Allel1[i] = pAllel1[i]
#            self.Allel2[i] = pAllel2[i]
            self.Allel2.append(pAllel2[i])
            self.Gender = Gender
#            print("................" + str(i) + self.Allel1[i])

#            if(self.Allel1[i]=="B" or self.Allel2[i] == "B"):
#                color = color + 1
#        print(self.Allel1[0]+self.Allel1[1]+self.Allel1[2]+"/"+self.Allel2[0]+self.Allel2[1]+self.Allel2[2])
#        self.Color = color
        self.Name = Name
#        self.ColorStr = str(self.Color)
        self.colorize()
        print("...Color:" + self.ColorStr)

    def colorize(self):
        color = 0
        for i in range(len(self.Allel1)):
            if(self.Allel1[i]=="B" or self.Allel2[i] == "B"):
                color = color + 1
        self.Color = color
        self.ColorStr = str(self.Color)

    def display(self):
        text = self.Name
        if(self.Gender=="M"):
            text = text + ", MALE "
        else:
            text = text + ", FEMALE "
        text = text + ":" + self.ColorStr
        return(text)

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
        text = "<td><img src=\"" + self.getImageFile()+ "\"</td>"
        return(text)
        
i = 1
CYCLE = 1
print("*** STARTING")
random.seed(a=None, version=2)

#----------------------------------
# Marriage, random kid is generated
#----------------------------------
def birth(Name,Apa,Anya):
    global CYCLE

    print("*** KID CREATION")
    print("apa:" + Apa.Name +   ":" + Apa.Gender +  ":" + Apa.Allel1[0]  + Apa.Allel1[1]  + Apa.Allel1[2])
    print("anya:" + Anya.Name + ":" + Anya.Gender + ":" + Anya.Allel1[0] + Anya.Allel1[1] + Anya.Allel1[2])
    
    if(Anya.Kids == 0):
        return(-1)

    kid = Ember(Name = Name + " ben " + Apa.Name,Gender="X",pAllel1="XXX",pAllel2="XXX")
    dice = random.randint(0,1)
    if dice == 0:
        kid.Gender = "M"
    else:
        kid.Gender = "F"
#    print(str(dice) + kid.Gender)

    for j in range(len(Apa.Allel1)):
        dice = random.randint(0,1)

        if(dice == 0):
            kid.Allel1[j] = Apa.Allel1[j]
        else:
            kid.Allel1[j] = Apa.Allel2[j]
#        print("....allel1 dice: " + str(dice) + ":" + kid.Allel1[j])
        dice = random.randint(0,1)
        if(dice == 0):
            kid.Allel2[j] = Anya.Allel1[j]
        else:
            kid.Allel2[j] = Anya.Allel2[j]
#        print("....allel2 dice: " + str(dice) + ":" + kid.Allel2[j])
    kid.colorize()

    print (kid.display() + "-" + kid.Allel1[0] + kid.Allel1[1] + kid.Allel1[2] + "/" + kid.Allel2[0] + kid.Allel2[1] + kid.Allel2[2])
    Anya.Kids = Anya.Kids - 1
    return(kid)

# -----------------------------
# Action when button is pressed
# -----------------------------
def doSomething():
    global htmlText
    global ember
    global myHtmlFrams
    global i
    i = i + 1
    if int(i/2) == i/2 :
        ember = Adam
        print("Páros " + str(i) + "-" + ember.displayHtmlImage())
    else :
        ember = Eva
        print("Páratlan " + str(i))
    print("*** I am doing something ***");
    htmlText = htmlText + "<tr><td>" + ember.display()+ "</td>" + ember.displayHtmlImage() + "</tr>"
    displayHtml()

# Displays HTML table
def displayHtml():
    global htmlText
    global root
    global myhtmlframe
    htmlTextFinal = htmlText + "</table>"
#    print ("displaying: " + htmlTextFinal)
    myhtmlframe.load_html(htmlTextFinal) #Load some HTML code
    myhtmlframe.pack(fill="both", expand=True) #attach the HtmlFrame widget to the parent window

# -----------------------------------------------------
# Displays an image of a human at the given coordinates
# -----------------------------------------------------
def displayMan(pEmber,pX,pY):
    global tk
#    filename = "r" + pEmber.getImageFile()
    filename = pEmber.getImageFile()
    print(filename)
    man = Image.open(filename)
    test = ImageTk.PhotoImage(man)
    label1 = tk.Label(image=test)
    label1.image = test
    label1.place(x=pX, y=pY)


# --------------------------------------------------
# ----------------- MAIN ---------------------------
# --------------------------------------------------
root = tk.Tk()
root.geometry("1500x700")

myhtmlframe = HtmlFrame(root,messages_enabled = False) #create HTML browser
htmlText = "<h1>Populáció genetikai szimuláció</h1><table  border = 1>"
# Label = tk.Label(root, text="Populáció genetikai szimuláció")
# Label.pack()

Populacio = []
NextGen = []

Adam = Ember(Name = "Adam",pAllel1 = "BWB", pAllel2 = "WWW",Gender = "M")
Eva = Ember(Name = "Eva",pAllel1 = "BWW", pAllel2 = "WBW",Gender = "F")

Kain = birth(Name="Kain",Apa=Adam,Anya=Eva)
Abel = birth(Name="Abel",Apa=Adam,Anya=Eva)
Seth = birth(Name="Seth",Apa=Adam,Anya=Eva)

Populacio.append(Adam)
Populacio.append(Eva)
Populacio.append(Kain)
Populacio.append(Abel)
Populacio.append(Seth)

for human in Populacio:
    htmlText = htmlText + "<tr><td>" + human.Name + "</td>" + human.displayHtmlImage()
    displayHtml()

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

#button = Button(text="PressMe",command=doSomething)
#button.place(x=500, y=50)

print("DONE")

displayHtml()
root.mainloop()
