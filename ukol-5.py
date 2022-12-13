# Zadání:
# Vytvor tridu Koronavirus ktera dedi ze tridy Nemoc a to nasledujicim zpusobem:

# Ze tridy Nemoc dedi beze zmeny chovani:

# Atribut jmeno
# Metodu zmen_pocet_obeti
# Navic pridava jeste:

# atribut varianty
# prazdny list v __init__ metode tridy Koronavirus
# metodu pridej_variantu(self, varianta)
# do atributu varianty prida novou variantu - varianty muzete specifikovat pomoci retezcu, pripadne i klidne vlastni tridou.

# Upravuje metodu tridy Nemoc:

# __str__ uprav tak aby zobrazovala obsah atributu jmeno a varianty
# v retezci budou varianty oddelene carkami tedy napriklad z listu ['omikron', 'delta'] se stane retezec 'omikron, delta' - pouzijte metodu join podle nasledujicicho prikladu:
# seznam = ['a', 'b', 'c']
# ' ,'.join(seznam)
# print(seznam) # 'a, b, c'
# Hodnoty atributu inkubacni_doba, pocet_obeti a sireni budou v __init__ metode tridy Koronavirus predane __init__ metode materske tridy (pres super().__init__(...)).

class Nemoc:
    def __init__(self, jmeno, inkubacni_doba, pocet_obeti, sireni):
        self.jmeno = jmeno
        self.inkubacni_doba = inkubacni_doba
        self.pocet_obeti = pocet_obeti
        self.sireni = sireni

    def __str__(self):
        return f'{self.jmeno} mela dosud {self.pocet_obeti} obeti.'

    def zmen_pocet_obeti(self, pocet_obeti):
        self.pocet_obeti = pocet_obeti

class Koronavirus(Nemoc):
    def __init__(self, jmeno, inkubacni_doba, pocet_obeti, sireni):
        super().__init__(jmeno, inkubacni_doba, pocet_obeti, sireni)
        self.varianty = []

    def pridej_variantu(self, varianta):
        self.varianty.append(varianta)

    def __str__(self):
        return f"{super().__str__()} Vznikla/y varianta/y {' ,'.join(self.varianty)}"

corona = Koronavirus("Corona", "tyden", "0", "primo exponencionalni")
print(corona)
chripka = Nemoc("Chripecka", "2 dny", "0", "dost snadny")
print(chripka)
corona.pridej_variantu("delta")
corona.pridej_variantu("omikron")
print(corona)