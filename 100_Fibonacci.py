
# Fibonacci

"""
Schreibe ein Programm, das per for-Schleife die ersten 10 Zahlen der
Fibonacci-Folge ausgibt: 0 1 1 2 3 5 8 13 21 34
Die ersten beiden Zahlen dürfen hart-codiert ausgegeben werden:
print(0, 1)
Alle folgenden Zahlen müssen dann in der for-Schleife ausgegeben werden.
Die Fibonacci-Folge beginnt mit 0 und 1.
Ab dann entsteht die folgende Zahl,
indem man jeweils die beiden vorherigen Zahlen addiert.

Zusatz: Gib alle Fibonacci Zahlen unter 500 aus
"""
j = 0
k = 1
for i in range(0, 10):
    print(j, end=' ')
    summe = j + k
    k = j
    j = summe
