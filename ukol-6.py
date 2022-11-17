#Zadání:
# Univerzita pro celoživotní vzdělávání se rozhodla změnit svůj známkovací systém z číselných známek 1 až 5 na hodnocení písmeny A až F. 
# Bohužel změna se odehrála jaksi uprostřed semestru, takže je potřeba změnit aktuální výkazy o známkách z čísel na písmena. 
# Nechte se vést následujícím postupem.
# Otevřete si dokument s jedním výkazem známek.
# Zkopírujte si tuto tabulku do textového souboru - uložte si ho do stejné složky jako skript s řešením domácího úkolu.
# Je jedno jak si ho pojmenujete, ten název pak budete používat ve vašem programu.
# Napište program, který tuto tabulku načte ze souboru (z toho který jste si vytvořily) a změní všechny známky tak, že 1 bude A, 2 bude B, 3 bude C, 4 bude D a 5 bude F.
# Existuje vic způsobů řešení, zamyslete se, jestli se vám třeba nehodí nějaká datová struktura, o které jsme se učili, případně podmínky (pro fajnsmekry se to řešit i s Třídami).
# Vypište váš výsledek do nějakého souboru tak, aby se z něj dal zase zkopírovat do tabulky Google.
# Už umíte funkce - nezapomínejte na to, pokud potřebujete něco udělat víckrát, dejte ten kód do funkce, kterou pak můžete znovu volat.

with open("text.txt", encoding="utf-8") as file:
    radky = file.readlines()

uprava_znamek = [radky[0]]

for radek in radky[1:]:
    uprava_znamek.append(radek.replace("1","A").replace("2","B").replace("3","C").replace("4","D").replace("5", "F")) 
    print(uprava_znamek)

with open("text.txt", mode="w", encoding="utf-8") as output:
    output.writelines(uprava_znamek)