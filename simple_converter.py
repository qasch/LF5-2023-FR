# einfachen Umrechner: Tage in Stunden

# Benutzereingabe: input() gibt immer einen String zurück
days = input("Bitte gib die Anzahl der Tage als einen Integer ein: ")
print(type(days))   # -> str

# explizites Casting von str nach int 
# Ergebnis muss in Variable days gespeichert werden, ansonsten wird die Variable nicht geändert
days = int(days)
print(type(days))   # -> int

# Umrechnung
hours = days * 24

# mehrere Argumente durch Komma getrennt
print(days, "Tage sind", hours, "Stunden")

# Kombination von Variablen und Strings mit + Operator (Konkatenationsoperator)
print(str(days) + " Tage sind " + str(hours) + " Stunden")

