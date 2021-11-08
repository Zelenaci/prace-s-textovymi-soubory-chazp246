############################################################################
# Soubor:  main.py
# Datum: 8.11. 2021
# Autor: Jakub Zahálka - 4B
############################################################################
from random import randint, choice

soubor = input("Zadej jmeno souboru: ")

def pocitadlo(soubor):
    try:
        f = open(soubor, "r")
    except FileNotFoundError:
        print("Tento soubor nelze otevřít!")
        exit(1)

    pocet = {}

    while True:
        pismeno = f.read(1).lower()
        if pismeno == "":
            break
        if pismeno.isalpha():
            try:
                pocet[pismeno] += 1
            except:
                pocet[pismeno] = 1

    for key in sorted(pocet.keys()):
        mapovany = 50 * pocet[key] / max(pocet.values()) #maximum * tvoje hodnota co chceš namapovat / maximum co dosahl tvoje hodnoty
        bar = int(mapovany) * "#" 
        print(f"{key} -----> {pocet[key]:7} | {bar}")

    f.close()

pocitadlo(soubor)