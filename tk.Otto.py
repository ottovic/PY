
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinterweb import HtmlFrame

def doSomething():
#    messagebox.showinfo("I am doing something")
    global htmlText
    print("I am doing something")
    htmlText = htmlText + "<br>I am doing something"
    displayHtml()

def displayHtml():
    global htmlText
    global root
    global myhtmlframe
    print ("diplaying")
    myhtmlframe.load_html(htmlText) #Load some HTML code
    myhtmlframe.pack(fill="both", expand=True) #attach the HtmlFrame widget to the parent window
    button = Button(text="PressMe",command=doSomething)
    button.place(x=500, y=50)
    root.mainloop()

root = tk.Tk()
root.geometry("700x400")
htmlText = "<h1>Hello, World!</h1>"
# Label = tk.Label(root, text="Populáció genetikai szimuláció")
# Label.pack()
root.title('Populáció genetikai szimuláció')
root.resizable(width=True, height=True)

myhtmlframe = HtmlFrame(root) #create HTML browser

#button = Button(text="PressMe",command=doSomething)
#button.place(x=500, y=50)

print("DONE")

displayHtml()
