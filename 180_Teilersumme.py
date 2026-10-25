
# Teilersumme

"""
Schreibe eine Funktion, die überprüft, ob bei einer Zahl
die Summe aller Teiler kleiner als die Zahl ist.
Die Zahl selber soll hierbei nicht zu den Teilern zählen.

Bei 81 würde True zurückgegeben werden, da
1 + 3 + 9 + 27 = 40
und 40 < 81

Bei 80 würde False zurückgegeben werden, da
1 + 2 + 4 + 5 + 8 + 10 + 16 + 20 + 40 = 106
und 106 > 80
"""

def teilersumme_test(num):
    summe = 0
    for i in range(1, num+1):
        if i == num:
            print('=', summe)
        elif num % i == 0:
            summe += i
            print(i, '+', end=' ')
        else:
            continue
    if summe < num:
        return True
    else:
        return False

def teilersumme_in_out():
    abfrage = int(input('Bitte gib eine ganze Zahl ein: '))

    ergebnis = teilersumme_test(abfrage)
    if ergebnis == True:
        print('Die Teilersumme ist kleiner als',abfrage)
    else:
        print('Die Teilersumme ist größer als', abfrage)


teilersumme_in_out()