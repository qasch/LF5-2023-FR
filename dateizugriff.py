# Dateizugriff

# relative Pfadangabe - ausgehend vom aktuellen Verzeichnis
# absolute Pfadangabe - ausgehend vom Wurzelverzeichnis (C: bzw. /)

path_to_file = "textdatei.txt"


# Dateiinhalt schreiben (w)
# Streng genommen könnten wir hier auf die FileNotFound Exception verzichten, da 
# die Datei erstellt wird, falls sie nicht existiert
try:
    # Dateistrom erzeugen
    # file = open("files/textdatei.txt")    # relativer Pfad, Angabe untergeordnetes Verzeichnis files
    # file = open("../textdatei.txt")    # relativer Pfad, Angabe übergeordnetes Verzeichnis
    # file = open("C:/Schulungen/Gfn/LF5/2023/FR/code/textdatei.txt")    # absoluter Pfad
    # file = open(path_to_file, "w")    # relativer Pfad, Dateiinhalt wird überschrieben
    file = open(path_to_file, "a")    # relativer Pfad, Text wird an bestehenden Inhalt angehängt
    text = "Ich bin ein Text aus einem Python Skript"
    file.write(text)
    file.close()
except FileNotFoundError:
    print("ERROR: Datei konnte nicht gefunden werden")
except Exception as e:
    print("ERROR: Folgender Fehler ist aufgetreten: ", e.args[0])


# Dateiinhalt lesen (r)
try:
    # Dateistrom erzeugen
    file = open(path_to_file, "r")    # relativer Pfad
    # text = file.read()     # liest gesamte Datei, über Argument kann Anzahl Bytes angegeben werden    
    # text = file.readline()   # liest eine Zeile, über Argument kann Anzahl Zeichen angegeben werden
    # text = file.readlines()  # liest ganze Datei, Ergebnis ist Liste, jede Zeile ein Element in Liste
    print(text)
    file.close()
except FileNotFoundError:
    print("ERROR: Datei konnte nicht gefunden werden")
except Exception as e:
    print("ERROR: Folgender Fehler ist aufgetreten: ", e.args[0])

# Context Manager
# Der eigentlich gebräuchlichere Weg, Dateien zu lesen bzw. zu schreiben.
# So brauchen wir uns z.B. nicht um das Schliessen des Streams zu kümmern 
# Achtung: Auch hier die Exceptions nicht vergessen!

with open('textdatei.txt', 'w') as my_opend_file:
    my_opend_file.write("Diddeldidumm")

with open('textdatei.txt', 'r') as my_opend_file:
    print(my_opend_file.read())
