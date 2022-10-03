baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}

print("Zadej kód balíku:")
kod =  input()

if baliky[kod]:
    print("balík byl předán kurýrovi.")
else: 
    print("balík zatím nebyl předán kurýrovi.")