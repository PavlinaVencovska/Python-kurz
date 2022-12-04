#Zadání:
#Stáhni si soubor temperature.csv, který obsahuje informace o průměrné teplotě v různých městech v listopadu 2017.
#Vypiš si prvních několik řádků, ať si prohlédneš strukturu tabulky.
import pandas as pd

teplota = pd.read_csv("temperature.csv", index_col="City")
print(teplota.info)

#Dotaz na měření, která byla provedena v Praze. Je na datech něco zvláštního?
print(teplota.loc["Prague"])

#Dotaz na měření, ve kterých je teplota (sloupec AvgTemperature) vyšší než 80 stupňů.
print(teplota[teplota["AvgTemperature"] > 80])

#Dotaz na měření, ve kterých je teplota vyšší než 60 stupňů a současně bylo měření provedeno v regionu (sloupec Region) Evropa (Europe).
print(teplota[(teplota["AvgTemperature"] > 60) & (teplota["Region"] == "Europe")])

#Dotaz na extrémní hodnoty, tj. měření, ve kterých je teplota vyšší než 80 stupňů nebo menší než - 20 stupňů.
print(teplota[(teplota["AvgTemperature"] > 80) | (teplota["AvgTemperature"] < -20)])