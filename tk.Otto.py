
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinterweb import HtmlFrame


class Ember:
    Genere = 1
    Name = ""
    Allel1 = ["W","B","W"]
    Allel2 = ["W","W","B"]
    Gender = "M"
    Color = 0
    ColorStr = ""

    def __init__(self,name,gender,allel1,allel2):
        color = 0

        for i in range(len(self.Allel1)):
            self.Allel1[i] = allel1[i:1]
            self.Allel2[i] = allel2[i:1]
            self.Gender = gender

            if(self.Allel1[i]=="B" or self.Allel2[i] == "B"):
                color = color + 1
        self.Color = color
        self.name = name
        self.ColorStr = str(self.Color)

    def display(self):
        text = self.name + ":" + self.ColorStr
        return(text)
        

Jozsi = Ember(name = "Jozsi",allel1 = "BWW", allel2 = "BWW",gender = "M")
print(Jozsi.display())


def doSomething():
#    messagebox.showinfo("I am doing something")
    global htmlText
    global Jozsi
    htmlText = htmlText + "<tr><td>" + Jozsi.display()+ "</td></tr>"
    print("I am doing something: " + htmlText)
    displayHtml()

def displayHtml():
    global htmlText
    global root
    global myhtmlframe
    print ("displaying")
    htmlText = htmlText + "</table>"
    myhtmlframe.load_html(htmlText) #Load some HTML code
    myhtmlframe.pack(fill="both", expand=True) #attach the HtmlFrame widget to the parent window
    button = Button(text="PressMe",command=doSomething)
    button.place(x=500, y=50)
    root.mainloop()

root = tk.Tk()
root.geometry("700x400")
htmlText = "<h1>Hello, World!</h1><table>"
# Label = tk.Label(root, text="Populáció genetikai szimuláció")
# Label.pack()
root.title('Populáció genetikai szimuláció')
root.resizable(width=True, height=True)

myhtmlframe = HtmlFrame(root,messages_enabled = False) #create HTML browser

#button = Button(text="PressMe",command=doSomething)
#button.place(x=500, y=50)

print("DONE")

displayHtml()
