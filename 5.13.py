#a lista legnagyobb elemének az értéke

t1 = [0,32, 5, 12, 8, 3, 75, 2, 15,112]

max = 0
index = 0

while index < len(t1):
    if t1[index] > max:
        max = t1[index]

    index += 1

print("A lista legnagyobb eleme: ",max)