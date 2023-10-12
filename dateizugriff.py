# Dateizugriff

# relative Pfadangabe - ausgehend vom aktuellen Verzeichnis
# absolute Pfadangabe - ausgehend vom Wurzelverzeichnis (C: bzw. /)

path_to_file = "textdatei.txt"


# Dateiinhalt schreiben (w)
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
    text = file.readlines()  # liest ganze Datei, Ergebnis ist Liste, jede Zeile ein Element in Liste
    print(text)
    file.close()
except FileNotFoundError:
    print("ERROR: Datei konnte nicht gefunden werden")
except Exception as e:
    print("ERROR: Folgender Fehler ist aufgetreten: ", e.args[0])

