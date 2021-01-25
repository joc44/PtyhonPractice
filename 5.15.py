nevek = ['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'Jean-Pierre','Sandra']

rövidNevek = []
hosszúNevek = []

index = 0

while index < len(nevek):
    if len(nevek[index]) <= 6:
        rövidNevek.append(nevek[index])

    else:
        hosszúNevek.append(nevek[index])
    index += 1

print(rövidNevek,hosszúNevek)





