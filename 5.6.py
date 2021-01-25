#Írjon   egy   programot,   ami   meghatározza,   hogy   egy  karakterlánc   tartalmazza-e  az   « e »
#karaktert.

karakterLánc = "sorugrást idéz elő"

keresettKarakter = "e"

láncHossza = len(karakterLánc)

index = 0
találat = 0

while index < láncHossza:
    if karakterLánc[index] == keresettKarakter:
        találat = 1
    index += 1

print("A keresett karakter:", keresettKarakter)

if találat == 1:
    print("Megtaláltam a keresett karaktert",keresettKarakter)
else:
    print("Nem találom a megadott karaktert a karakterláncban! ",karakterLánc)



