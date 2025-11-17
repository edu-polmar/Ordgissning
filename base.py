
def hemligt():
    bleh = "Python"
    return bleh

print("Du ska gissa ett ord, bokstav för bokstav, på (ANTAL) bokstäver")

hemligt()
gissade_bokstäver = []
while True:
    gissning = input("Gissa en bokstav: ").upper()
    if gissning in hemligt().upper():
        gissade_bokstäver.append(gissning)
        print("Rätt gissat!")
    else:
        print("Fel gissat, försök igen.")

    visat_ord = ""
    for bokstav in hemligt().upper():
        if bokstav in gissade_bokstäver:
            visat_ord += bokstav
        else:
            visat_ord += "_"

    print("Ord: " + visat_ord)

    if "_" not in visat_ord:
        print("Grattis! Du har gissat ordet:", hemligt)
        break