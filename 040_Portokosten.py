
# Portokosten

"""
Die Portokosten (Versandkosten) sind wie folgt festgelegt:
Unter 39.99 € Bestellwert kosten 3.99 € Porto
40 - 69.99 € Bestellwert kosten 2.99 € Porto
70 - 99.99 € Bestellwert kosten 1.99 € Porto
ab 100 € ist portofrei

Es soll eine Zufallszahl (bestellwert)
von 1.00 - 130.00 erzeugt werden (z.B. 40.47, 123.78)

Dann soll ermittelt werden,
wie hoch die entsprechenden Portokosten sind.
Am Ende sollen der Bestellwert, die Portokosten
und der Gesamtbetrag ausgegeben werden.
"""

import random
import math

def runden(f):
    ergebnis = math.floor(f * 100 + 0.5) / 100
    return ergebnis

rFloor = random.uniform(1.00, 130.00)
order = runden(rFloor)

porto1 = 3.99
porto2 = 2.99
porto3 = 1.99

if order <= 39.99:
    print(f'Der Bestellwert beträgt {order} €.\nDie Portokosten betragen {porto1} €.\nDie Gesamtkosten betragen {runden(order + porto1):.2f} €.\n')
elif order <= 69.99:
    print(f'Der Bestellwert beträgt {order} €.\nDie Portokosten betragen {porto2} €.\nDie Gesamtkosten betragen {runden(order + porto2):.2f} €.\n')
elif order <= 99.99:
    print(f'Der Bestellwert beträgt {order} €.\nDie Portokosten betragen {porto3} €.\nDie Gesamtkosten betragen {runden(order + porto3):.2f} €.\n')
else:
    print(f'Der Bestellwert beträgt {order} €.\nDer Versand ist Portofrei.\nDie Gesamtkosten betragen {order} €.\n')