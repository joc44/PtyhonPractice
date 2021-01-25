# Írjon egy programot, ami euróban kifejezett pézösszegeket kanadai dollárba vált át és az
#eredményt egy táblázatba írja ki. A táblázatban a pézösszegek « geometriai haladvány »
#szerint növekedjenek úgy, mint az alábbi példában :
#1 euro = 1.65 dollar
#2 euro = 3.30 dollar
#4 euro = 6.60 dollar
#8 euro = 13.20 dollar
#stb. ( 16384 euronál kell megállni)"

euro = 1
dollar = 1.65
euroOssz = 16384

while euro <= euroOssz:
    print(euro, "euro =", dollar, "dollar")
    dollar += dollar
    euro = euro * 2


