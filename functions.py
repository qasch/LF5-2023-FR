# Funktionen in Python

## Funktion ohne Rückgabewert und ohne Parameter

# 1. Deklaration der Funktion
def print_hello_world():
    print("Hello World")

# 2. Aufruf der Funktion
print_hello_world()


## Funktion ohne Rückgabewert mit Parameter
def print_my_name(name):
    print("Mein Name ist " + name)

print_my_name("Gretl")
print_my_name("Kai")
print_my_name("Peter")


# alter = 18

def print_full_name(firstname, lastname):
    # Variable alter ist jetzt im gesamten Code gültig (nicht der beste Stil aber möglich)
    global alter
    alter = 31

    # lokale Variable alter gibt es nur innerhalb der Funktion, ausserhalt existiert sie nicht
    # alter = 42 

    print("Mein Vorname ist " + firstname)
    print("Mein Nachname ist " + lastname)
    print("Ich bin " + str(alter) + " Jahre alt")

firstname = "Karl"
lastname = "Dall"
print_full_name("Peter", "Lustig")
print(firstname)
print(alter)

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
print(type(alter))

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


