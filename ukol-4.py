# Zadání:
# Uvažuj že vytváříš kuchařku a potřebuješ uložit několik receptů. Vytvoř dvě třídy Recept a Kucharka (idealne v tomto poradi).

# 1. Recept
# Bude mít 3 atributy:

# nazev - string, jmeno kucharky
# narocnost - necham na vas jak ji budete reprezentovat (muze byt cislo, muze byt slovni vyjadreni)
# url_adresa - string, odkaz na recept
# vyzkouseno - bool, metoda __init__ ji vzdy nastavi na False
# nazev,narocnost, url_adresa budou atributy metody __init__, tedy uzivatel si je muze zvolit pri vytvareni objektu.

# A bude mít také 3 metody:

# __str___(self)
# vraci hezky vypis receptu (necham na vas ktere atributy chcete do vypisu dat)
# zmen_narocnost(self, nova_hodnota)
# zmeni narocnost, tedy zmeni atribut narocnost na nova_hodnota
# zkusit(self)
# zmeni atribut vyzkouseno na True

# 2. Kucharka
# Bude mít 3 atributy:

# nazev - string, jmeno kucharky
# autor - string, jmeno autora kucharky
# recepty - list objektu tridy Recept, metoda __init__ ji nastavuje vzdy na prazdny seznam []
# nazev a autor budou atributy metody __init__, tedy uzivatel si je muze zvolit pri vytvareni objektu.

# A bude mít také 3 metody:

# __str___(self)
# vraci hezky vypis kucharky (necham na vas ktere atributy chcete do vypisu dat)
# pocet_receptu(self)
# vraci cislo reprezentujici pocet receptu v atributu recepty
# pridej_recept(self, recept)
# prida do atributu recepty objekt recepty ktery je v argumentu recept

class Recept:
    def __init__(self, nazev, narocnost, url_adresa):
        self.nazev = nazev
        self.narocnost = narocnost
        self.url_adresa = url_adresa
        self.vyzkouseno = False

    def __str__(self):
        return f"Recept na {self.nazev} najdete na {self.url_adresa}. Jeho míra náročnosti je {self.narocnost}. Vyzkoušeno? - {self.vyzkouseno}."

    def zmen_narocnost(self, mira_narocnosti_po_vyzkouseni):
        self.narocnost -= mira_narocnosti_po_vyzkouseni

    def zkusit(self):
        self.vyzkouseno = True

cukrovi = Recept("cukroví", 5, "www.cukrovi.cz")
cukrovi.zkusit()
cukrovi.zmen_narocnost(2)
print(cukrovi)

class Kucharka:
    def __init__(self, nazev, autor):
        self.nazev = nazev
        self.autor = autor
        self.recepty = []

    def __str__(self):
        return f"Kuchařku {self.nazev} napsal/a {self.autor}."

    def pocet_receptu(self):
        return len(self.recepty)

    def pridej_recept(self, novy_recept):
        self.recepty.append(novy_recept)

vanoce = Kucharka("Nejlepší Vánoce", "Pavlínka")
print(vanoce.pocet_receptu())
vanoce.pridej_recept("cukrovi")
print(vanoce.pocet_receptu())
print(vanoce)

# Pořád mi nejde do hlavy, co přesně dělá return. 
# Totiž v tomhle případě, proč ho u té třídy Kuchařka potřebuju u fce pocet_receptu(), aby mi to správně spočítalo ten počet, 
# ale už ho nepotřebuju např. u fce pridej_recept, 
# aby mi to ten recept připojilo k tomu seznamu.
