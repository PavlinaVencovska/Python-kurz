# Zadání:
# Vytvoř program na prodej vstupenek do letního kina. Ceny vstupenek jsou v tabulce níže.

# Datum	Cena
# 1. 7. 2021 - 10. 8. 2021	250 Kč
# 11. 8. 2021 - 31. 8. 2021	180 Kč
# Mimo tato data je středisko zavřené.

# Tvůj program se nejprve zeptá uživatele na datum a počet osob, pro které uživatel chce vstupenky koupit. Uživatel zadá datum ve středoevropském formátu. Převeď řetězec zadaný uživatelem na datum pomocí funkce datetime.strptime().

# Pokud by uživatel zadal příjezd mimo otevírací dobu, vypiš, že letní kino je v té době uzavřené. Pokud je letní kino otevřené, spočítej a vypiš cenu za vstupenky.


from datetime import datetime

datum = input("Zadej datum: ")
pocet_osob = input("Zadej počet osob: ")

datum = datetime.strptime(datum, "%d. %m. %Y")

if datum >= datetime(2021, 7, 1) and datum <= datetime(2021, 8, 10):
    cena_vstupenky = int(pocet_osob) * 250
    print(f"Cena vstupenky/ek je {cena_vstupenky}.")
elif datum >= datetime(2021, 8, 11) and datum <= datetime(2021, 8, 31):
    cena_vstupenky = int(pocet_osob) * 180
    print(f"Cena vstupenky/ek je {cena_vstupenky}.")
else: 
    print("Letní kino je v tuto dobu zavřené.")
