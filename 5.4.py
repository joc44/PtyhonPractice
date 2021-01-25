#Írjon egy programot, ami a bankban elhelyezett 4,3 % -os kamatozású tőke 20 év alatt
#felhalmozódott évi kamatait számolja ki.



tőke = 12000000

kamat = 0.043

év = 1

while év < 21:
    tőke = tőke * kamat
    print(év,tőke)
    év += 1
