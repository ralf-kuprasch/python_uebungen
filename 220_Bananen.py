
# Bananen
#
# In einer stürmischen Sommernacht sind die drei Piraten Ray, Tom und Steve
# von ihrem Piratenschiff gespült worden.
# Glücklicherweise konnten sie sich auf eine einsame Insel retten.
# Am nächsten Morgen stellen sie fest, dass es neben reichlich Trinkwasser
# auch jede Menge Bananen und eine paar friedliche Tiere auf der kleinen Insel gibt.
#
# Da sie nichts zu essen haben, sammeln sie den ganzen Tag lang einen großen
# Haufen Bananen und wollen diesen dann später gerecht aufteilen.
#
# Jedoch bricht die Dunkelheit früher als erwartet herein, die Müdigkeit macht
# sich längst breit und so wird die Teilung auf den nächsten Tag verschoben.
#
# In der Nacht wacht Ray auf.
# Er traut den anderen beiden nicht über den Weg und möchte sich daher
# sein Drittel schon mal sichern. So zählt er die Bananen,
# teilt die gesamte Anzahl durch drei und versteckt seinen Anteil
# unweit der Quelle unter Laub und Sand. Bei seiner Rechnung ergibt
# sich ein Rest von einer Banane, die er kurzerhand einem Affen spendiert
# und sich danach wieder beruhigt Schlafen legt.
# Nur eine Stunde später erwacht Tom. Auch er will sich seinen Teil vorab sichern,
# schafft ein Drittel von den noch vorhandenen Bananen zur Seite
# und gibt eine Banane - die beim Teilen übrig bleibt - einem Affen.
# Anschließend geht auch er wieder schlafen.
# Das gleiche Schauspiel vollzieht sich später in der Nacht ein drittes Mal.
# Auch Steve wird wach und abermals erhält ein Affe eine Banane,
# da auch dieses Mal die Division nicht glatt aufgeht.
# Tags darauf sagt aus Scham keiner der Piraten etwas über den arg
# geschrumpften Haufen und so wird nochmals durch drei geteilt.
# Wieder erhält ein Affe eine Banane, da die Division nicht aufgeht.
#
# Schreibe ein Programm, das ermittelt wie viele Bananen
# die Piraten mindestens gesammelt haben.

"""
1. b = (b - 1) / 3 * 2
2. b = (b - 1) / 3 * 2
3. b = (b - 1) / 3 * 2
4. b = (b - 1) / 3
"""

def bananen_rechner():
    test = False
    for i in range(4, 500):
        string = ''
        bananen = i
        bananen_gesamt = i
        for j in range(4):
            if bananen % 3 == 1:
                if j == 3:
                    bananen = (bananen - 1) // 3
                    test = True
                    print(string + str(bananen))
                else:
                    bananen = (bananen - 1) // 3 * 2
                    string += f'{bananen}, '
            else:
                break
        if test == True:
            return bananen_gesamt
    return None

print(f'Die Piraten hatten mindestens {bananen_rechner()} Bananen.')