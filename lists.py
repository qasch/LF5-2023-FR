# Lists (Arrays) in Python

# Variablen können *einen* Wert aufnehmen
# Lists können *mehrere* Werte aufnehmen

my_str = "2 23 34 7"
print(my_str)
print(type(my_str))


my_digit_list = [2, 23, 34, 7]
print(my_digit_list)
print(type(my_digit_list))

# Index
# Element in einer List sind durch einen Index ansprechbar
# Der Index beginnt immer bei 0
# Das 1. Element einer List steht am Index 0

#     Index       0       1       2    3
my_mixed_list = [True, "Hallo", 2.34, 87]
print(my_mixed_list)

# Ausgabe des ersten Elements:
print(my_mixed_list[0])

# Ausgabe des zweite Elements:
print(my_mixed_list[1])

# Ausgabe des dritten Elements:
print(my_mixed_list[2])

# Ausgabe des vierten Elements:
print(my_mixed_list[3])

# Ausgabe des fünften Elements:
# print(my_mixed_list[4])       # -> IndexError: list index out of range - passiert immer beim 
                                #   Versuch auf ein Listenelement zuzugreifen, welches nicht existiert



my_string_list = ["Apfel", "Birne", "Mango", "Erdbeere", "Ananas", "Banane", "Kiwi"]
print(my_string_list)

# negativer Index
print(my_string_list[-1])      # letztes Element der list 
print(my_string_list[-2])      # vorletztes Element der list 

# Bereich
print(my_string_list[:3])       # Ausgabe der ersten drei Elemente
print(my_string_list[3:])       # Ausgabe aller Element ab Index 3
print(my_string_list[::])       # Ausgabe aller Elemente

# Ausgabe aller Elemente 
print("Ausgabe aller Elemente auf die dumme Art: ")
# print(my_string_list[0])
# print(my_string_list[1])
# print(my_string_list[2])
# print(my_string_list[3])
# print(my_string_list[4])
# print(my_string_list[5])
# print(my_string_list[6])


# Nicht ganz ungefährlich, Index out of range Fehler falls z.B. ein Element aus Liste entfernt wird
# print("\nAusgabe aller Elemente auf die schlauere Art: ")
# index = 0
# while index < 6:
#     print(my_string_list[index])
#     index += 1

print("\nAusgabe aller Elemente auf die noch schlauere Art: ")
index = 0
while index < len(my_string_list):
    print(my_string_list[index])
    index += 1


print("\nAusgabe aller Elemente auf die schlaueste Art: ")
for element in my_string_list:
    print(element)

