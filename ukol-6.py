with open("text.txt", encoding="utf-8") as file:
    radky = file.readlines()

uprava = []

for radek in radky[1:]:
    uprava = radek.replace("1", "A").replace("2", "B").replace("3", "C").replace("4", "D").replace("5", "F")
    print(uprava) 

with open("text.txt", mode="w", encoding="utf-8") as file:
    file.writelines(uprava)

