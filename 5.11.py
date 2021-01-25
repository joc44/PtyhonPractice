t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = ['Január', 'Február', 'Március', 'Április', 'Május', 'Június',
 'Július', 'Augusztus', 'Szeptember', 'Október', 'November', 'December']

t3 =[]

index = 0

while index < len(t1):
    t3.append(t2[index])
    t3.append(t1[index])
    index += 1

print(t3)

