# Zadání:

# Uvažuj, že píšeš jednoduchou aplikaci pro zasílání SMS zpráv. 
# Napiš program, který provede následující činnosti:

# Zeptá se uživatele na číslo, kam chce zprávu zaslat a ověří, že číslo má správný formát.
# Zeptá se uživatele na zprávu, kterou chce zaslat. Následně vypíše, kolik zpráva bude stát.

# Tvůj program bude obsahovat dvě funkce:

# První funkce ověří délku telefonního čísla. 
# Uvažuj, že telefonní číslo může být devítimístné nebo třináctimístné (pokud je na začátku předvolba "+420"). Nemusíte kontrolovat, zda uživatel zadal skutečně číslo, či zda jsou tam i jiné znaky. To jsme v kurzu zatím neřešili. Pokud je číslo platné, funkce vrátí hodnotu True, jinak vrátí hodnotu False.
# Druhá funkce spočte cenu zprávy. Uživatel platí 3 Kč za každých započatých 180 znaků.

# Tvůj program nejprve ověří pomocí první funkce správnost telefonního čísla. 
# Pokud není platné, vypíše chybu, v opačném případě se zeptá na text zprávy a pomocí druhé funkce určí její cenu, kterou vypíše uživateli.

import math

prijemce = str(input("Zadej telefonni cislo: "))

def delka_tel_cisla(prijemce):
    return len(prijemce) == 9 or len(prijemce) == 13

zprava = ""
    
if delka_tel_cisla(prijemce):
    zprava = str(input("Napis zpravu: "))
else:
    prijemce = str(input("Cislo nema spravny format."))

def cena_zpravy(zprava):
    if len(zprava) % 180 == 0:
        fin_cena = (len(zprava) / 180) * 3 
        print(f"Cena zpravy je : {fin_cena}")
    else:
        fin_cena = (math.ceil(len(zprava) / 180)) * 3
        print(f"Cena zpravy je: {fin_cena}")

cena_zpravy(zprava)




