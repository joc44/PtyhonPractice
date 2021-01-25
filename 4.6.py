#Írjon egy programot, ami átszámolja a kiindulásként megadott egészszámú másodpercet
#évekké, hónapokká, napokká, percekké és másodpercekké.
#(Használja a modulo operátort : % ).



kiindulás = 40803612

napMp = 3600 * 24
hónapMp = napMp * 30
évMp = napMp * 365

év = kiindulás//évMp
év_maradék = kiindulás % évMp

hónap = év_maradék // hónapMp
hónap_maradék = év_maradék % hónapMp

nap = hónap_maradék // napMp
nap_maradék = hónap_maradék % napMp

óra = nap_maradék // 3600
óra_maradék = nap_maradék % 3600

perc = óra_maradék // 60
perc_maradék = óra_maradék % 60

mp = perc_maradék // 60




print(év,"év",hónap,"hónap",nap,"nap",óra,"óra",perc,"perc",mp,"másodperc")

