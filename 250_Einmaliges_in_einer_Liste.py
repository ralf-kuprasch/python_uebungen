import random
from random import randint, shuffle

# Einmaliges in einer Liste

"""
Schreibe eine Funktion,
die eine Liste mit neun zufälligen Zahlen befüllt und zurückgibt.
Dabei sollen vier Zahlen doppelt vorkommen und eine Zahl nur einmal.

Dann mische die Liste per random.shuffle() und schreibe eine zweite Funktion,
die aus dieser Liste die Zahl findet, die nur einmal vorkommt.
"""


def mache_zufalls_liste():
    zufalls_liste = []
    test = 0
    i = 0

    while len(zufalls_liste) < 9:
        if len(zufalls_liste) == 0:
            zufalls_liste.append(randint(0, 100))
        else:
            temp = randint(0, 100)
            if temp not in zufalls_liste:
                zufalls_liste.append(temp)
                zufalls_liste.append(temp)

    random.shuffle(zufalls_liste)

    for v in zufalls_liste:
        print(v, end=" ")
    print()

    return zufalls_liste

def finde_einmalige(l):
    liste = l
    tmp = None

    for x in liste:
        if liste.count(x) == 1:
            tmp = x
    return tmp

unikat= finde_einmalige(mache_zufalls_liste())
print(unikat)