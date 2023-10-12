import random

# Zufallszahl (float) zwischen 0 und 1
zufallszahl = random.random()

# Zufallszahl (int) zwischen 1 und 49 generieren (beide inklusive)
zufallsint = random.randint(1, 49)
print(zufallsint)

# sechs Zufallszahlen generieren und einer list hinzufügen 
lottozahlen = []
for _ in range(6):
    lottozahlen.append(random.randint(1, 49))

print(lottozahlen)

# Prüfen, ob eine Zahl in einer list enthalten ist
zahlen = [10, 2, 3, 4]
if 1 in zahlen:
    print("1 ist bereits enthalten")

# Prüfen, ob ein Buchstabe in einem String enthalten ist
wort = "zebra"
if "Z" in wort:
    print("kleines z ist in zebra")


# Zufällig ein Element aus einer Liste auswählen
handgesture = ["rock", "paper", "scissors", "spock"]
print(random.choice(handgesture))

# Liste randomisieren
my_ordered_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(my_ordered_list)  # list wird 'in-place' geändert
print(my_ordered_list)


help(random.randint)