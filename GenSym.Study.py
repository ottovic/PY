print("Hello world")

class Ember:
    Genere = 1
    Name = ""
    Locus = ["B","W","W"]
    Color = 0
    ColorStr = ""

Jozsi = Ember
Jozsi.Name = "Jozsi"

stri = "" + Jozsi.Name + ":"
color = 0
for i in range(3):
    stri = stri + Jozsi.Locus[i]
    if Jozsi.Locus[i] == "B":
        i = i + 1
Jozsi.Color = i;
Jozsi.ColorStr = str(Jozsi.Color)
stri = stri + ":" + Jozsi.ColorStr

print(stri)



