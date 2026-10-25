
#  Urlaubsanspruch
#
#  Für die Bestimmung des Urlaubsanspruchs der Beschäftigten einer Firma
#  soll ein Programm entwickelt werden.
#  Die Grundlage für die Berechnung des Urlaubsanspruchs
#  bildet die Betriebsvereinbarung.
#  Das Programm soll die Anzahl der Urlaubstage für
#  jeweils einen Beschäftigten berechnen.
#
#  Betriebsvereinbarung:
#  Allen Beschäftigten stehen 26 Tage Urlaub zu.
#  Minderjährige Beschäftigte erhalten 30 Tage Urlaub.
#  Beschäftigte, die älter als 55 Jahre sind, erhalten 28 Tage Urlaub.
#  Beschäftigte mit einer Behinderung ab 50 % erhalten
#  zusätzlich 5 weitere Tage Urlaub.
#  Beschäftigte mit einer Betriebszugehörigkeit von mehr als 10 Jahren
#  erhalten 2 zusätzliche Tage Urlaub.

import sys

urlaub = 26

while True:
    try:
        alter = int(input("Wie alt sind Sie? "))
        if alter < 16:
            print('Fehler! Wir beschäftigen keine Kinder!')
            sys.exit(1)
        elif alter > 65:
            print('Vielen Dank, genießen Sie ihren Ruhestand!')
            sys.exit(0)
        else:
            break   # Verlässt die Schleife, wenn die Umwandlung erfolgreich war
    except ValueError:
        print("Das war keine gültige Zahl! Bitte versuche es erneut.")
print('Alter: ', alter)

while True:
    try:
        gdb = int(input('Wie hoch ist ihr Grad der Behinderung? (0 - 100) '))
        if gdb <= 100:
            break  # Verlässt die Schleife, wenn die Umwandlung erfolgreich war
        else:
            print("Das war keine gültige Zahl! Der Wert muss zwischen 0 und 100 liegen.")
    except ValueError:
        print("Das war keine gültige Zahl! Bitte versuche es erneut.")
print('GdB: ', gdb, '%')

while True:
    try:
        zugehoerig = int(input('Wie lange sind Sie in unserem Betrieb? '))
        if zugehoerig <= (alter - 16):
            break  # Verlässt die Schleife, wenn die Umwandlung erfolgreich war
        else:
            print(f'Fehler! Sie sind zu jung um {zugehoerig} Jahre im Betrieb zu sein.')
    except ValueError:
        print("Das war keine gültige Zahl! Bitte versuche es erneut.")
print('Zugehörigkeit: ', zugehoerig)
print()

if gdb >= 50:
    urlaub += 5

if zugehoerig > 10:
    urlaub += 2

if alter < 18:
    print(f'Alter: {alter}\nGdB: {gdb} %\nZugehörigkeit: {zugehoerig}\nDer Beschäftigte bekommt {urlaub+4} Tage Urlaub!')
elif alter >= 18 and alter <= 55:
    print(f'Alter: {alter}\nGdB: {gdb} %\nZugehörigkeit: {zugehoerig}\nDer Beschäftigte bekommt {urlaub} Tage Urlaub!')
else:
    print(f'Alter: {alter}\nGdB: {gdb} %\nZugehörigkeit: {zugehoerig}\nDer Beschäftigte bekommt {urlaub+2} Tage Urlaub!')

