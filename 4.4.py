#Írjon egy programot, ami kiír egy 12 számból álló sorozatot, aminek minden tagja vagy
#egyenlő az előző taggal, vagy annak háromszorosa

a = 1
b = 1

while b < 13:
    print(a)
    a = a * 3
    b += 1
