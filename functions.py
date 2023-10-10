# Funktionen in Python
#
# Um Funktionen nutzen zu können, werden immer zwei Schritte unternommen:
# 1. die Deklaration der Funktion (sozusagen die Beschreibung der Funktion, bzw. die Definietion, was die Funktion kann)
# 2. der Aurfruf/Benutzung der Funktion
#
# Es gibt Funktionen mit und ohne Paramenter und Funktionen mit oder ohne Rückgabewert

## Funktion ohne Rückgabewert und ohne Parameter

# 1. Deklaration der Funktion
def print_hello_world():
    print("Hello World")

# 2. Aufruf der Funktion
print_hello_world()


print("\n-------------------------------------------\n")

## Funktion ohne Rückgabewert mit Parameter
# Hierbei ist der *Gültigkeitsbereich* von Variablen zu beachten:
# Generell sind Variablen im gesamten Code gültig, können also von überall her aufgerufen und verändert werden.
# Werden Varaibalen aber innerhalbt von Funktionen definiert, so existieren diese nur *innerhalb* der Funktion. Es kann also 
# Variablen in- und ausserhalt einer Funktion geben, die den gleichen Bezeichner/Namen haben. Dies sind dann aber *unterschiedliche*
# Variaiblen. Parameter sind innherhalt einer Funktion lokale Variablen.

def print_my_name(name):
    print("Mein Name ist " + name)

print_my_name("Gretl")
print_my_name("Kai")
print_my_name("Peter")


print("\n-------------------------------------------\n")

# Folgende Variable ist sowohl innerhalb als auch ausserhalb der Funktionen gültig/sichtbar:
# alter = 18

def print_full_name(firstname, lastname):
    # die *gloabale* Variable alter ist jetzt im gesamten Code gültig (nicht der beste Stil aber möglich)
    global alter
    alter = 31

    # die lokale Variable alter gibt es nur innerhalb der Funktion, ausserhalb existiert sie nicht
    # alter = 42 

    print("Mein Vorname ist " + firstname)
    print("Mein Nachname ist " + lastname)
    print("Ich bin " + str(alter) + " Jahre alt")

firstname = "Karl"
lastname = "Dall"
print_full_name("Peter", "Lustig")
print(firstname)
print(alter)

print("\n-------------------------------------------\n")

def generate_age(actual_year, birth_year):
    return actual_year - birth_year

# ----------------------------------------------------------

def print_full_name_and_age(firstname, lastname, alter):
    print("Mein Vorname ist " + firstname)
    print("Mein Nachname ist " + lastname)
    print("Ich bin " + str(alter) + " Jahre alt")

# Funktionen können auch als Argumente übergeben werden
print_full_name_and_age("Gretl", "Hund", generate_age(2023, 2013))

# s.o.
# print(type(alter))

print("\n-------------------------------------------\n")

## Funktion mit Rückgabewert
def addition(x, y):
    return x + y
    print("ich werde niemals ausgeführt")

result1 = addition(1, 8)    # 9
result2 = addition(2, 3)    # 5

result3 = result1 + result2   # 14

print(result1)
print(result2)
print(result3)

print("\n-------------------------------------------\n")


