# páros és páratlan számok széttválogatása


t1 = [0,32, 5, 12, 8, 3, 75, 2, 15,112]

páros = []
páratlan = []

index = 0

while index < len(t1):
    if t1[index] % 2 == 0:
        páros.append(t1[index])

    else:
        páratlan.append(t1[index])

    index += 1

print("páros számok: ",páros,"páratlan számok: ",páratlan)