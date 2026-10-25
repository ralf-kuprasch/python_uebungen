
# Notenschnitt

"""
Schreibe ein Programm, das 20 Zeugnisnoten (1.0 bis 6.0) in Zehntel-Noten
(z.B. 4.3) zufällig erzeugt.

Verwende diese 20 Noten, um damit den relevanten Durchschnitt
nach folgendem Verfahren zu berechnen:
- streiche die beste und die schlechteste Note (statistische Ausreißer),
- ermittel den Durchschnitt der verbleibenden Noten
- runde zu halben Note (1, 1.5, 2, ..., 4.5, 5, 5.5, 6).
- Z.B.: 3.7 wird zu 3.5, 3.8 wird zu 4.0
"""

import random


def berechne_gestutztes_mittel(noten):
    if len(noten) <= 2:
        return "Nicht genügend Noten vorhanden (mindestens 3 benötigt)."

    # 1. Noten sortieren (z.B. [5.0, 2.0, 1.0, 4.0, 3.0] -> [1.0, 2.0, 3.0, 4.0, 5.0])
    noten_sortiert = sorted(noten)

    # 2. Das erste (beste) und letzte (schlechteste) Element abschneiden
    verbleibende_noten = noten_sortiert[1:-1]

    # 3. Den Durchschnitt der restlichen Noten berechnen
    durchschnitt = sum(verbleibende_noten) / len(verbleibende_noten)
    return round(durchschnitt * 2) / 2

noten_liste = []
for i in range(0, 20):
    noten_liste.append(round(random.uniform(1.0, 6.0), 1))
print(noten_liste)

gestutztes_mittel = berechne_gestutztes_mittel(noten_liste)

print(f'Der relevante Durchschnitt: {gestutztes_mittel}')