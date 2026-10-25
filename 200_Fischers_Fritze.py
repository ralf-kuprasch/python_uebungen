
# Fischers Fritze

# Es steht folgender String zur Verfügung:
satz = 'Fischers Fritz fischt frische Fische'

# Gib durch String-Slicing des Strings 'satz' die folgenden Strings aus
# 1. ihsrzihf
# 2. sifhrhi
# 3. sche (mit möglichst wenig Zeichen)
# 4. eci hsr hsfziFseci
# 5. ii i

# 1.

i = 0
j = 0

for b in satz:
    i += 1
    if b == 'f':
        j += 1
        if j == 2:
            break

verschnitt1 = satz[1:i:3]
print('1.', verschnitt1, end='')
print('\n')

# 2.
verschnitt2 = satz[7:len(satz)-1:4]
print('2.', verschnitt2)
print()

# 3.
print('3.', satz[2:6])
print()

# 4.
num = len(satz)
verschnitt4 = satz[num:0:-2]
print('4.', verschnitt4)

# 5.
verschnitt5 = satz[11:22:5]+satz[1]
print('5.', verschnitt5)

