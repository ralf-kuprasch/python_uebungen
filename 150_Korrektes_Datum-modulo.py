
# Korrektes Datum

"""
Die Meyer GmbH benötigt ein Modul,
das ein beliebiges Datum auf Korrektheit prüft.
Ist das zu prüfende Datum korrekt,
so ist die Variable datok auf 1, andernfalls auf 0
zu setzen.

Beispiele:

29.02.1999 - datok: 0
29.02.2000 - datok: 1
13.05.2000 - datok: 1
32.05.2000 - datok: 0
24.13.2000 - datok: 0

Für die Jahre gilt: jahr > 1900 UND jahr < 2100
"""

"""
Die Schaltjahresregel lässt sich perfekt mit Modulo abbilden,
da jahr % x == 0 prüft, ob eine Jahreszahl glatt durch x teilbar ist:
 
jahr % 4 == 0: Grundsätzlich ist jedes vierte Jahr ein Schaltjahr.
jahr % 100 != 0: Jahrhundertwenden (1700, 1800, 1900) sind keine Schaltjahre.
jahr % 400 == 0: Ist die Jahrhundertwende aber durch 400 teilbar (2000, 2400),
ist es doch ein Schaltjahr.
"""

def datums_test(str):
    str = str.strip()

    try:
        str_liste = str.split('.')
        jahr = int(str_liste[2])
        monat = int(str_liste[1])
        tag = int(str_liste[0])
        schalt_jahr = 0
        wahr = 0  # 0 steht für False

        if len(str_liste) > 3 or jahr < 1900 or jahr > 2100:
            wahr = 0
            return wahr

        if (jahr % 4 == 0 and jahr % 100 != 0) or (jahr % 400 == 0):
            schalt_jahr = 1

        if monat < 1 or monat > 12:
            wahr = 0
        else:
            wahr = 1

        m_tage_liste = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if schalt_jahr == 1 and monat == 2 and tag <= 29:
            wahr = 1
        elif tag > m_tage_liste[monat-1] or tag < 1:
            wahr = 0
        else:
            wahr = 1

    except IndexError:
        wahr = 0
    return wahr

def neue_frage():
    neuefrage = input('Ein weiteres Datum prüfen? (ja / nein) ')
    neuefrage = neuefrage.strip().lower()
    if neuefrage == 'ja':
        i = 1
        return i
    elif neuefrage == 'nein':
        i = 0
        return i
    else:
        print('Ungültige Eingabe!')
        neue_frage()

def datum_app():
    print('Hallo, dies ist Ihre Datumsprüfer-App.')
    i = 1
    while i == 1:
        inDatum = input('Bitte gib ein Datum im Format TT.MM.JJJJ ein: ')

        datok = datums_test(inDatum)
        print(datok)
        if datok:
            print('Das Datum ist korrekt!')
        else:
            print('Das Datum ist nicht korrekt!')
        print(f'{inDatum} - datok: {datok}')

        i = neue_frage()

datum_app()


