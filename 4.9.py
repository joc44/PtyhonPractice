#Írjon egy programot, ami a következő jelsorozatot írja ki :
#*
#**
#***
#****
#*****
#******
#*******


count = 0
star = "*"

while count < 7:
    print(star)
    star += "*"
    count += 1

