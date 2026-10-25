
# Ulam

# Berühmt ist die (3a + 1)-Folge des amerikanischen Mathematikers Ulam.
# Sie ist durch folgenden Algorithmus definiert:
#
# 1. Beginne mit einem Startwert a.
# 2. Wenn a == 1 ist, stoppe.
# 3. Ist a gerade, setze a = a/2,
#    sonst setze a = 3*a + 1 und fahre mit 2. fort.
#
# Bis heute weiß man nicht,
# ob die Ulam-Folge bei jedem Startwert a zum Stoppen kommt.
#
# Entwickle zu dem Algorithmus eine Funktion
# und teste sie mit verschiedensten Startwerten für a.

import sys

def ulam(zahl):
    a = zahl
    if a == 1:
       # print(a)
        return a
    elif a % 2 == 0:
        a = a/2
        print(a)
        ulam(a)
    else:
        a = 3*a + 1
        print(a)
        ulam(a)

def neue_frage():
    neuefrage = input('Eine weitere Zahl eingeben? (ja / nein) ')
    neuefrage = neuefrage.strip().lower()
    if neuefrage == 'ja':
        i = 1
        return i
    elif neuefrage == 'nein':
        i = 0
        return i
    else:
        print('Ungültige Eingabe!')
        return neue_frage()

def run_ulam():
    i = 1
    while i == 1:
        neue_zahl = input('Bitte gib eine Zahl ein: ')
        neue_zahl = int(neue_zahl.strip())
        ulam(neue_zahl)
        i = neue_frage()



run_ulam()

