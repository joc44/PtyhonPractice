# Írjon egy programot, ami kiszámolja 13-sas szorzótábla első 50 tagját, de csak azokat írja ki,
#melyek 7-nek többszörösei.

count = 0


while count < 50 :
    count +=1
    if count % 7 == 0:
        print(count,count * 13)
