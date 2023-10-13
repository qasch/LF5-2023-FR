# Ausgabe von Strings und Variablen

foo = "bar"
zahl = 17
kommazahl = 3.14
wahreitswert = True

# Ausgabe mit Konkatenationsoperator +
# ACHTUNG: Alle Variablen müssen expliziet in einen String gecastet werden
# GEFAHR!
# print("In der Variable foo steht der Wert " + str(foo))

# Ausgabe mit String Format Methode
#                                                                                     Index  0  ,  1  etc
# Variablen werden impliziet in einen String gecastet
print("In der Variable foo steht der Wert {0} und in der Variablen zahl der Wert {1}".format(foo, wahreitswert))

# Ausgabe mit dem f-String
# komfortabelste und mächtigste Möglichkeit zur Ausgabe
print(f"In der Variable foo steht der Wert {foo} und in der Variablen zahl der Wert {zahl}")


