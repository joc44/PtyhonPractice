# Írjon   egy   programot,   ami   megszámolja  az   « e »   karakter   előfordulásainak   számát   egy
#stringben.


karakterLánc = "Megszereted e cseh remeket"

számolandóKarakter = "e"

index = 0
találatSzáma = 0

láncHossza = len(karakterLánc)

while index < láncHossza:
    if karakterLánc[index] == számolandóKarakter:
        találatSzáma +=1
    index += 1

print("A megadott szöveg ",találatSzáma, "-db ",számolandóKarakter, "-t tartalmaz.")