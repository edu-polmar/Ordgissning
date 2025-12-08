import random

def Hemligt(): #Slumpar fram ett slumpmässigt ord från ordlista.txt.
    with open("Ordlista.txt", "r", encoding="utf-8") as fil:
        Ord = fil.read().splitlines()
    slump_ord = random.choice(Ord)
    return slump_ord

def Kontroll(bokstav, Fel_bokstäver, Rätt_bokstäver): #Funktionen som kontrollerar att du skrivit in en bokstav, om du gissat bokstaven innan, om den är fel eller rätt.
    if len(bokstav) != 1 or not bokstav.isalpha():
        print("Ogiltigt tecken. Skriv en bokstav (A–Ö).")
        return False
    elif bokstav.upper() in Fel_bokstäver or bokstav.upper() in Rätt_bokstäver:
        print("Du har redan gissat på den bokstaven. Försök igen.")
        return False
    else:
        return True

print("Välkommen till Ord-Gissningsspelet! Du har 10 felgissningar innan ordet avslöjas.")

Fel_bokstäver = []
Rätt_bokstäver = []
Antal_gissningar = 10 

while Antal_gissningar > 0: 
    str1 = input("Skriv en bokstav:  ")

    if not Kontroll(str1):
        continue

    if str1.upper() in hemligt_ord.upper():
        print("Rätt gissat")
        Rätt_bokstäver.append(str1.upper())

    else : 
        print("Fel gissat, försök igen!")
        Antal_gissningar -= 1
        print("Gissningar kvar:", Antal_gissningar)
        Fel_bokstäver.append(str1.upper())

if Antal_gissningar == 0:
    print("Du förlorade! Ordet var:", hemligt_ord)

