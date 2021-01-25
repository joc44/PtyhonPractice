# Írjon egy programot, ami értékeket tesz egy listába. Ennek a programnak ciklusban kell működni úgy,
#hogy mindaddig kéri az értékeket, amíg a felhasználótól úgy nem dönt, hogy befejezésként  <Entert>üt.
# A program a lista kiírásával fejeződik be.

értékek = []


érték = "Indulás"

while érték != "":
    érték = input("Írj be egy számot: ")
    if érték != "":
        értékek.append(érték)

print(értékek)




