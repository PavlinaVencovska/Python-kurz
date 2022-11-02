with open("text.txt", encoding="utf-8") as file:
    radky = file.readlines()

print(radky)

uprava_znamek = []

for radek in radky:
    if radek[0][1] == "ř":
        nova_znamka = radek[0][1].replace("ř", "A")

       
        # spz, km = radek.split(' )
        


# radky = [radek.split('\t') for radek in radky]
# radky = [[radek[0], float(radek[1])] for radek in radky]
# print(radky)

#replace() metoda