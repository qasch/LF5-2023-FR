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


def print_full_name(firstname, lastname):
    print("Mein Vorname ist " + firstname)
    print("Mein Nachname ist " + lastname)

firstname = "Karl"
lastname = "Dall"
print_full_name("Peter", "Lustig")
print(firstname, lastname)



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


