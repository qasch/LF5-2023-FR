# Strings sind (wie jeder andere Datentyp) Klassen in Python
# ein konkreter String, z.B. "huhu" ist also ein Objekt, eine konkrete 
# Ausprägung einer Klasse
# Objekte können Methoden aufrufen
# Dies erfolgt über die sog. Punkt-Notation:


my_string = "huhudu" 
print(my_string)

# Ein paar Beispiele für String-Methoden
# Nach Eingabe des Punkts erscheint ein Auswahltmenü
# Dies kann auch über die Tastenkombination STRG+SPACE getriggert werden
print(my_string.capitalize())   # Ersten Buchstaben gross schreiben
print(my_string.count("u"))     # Wie viele 'u' gibt es in dem String?
print(my_string.split("d"))     # Unerteilt String am angegebenen Buchstaben
print(my_string.startswith('u'))     # Beginnt der String mit einem 'u'?