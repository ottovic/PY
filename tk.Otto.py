from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinterweb import HtmlFrame

def doSomething():
#    messagebox.showinfo("I am doing something")
    print("I am doing something")


root = tk.Tk()
root.geometry("700x400")
# Label = tk.Label(root, text="Populáció genetikai szimuláció")
# Label.pack()
root.title('Populáció genetikai szimuláció')
root.resizable(width=True, height=True)

myhtmlframe = HtmlFrame(root) #create HTML browser
myhtmlframe.load_html("<h1>Hello, World!</h1>") #Load some HTML code
myhtmlframe.pack(fill="both", expand=True) #attach the HtmlFrame widget to the parent window

root.bind("PRESS ME", doSomething)

button = Button(text="PressMe",command=doSomething)
button.place(x=115, y=250)

print("DONE")

root.mainloop()


