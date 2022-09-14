print("Hello world")

class Ember:
    Genere = 1
    Name = ""
    Locus = ["W","B","W"]
    Color = 0
    ColorStr = ""

Jozsi = Ember
Jozsi.Name = "Jozsi"

stri = "" + Jozsi.Name + ":"
color = 0
for i in range(3):
    stri = stri + Jozsi.Locus[i]
    if Jozsi.Locus[i] == "B":
        color = color + 1
    i = i + 1
Jozsi.Color = color;
Jozsi.ColorStr = str(Jozsi.Color)
stri = stri + ":" + Jozsi.ColorStr

print(stri)



