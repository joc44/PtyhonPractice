#Írjon egy programot, ami kiíratja a 7-es szorzótábla első 20 tagját, csillaggal jelölve azokat,
#amelyek 3-nak többszörösei.
#Példa :   7   14   21 * 28   35   42 * 49

count = 0



while count < 20:
    count +=1
    print(count, count * 7)
    if count % 3 == 0:
        print("*")
