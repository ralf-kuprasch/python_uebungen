
# Passwort-Qualität

# Schreibe eine Funktion, die die Qualität von Passwörtern nach
# einem einfachen Punktesystem bewertet.
# Es gelten dabei die folgenden
# Regeln:
# – Passwort mit 7 oder weniger Zeichen: immer 0 Punkte,
# - egal, welche Kriterien noch erfüllt sind.
# – Ab 8 Zeichen: 1 Punkt.
# – Enthält sowohl Groß- als auch Kleinbuchstaben: +1 Punkt.
# – Enthält MEHR als sechs unterschiedliche Zeichen: +1 Punkt.
# – Enthält zumindest eine Ziffer: +1 Punkt.
# – Enthält zumindest ein Sonderzeichen: +1 Punkt.
# Beispiele:
# – 'abc': 0 Punkte
# – 'abcdefghij': 2 Punkte
# – 'ab1122$$!!': 3 Punkte
# – 'Abcd1234$!': 5 Punkte

def passw_quali(pw):
    punkte = 0
    word = pw
    if len(word) <= 7:
        print('Das Passwort muss mindestens 8 Zeichen haben!\n')
        return 0
    else:
        print('Das Passwort hat 8 Zeichen oder mehr. +1')
        punkte = 1

    lower = 0
    upper = 0
    for w in word:
        if w.islower():
            lower = 1
        elif w.isupper():
            upper = 1
        if lower==1 and upper==1:
            punkte += 1
            print('Das Passwort hat Groß- und Kleinbuchstaben. +1')
            break

    if len(set(word)) > 6:
        punkte += 1
        print('Das Passwort hat mehr als 6 unterschiedliche Zeichen. +1')

    for n in word:
        if n.isdigit():
            punkte += 1
            print('Das Passwort hat mindestens eine Ziffer. +1')
            break

    for m in word:
        if m.isalpha()==False and m.isdigit()==False:
            punkte += 1
            print('Das Passwort hat mindestens ein Sonderzeichen. +1')
            break

    return punkte

def neue_frage():
    frage = input('Ein anderes Passwort bewerten? (ja / nein) ')
    frage = frage.strip().lower()
    print()
    if frage == 'ja':
        return 1
    elif frage == 'nein':
        return 0
    else:
        print('Ungültige Eingabe!')
        return neue_frage()

def passwort_test_app():
    i = 1
    print('Herzlich Willkommen zu Or_Well, Ihrem Passwort-Qualitätscheck!')
    print()
    while i == 1:
        pw = input('Bitte geben Sie ein Passwort ein: ')
        word_punkte = passw_quali(pw)
        print(f'Ihr Passwort hat {word_punkte} von insgesamt 5 Punkten!')

        i = neue_frage()
    print('Vielen Dank und Aufwiedersehen!')

passwort_test_app()