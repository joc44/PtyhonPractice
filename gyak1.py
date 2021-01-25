szo = input("Írj be egy szót: ")

if szo < "limonade":
    place = "megelőzi"

elif szo > "limonade":
    place = "követi"
else:
    place = "fedi"

print("A", szo, "szó", place,"a 'limonade' szót a névsorban" )