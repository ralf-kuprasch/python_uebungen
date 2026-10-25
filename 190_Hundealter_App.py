
# Hundealter

# Hundeliebhaber stellen sich häufig die Frage,
# wie alt ihr Hund wohl wäre, wenn er kein Hund, sondern ein Mensch wäre.
# Landläufig rechnet man Hundejahre in Menschenjahre um,
# indem man das Alter des Hundes mit 7 multipliziert.
# Je nach Hundegröße und Rasse sieht die Umrechnung jedoch etwas komplizierter aus,
# z.B.:
# - Ein einjähriger Hund entspricht in etwa einem 14-jährigen Menschen.
# - 2 Jahre eines Hundes entsprechen 22 Jahre eines Menschen.
# - Ab dann entspricht ein Hundejahr jeweils 5 Menschenjahren.

# Schreibe ein Programm, das das Alter eines Hundes erfragt und dann nach obiger
# Methode berechnet, welchem Alter in Menschenjahren das entspricht.

# „Tha mi cho sgìth ri seann chù!“

def hundealter_umrechnen(num):
    alter = num
    m_alter = 0

    if alter == 1:
        m_alter = 14
    elif alter == 2:
        m_alter = 22
    elif alter >= 3:
        m_alter = (alter-2) * 5 + 22
    return m_alter

def neue_frage():
    frage = input('Eine weitere Zahl eingeben? (ja / nein) ')
    frage = frage.strip().lower()
    print()
    if frage == 'ja':
        return 1
    elif frage == 'nein':
        return 0
    else:
        print('Ungültige Eingabe!')
        return neue_frage()

def hundealter_programm():
    i = 1
    print('Herzlich Willkommen bei "Seann Chù", ihrem Hundealter-Rechner!')
    print()
    while i == 1:
        alter = int(input('Wie alt ist Ihr Hund? '))
        menschen_alter = hundealter_umrechnen(alter)
        print(f'Das Alter des Hundes wäre in Menschenjahren: {menschen_alter} Jahre')

        i = neue_frage()
    print('Vielen Dank und Aufwiedersehen!')


hundealter_programm()
