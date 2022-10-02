baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}

if baliky["B541X"] == True:
    print("Balík byl předán kurýrovi"),
else:
    print("Balík zatím nebyl předán kurýrovi")

uz1 = baliky["B541X"]
uz2 = baliky["B547X"]
uz3 = baliky["B251X"]
uz4 = baliky["B501X"]
uz5 = baliky["B947X"]

if uz1 == True:
    print("Balik byl předán kurýrovi.")
else:
    print("Balík zatím nebyl předán kurýrovi.")

if baliky.values == True:
    print("Balik byl předán kurýrovi."),
else:
    print("Balík zatím nebyl předán kurýrovi.")



