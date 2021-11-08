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

def slovo(maxchars = 7):
    samohlasky = "aeiyou"
    souhlasky = "qwrtpsdfghjklzxcvbnm"
    slovo = ""
    for i in range(randint(1, maxchars)):
        if i % 2 == randint(0, 1):
            slovo = slovo + choice(souhlasky)
        else:    
            slovo = slovo + choice(samohlasky)
    return slovo 

def veta(minslovo = 3, maxslovo = 12):
    veta = ""
    for i in range(randint(minslovo, maxslovo)):
        veta = veta + slovo() + " "
    veta = (veta[:-1] + ".").capitalize()
    return veta

def text(minvet = 3, maxvet = 10):
    text = ""
    for i in range(randint(minvet, maxvet)):
        text = text + veta()
        if randint(1, 5) == 5:
            text = text + "\n"
    return text

def generator(soubor, minvet = 3, maxvet = 10):
    try:
        f = open(soubor,"w")
    except FileNotFoundError as e:
        print(f"Soubor se nepovedlo otevřít. {e.filename}")
        exit(1)
    f.write(text(minvet, maxvet))
    f.close()

def menic(soubor):
    try:
        f = open(soubor, "r")
    except FileNotFoundError as e:
        print(f"Soubor se nepovedlo otevřít. {e.filename}")
        exit(1)
    fB = open("textB.txt","a")

    while True:
        pismeno = f.read(1).lower()
        if pismeno == "a":
            pismeno = "@"
        if pismeno == "":
            break
        fB.write(pismeno)
        

    f.close()
    fB.close()


#generator(soubor)
#pocitadlo(soubor)
menic(soubor)