
# Fakultät

"""
Schreibe ein Skript, dass ermittelt,
welche Zahl möglichst groß ist,
ohne dass ihre Fakultät über 1.000.000.000 ist.

Hinweis:
Fakultät von 5 (Kurzschreibweise: 5!):
1 * 2 * 3 * 4 * 5 = 120
"""

i = 0
fakultaet = 1
fakultaet_list = []

while fakultaet <= 1_000_000_000:
    i += 1
    numList = []
    fakultaet = 1
    for j in range(1, i + 1):
        numList.append(j)
    for num in numList:
        fakultaet *= num
    fakultaet_list.append(fakultaet)

f_Zahl = len(fakultaet_list)-1

print(f'Die gewünschte Zahl ist {f_Zahl} und ihre Fakultät ist: {fakultaet_list[f_Zahl-1]}')