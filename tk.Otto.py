
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinterweb import HtmlFrame
from PIL import ImageTk, Image


class Ember:
    Genere = 1
    Name = ""
    Allel1 = ["X","X","X"]
    Allel2 = ["X","X","X"]
    Gender = "M"
    Color = 0
    ColorStr = ""
    Kids = 5

    def __init__(self,name,gender,allel1,allel2):
        color = 0
        print("INIT: " + name)

        for i in range(len(self.Allel1)):
            print("   " + str(i) + allel1[i])
            self.Allel1[i] = allel1[i]
            self.Allel2[i] = allel2[i]
            self.Gender = gender

            if(self.Allel1[i]=="B" or self.Allel2[i] == "B"):
                color = color + 1
        print(self.Allel1)
        self.Color = color
        self.name = name
        self.ColorStr = str(self.Color)

    def display(self):
        text = self.name
        if(self.Gender=="M"):
            text = text + " MALE "
        else:
            text = text + " FEMALE "
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
        
        

Adam = Ember(name = "Adam",allel1 = "BWW", allel2 = "BWW",gender = "M")
Eva = Ember(name = "Eva",allel1 = "WWW", allel2 = "WWW",gender = "F")
i = 1
print("*** STARTING")


def doSomething():
#    messagebox.showinfo("I am doing something")
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

def displayHtml():
    global htmlText
    global root
    global myhtmlframe
    htmlTextFinal = htmlText + "</table>"
#    print ("displaying: " + htmlTextFinal)
    myhtmlframe.load_html(htmlTextFinal) #Load some HTML code
    myhtmlframe.pack(fill="both", expand=True) #attach the HtmlFrame widget to the parent window

def displayMan(pEmber,pX,pY):
    global tk
#    filename = "r" + pEmber.getImageFile()
    filename = pEmber.getImageFile()
    print(filename)
    man = Image.open(filename)
#man = img.resize((20, 20), Image.ANTIALIAS)
    test = ImageTk.PhotoImage(man)
    label1 = tk.Label(image=test)
    label1.image = test
    label1.place(x=pX, y=pY)


root = tk.Tk()
root.geometry("1500x700")

myhtmlframe = HtmlFrame(root,messages_enabled = False) #create HTML browser
htmlText = "<h1>Populáció genetikai szimuláció</h1><table  border = 1>"
# Label = tk.Label(root, text="Populáció genetikai szimuláció")
# Label.pack()
root.title('Populáció genetikai szimuláció')
root.resizable(width=True, height=True)

displayMan(Adam,300,200)
displayMan(Eva,400,300)

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
