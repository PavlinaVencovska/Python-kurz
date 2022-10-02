baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}

print(baliky.keys())

if baliky["B541X"] == True:
    print("Balík byl předán kurýrovi"),
else:
    print("Balík zatím nebyl předán kurýrovi")

for key in baliky:
    print(key)
    if key == True:
        print("Balik byl předán kurýrovi."),
    else:
        print("Balík zatím nebyl předán kurýrovi.")



