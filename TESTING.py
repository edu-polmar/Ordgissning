import random

def Hemligt():
    with open("Ordlista.txt", "r", encoding="utf-8") as fil:
        Ord = fil.read().splitlines()
    slump_ord = random.choice(Ord)
    return slump_ord

def Kontroll(bokstav, Fel_bokstäver, Rätt_bokstäver):
    if len(bokstav) != 1 or not bokstav.isalpha():
        print("Ogiltigt tecken. Skriv en bokstav (A–Ö).")
        return False
    elif bokstav.upper() in Fel_bokstäver or bokstav.upper() in Rätt_bokstäver:
        print("Du har redan gissat på den bokstaven. Försök igen.")
        return False
    else:
        return True
    
print("Välkommen till Ord-Gissningsspelet! Du har 10 felgissningar innan ordet avslöjas.")

while True:  # Yttre loop för "spela igen"
    Fel_bokstäver = []
    Rätt_bokstäver = []
    Antal_gissningar = 10
    hemligt_ord = Hemligt()
    gissning = ["_"] * len(hemligt_ord)
    
    print("\nDet hemliga ordet har", len(hemligt_ord), "bokstäver.")
    print(" ".join(gissning))

    while Antal_gissningar > 0:
        str1 = input("Skriv en bokstav:  ")

        if not Kontroll(str1, Fel_bokstäver, Rätt_bokstäver):
            continue  # Hoppa över iterationen om bokstaven inte är giltig

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

        print(" ".join(gissning))
        print("Gissningar kvar:", Antal_gissningar)
        print("Felgissade bokstäver:", Fel_bokstäver)

        if "_" not in gissning:
            print("Bra jobbat! Du gissade rätt ord. :", hemligt_ord)
            break

    if Antal_gissningar == 0:
        print("Du förlorade! Ordet var:", hemligt_ord)

    Spela_igen = input("Vill du spela igen? (j/n): ").lower()
    if Spela_igen != "j":
        print("Tack för att du spelade!")
        break


