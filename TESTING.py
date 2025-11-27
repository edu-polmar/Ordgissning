#Funktionen för att slumpa fram ett ord från ordlistan
import random
def Hemligt():
    with open("Ordlista.txt", "r", encoding="utf-8") as fil:
        Ord = fil.read().splitlines()
    slump_ord = random.choice(Ord)
    return slump_ord

print("Välkommen till Ord-Gissningsspelet! Du ska gissa ett ord på X antal bokstäver. Du har 10 felgissningar innan det Hemliga Ordet avslöjas. Lycka till!")

#Ber dig skriva in en bokstav och gör den till en stor om du skrivit in en liten.

def Kontroll(bokstav):
    if len(bokstav) != 1 or not bokstav.isalpha():
        print("Ogiltigt tecken. Skriv en bokstav (A–Ö).")
        return False
    elif bokstav.upper() in Fel_bokstäver or bokstav.upper() in Rätt_bokstäver:
        print("Du har redan gissat på den bokstaven. Försök igen.")
        return False
    else:
        return True



hemligt_ord = Hemligt() #Hämtar slumpat ord från ordlistan (filen)
gissning = ["_"] * len(hemligt_ord)
print("Det hemliga ordet har", len(hemligt_ord),"bokstäver.")
print(" ". join(gissning))



Fel_bokstäver = []
Rätt_bokstäver = []
Antal_gissningar = 10 

while Antal_gissningar > 0: #Spel loopen
    str1 = input("Skriv en bokstav:  ")

    if str1.upper() in hemligt_ord.upper() and Kontroll(str1) == True:
        print("Rätt gissat")
        print("Gissningar kvar:", Antal_gissningar, )
        Rätt_bokstäver.append(str1.upper())
    elif str1.upper() not in hemligt_ord.upper() and Kontroll(str1) == True: 
        print("Fel gissat, försök igen!")
        Antal_gissningar -= 1
        print("Gissningar kvar:", Antal_gissningar, )
        Fel_bokstäver.append(str1.upper())

    for i, bokstav in enumerate(hemligt_ord):
        if bokstav.upper()==str1.upper():
            gissning[i]=bokstav

    print(" ".join(gissning))

    if "_" not in gissning:
        print("Grattis! Du klarade ordet:", hemligt_ord)
        break
    print( )

if Antal_gissningar == 0: #förlorare meddelande
    print("Du förlorade! Ordet var:", hemligt_ord)

#Behöver en fråga för att spela igen

