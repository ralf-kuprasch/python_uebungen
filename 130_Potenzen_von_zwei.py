
# Potenzen von zwei
#
# Schreibe ein Programm, das alle Potenzen von 2 ausgibt
# deren Ergebnis kleiner als 10.000 ist.
# Hilfsmittel: Schleife, **
#
# Zusatz: Die Ausgabe soll folgendermaßen aussehen:
# 2 ** 0 = 1
# 2 ** 1 = 2
# 2 ** 2 = 4
# 2 ** 3 = 8
# 2 ** 4 = 16
# 2 ** 5 = 32
# 2 ** 6 = 64
# ...

baseNum = 2
i = 0
grenze = 10_000

while True:
    potenz = baseNum ** i
    if potenz > grenze:
        break
    print(f'{baseNum} ** {i} = {potenz}')
    i += 1