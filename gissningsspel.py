import random

def Hemligt():  #Slumpar fram ett slumpmässigt ord från ordlista.txt.

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
    
def Kontrollsvar(svar): #Funktionen som kontrollerar spelarens svar om den vill spela igen eller inte. Om svaret är gilltigt eller ej.
    if not svar.strip().lower().isalpha() and svar.strip().lower() not in ("j", "n"):
        print("Ogiltigt val. Skriv 'j' för ja eller 'n' för nej.")
        return False
    elif svar.strip().lower() == "j":
        return True

print(" ") 
print("Välkommen till Ord-Gissningsspelet! Du har 10 felgissningar innan ordet avslöjas.")


while True:   #Yttre loop för "spela igen" som är oändlig tills spelaren väljer att sluta spela
    Fel_bokstäver = [] #olika variabler som behövs för spelet
    Rätt_bokstäver = []
    Antal_gissningar = 10
    hemligt_ord = Hemligt()
    gissning = ["_"] * len(hemligt_ord)
    
    print("\nDet hemliga ordet har", len(hemligt_ord), "bokstäver.") #Informerar spelaren om hur många bokstäver det hemliga ordet har
    print(" ".join(gissning))


    while Antal_gissningar > 0:  #Inre loop för själva gissningsspelet
        str1 = input("Skriv en bokstav:  ")

        if not Kontroll(str1, Fel_bokstäver, Rätt_bokstäver):
            continue  #Hoppa över iterationen om bokstaven inte är giltig

        if str1.upper() in hemligt_ord.upper():
            print("Rätt gissat!")
            Rätt_bokstäver.append(str1.upper())
        else:
            print("Fel gissat, försök igen!")
            Fel_bokstäver.append(str1.upper())
            Antal_gissningar -= 1

        for i, bokstav in enumerate(hemligt_ord):
            if bokstav.upper() == str1.upper():
                gissning[i] = bokstav

        #Det som skrivs ut efter gissingsrundan
        print(" ".join(gissning))
        print("Gissningar kvar:", Antal_gissningar)
        print("Felgissade bokstäver:", Fel_bokstäver)
        print(" ")

        if "_" not in gissning: #Vinstmeddelande
            print("Bra jobbat! Du gissade rätt ord. :", hemligt_ord)  
            break

    if Antal_gissningar == 0: #Förlustmeddelande
        print("Du förlorade! Ordet var:", hemligt_ord)

    while True: #Loop för att fråga om spelaren vill spela igen tills ett giltigt svar ges
        Spela_igen = input("Vill du spela igen? (j/n): ")
        Kontrollsvar(Spela_igen)
        if Kontrollsvar(Spela_igen) == True:
            break
        elif Spela_igen.strip().lower() == "n":
            print("Tack för att du spelade!")
            exit()


