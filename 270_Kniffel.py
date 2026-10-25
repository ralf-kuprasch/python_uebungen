
# Kniffel

# Verwende einen Zufallszahlengenerator
# um Würfelergebnisse (1-6) zu simulieren.
# Werfe nun 5 Würfel und bilde die Augensumme.
# Spiele dieses Experiment 1000 Mal durch
# und ermittel, wie oft jede mögliche Augensumme
# (Minimum = 5, Maximum = 30) vorgekommen ist.
# Gib das Ergebnis wie unten optisch aus.


"""
05->
06->
07->xx
08->xxxxx
09->xxxxxxxxx
10->xxxxxxxxxxxxx
11->xxxxxxxxxxxxxxxxxxxxxxxxxxx
12->xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
13->xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
14->xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
15->xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
16->xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
17->xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
18->xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
19->xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
20->xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
21->xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
22->xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
23->xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
24->xxxxxxxxxxxxxxxx
25->xxxxxxxxxxxxxxxx
26->xxxxxxxxxxx
27->xxxxx
28->xx
29->xx
30->
"""

import random
from random import randint

def zufalls_generator():

    würfel_summen = []
    augensumme = 0

    for i in range(1000):
        würfel_liste = []
        for j in range(5):
            neue_zahl = randint(1, 6)
            würfel_liste.append(neue_zahl)
            # print(würfel_liste[j], end=" ")
        # print()
        augensumme = sum(würfel_liste)
        würfel_summen.append(augensumme)

    return würfel_summen

print(zufalls_generator())
print()


def statistik_augen(a):
    w_summen = a
    menge_liste = []
    list_summe = list(range(5,31))

    for x in list_summe:
        menge_liste.append({x:w_summen.count(x)})

    for d in menge_liste:
        for augen, anzahl in d.items():
            if augen < 10:
                print(('0'+str(augen)+'->'),end='')
            else:
                print((str(augen) + '->'), end='')
            print(anzahl * 'x')



statistik_augen(zufalls_generator())



