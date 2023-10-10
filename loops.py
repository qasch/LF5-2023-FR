# Loops in Python

## While-Loop

# Bei einem while-Loop müssen wir zwingend darauf achten, dass die Abbruchbedingung
# auch eintritt. Ansonsten bauen wir einen Endlos-Loop (Dies kann unter Umständen auch
# gewünscht sein).
# Wird eine Zählvariable verwendet, so muss diese *ausserhalb* des Loops deklariert und 
# initialisiert werden und *innherhalb* des Loops in- bzw. dekrementiert werden.

# Einfacher while-Loop mit Zählvariable

# zahl = 6   # Zählvariable
# while zahl < 1:
#     print(zahl)
#     # zahl = zahl + 1     # Inkrement
#     zahl += 1             # Kurzschreibweise Inkrement
#     # zahl = zahl - 1     # Dekrement
#     # zahl -= 1

# While-Loop mit else
# Analog zum if-else kann auch ein while-Loop einen else-Zweig enthalten.
# Dieser wird dann ausgeführt, wenn die Bedingugn *nicht (mehr)* zutrifft.

# nummer = 2
# while nummer < 4:
#     print(nummer)
#     nummer += 1
# else:
#     print(str(nummer) + " ist nicht kleiner als 4")


# While-Loop mit break
# Wird das Schlüsselwort *break* erreicht, so wird die Schleife verlassen
# ziffer = 0
# while ziffer <= 100:
#     print(ziffer)
#     ziffer += 5
#     if ziffer == 50:
#         print("ziffer ist gleich 50, Schleife wird verlassen")
#         break

# While-Loop mit continue
# Wird das Schlüsselwort *continue* erreicht, springen wir an den Anfang der Schleife
# -> Ausgabe aller ungeraden Zahlen
# number = 0
# while number < 20:    
#     number += 1
#     if number % 2 == 0:
#         continue
#     print(number)


# for-Loop
# for count in range(10):      # Angabe Endwert (exklusiv)
#     print(count)

# for count in range(1, 10):   # Angabe Startwert (inklusiv) und Endwert (exklusiv)
#     print(count)


for count in range(1, -10, -1):   # Angabe Startwert (inklusiv) und Endwert (exklusiv)
    print(count)

# Analoges Beispiel in Java:
# for(int i = 0; i < 10; i++){
#     print i
# }


# for count in range(start, end, step):
#     print(count)


# Beispiel für for-Loop
# my_string = "hallo"
# for character in my_string:
#     print(character)
