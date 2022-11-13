with open("text.txt", encoding="utf-8") as file:
    radky = file.readlines()

uprava_znamek = []

for radek in radky[1:]:
    uprava_znamek = radek.replace("1","A").replace("2","B").replace("3","C").replace("4","D").replace("5", "F")
    print(uprava_znamek)

with open("text.txt", mode="w", encoding="utf-8") as output:
    output.writelines(uprava_znamek)