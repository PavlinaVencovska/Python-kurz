with open("vykaz.txt", "r", encoding="utf-8") as file:
    hodiny = file.readlines()

print(hodiny)

    # for radek in radky:
    #     print(radek.replace("\n", ""))
    # Nechte uživatele zadat na příkazovém řádku hodinovou mzdu. 
    # Spočítejte a na výstup vytiskněte celkovou výplatu za celý rok a 
    # průměrnou výplatu na jeden měsíc.

hodinova_mzda = int(input("Zadej hodinovku: "))

vyplata = [int(mesic) * hodinova_mzda for mesic in hodiny]

print(vyplata)

platy_k_zapisu = [str(plat) + "\n" for plat in vyplata]


# with open("vykaz.txt", "w", encoding="utf-8") as vystup:
#     # for hodnota in vyplata:
#     #     vystup.write(f"{vyplata}\n")
#     vystup.writelines(platy_k_zapisu)



#     # with open('data/vykaz.txt', 'r', encoding='utf-8') as vstup:
#     radky = [int(radek) for radek in vstup.readlines()]

# hodinova_mzda = 250
# platy = [hodinova_mzda*mesic for mesic in radky]

# # for mesic in radky:
# #     print(mesic * hodinova_mzda)

# print(platy)

# platy_k_zapisu = [str(plat) + '\n' for plat in platy]

# with open('data/mesicni_platy.txt', 'w', encoding='utf-8') as vystup:
#     # for plat in platy:
#     #     vystup.write(f'{plat}\n')
#         # vystup.write(str(plat) + '\n')
#     vystup.writelines(platy_k_zapisu)
