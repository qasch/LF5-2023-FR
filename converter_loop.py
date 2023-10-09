# Bewusst konzipierte Endlosschleife, damit Programm immer wieder ausgeführt wird
# Programm kann dann über bestimmte Eingabe verlassen werden.
# Einfaches Beispiel für Anwendung des break-Statements.
while True:

    print("Umrechung von gegebenen Tagen in: ")

    choice_input = input("""
    [1] Stunden
    [2] Minuten
    [3] Sekunden

    [0] Programm beenden
    
    Eingabe: """)

    days = input("Bitte gib die Anzahl der Tage als einen Integer ein: ")
    
    if days.isdigit():
        # Programmlogik
        days = int(days)
        hours = days * 24
        minutes = hours * 60
        seconds = minutes * 60

        # Ausgabe
        if choice_input == '1':
            print(str(days) + " Tage sind " + str(hours) + " Stunden")
        elif choice_input == '2':
            print(str(days) + " Tage sind " + str(minutes) + " Minuten")
        elif choice_input == '3':
            print(str(days) + " Tage sind " + str(seconds) + " Sekunden")
        elif choice_input == '0':
            break
        else:
            print("Falsche Eingabe, bitte 1, 2, 3 oder 0 eingeben")

    else:
        print("Bitte nur Ziffern eingaben.")

print("Programm beendet.")
