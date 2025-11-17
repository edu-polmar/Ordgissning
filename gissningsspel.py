import random
def Hemligt():
    with open("Ordlista.txt", "r", encoding="utf-8") as fil:
        Ord = fil.read().splitlines()
    slump_ord = random.choice(Ord)
    return slump_ord


hemligt_ord = Hemligt() #Hämtar slumpat ord från ordlistan (filen)
gissning = ["_"] * len(hemligt_ord)
print("Det hemliga ordet har", len(hemligt_ord),"bokstäver.")


#I slutet av spelet, om man gissat rätt ord, eller förlorat alla gissningar
if "_" not in gissning:
    print("Grattis! Du gissade rätt ord:", hemligt_ord)
else: 
    print("Du förlorade! Ordet var:", hemligt_ord)