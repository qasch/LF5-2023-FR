# einfachen Umrechner: Tage in Stunden
# Benutzer gibt die Anzahl der Tage ein
# Programm fragt, welche Umrechnungsmethode angewandt werden soll

# Benutzereingabe: input() gibt immer einen String zurück
days = input("Bitte gib die Anzahl der Tage als einen Integer ein: ")
# print(type(days))   # -> str

# Benutzereingabe: Welche Umrechungsmethode soll angewandt werden?
choice_input = input("[1] Umrechung in Stunden, [2] Umrechung in Minuten, [3] Umrechung in Sekunden")

print(choice_input)

# explizites Casting von str nach int 
# Ergebnis muss in Variable days gespeichert werden, ansonsten wird die Variable nicht geändert
days = int(days)
# print(type(days))   # -> int

# Umrechnung
# Tage in Stunden
hours = days * 24
# Tage in Minuten
minutes = hours * 60
# Tage in Sekunden
seconds = minutes * 60

if choice_input == '1':
    print(str(days) + " Tage sind " + str(hours) + " Stunden")
elif choice_input == '2':
    print(str(days) + " Tage sind " + str(minutes) + " Minuten")
elif choice_input == '3':
    print(str(days) + " Tage sind " + str(seconds) + " Sekunden")
else:
    print("Falsche Eingabe, bitte 1, 2 oder 3 eingeben")

