# Írjon egy programot, ami egy új változóba másol át egy karakterláncot úgy, hogy csillagot
#szúr be a karakterek közé.
#Így például, « gaston »-ból « g*a*s*t*o*n » lesz.

kiIndulóSzöveg = "gaston"
beszúrandóKarakter = "*"


szövegHossz = len(kiIndulóSzöveg)

index = 1

megváltozottSzöveg = kiIndulóSzöveg[0]

while index < szövegHossz:
    megváltozottSzöveg = megváltozottSzöveg + beszúrandóKarakter + kiIndulóSzöveg[index]
    index += 1

print(megváltozottSzöveg)