# Skript für eine einfache Einkaufsliste
#    -> dazu brauch ich eine list
#
# grundlegende Funktionen:
# - [x] 1. Artikel der Liste hinzufügen   -> append()? insert()? -> vielleicht wenn wir Artikel ordnen wollen
#   - [ ] 1.1 Artikel über input() Funktion hinzufügen: Geht immer nur ein Arikel oder mehrere auf einmal?
# - [x] 2. Einkäufe/Artikel auflisten     -> for - Loop verwenden
# - [x] 3. Artikel aus der Liste entfernen -> remove()? pop()? -> Rückmeldung, gute Idee!
#   - [x] User soll Index angeben, nicht Name des Artikels
# NOTE: Beim Beenden des Skripts wird die Einkaufsliste gelöscht -> später Inhalt in Datei/Datenbank speichern
# --------
#
# weiterführende Funktionen:
# - Anzahl der Artikel soll angegeben werden können
# - Anzahl der Artikle ändern
#
# --------
#
# Wunschfunktionen:
# - Wie ist das eigentlich mit Gramm bzw. Gewichtsangaben? -> TODO später
# - Einkäufe gruppieren (List in List?)


print("Dies ist eine Einkaufsliste (hoffentlich...)")

shopping_list = []

# Funktionsdeklarationen

def append_article_to_list(article):
    '''Artkel aus der Shopping Liste entfernen'''
    shopping_list.append(article)


def ask_user_for_article_to_append():
    '''Benutzer nach Artikel fragen und diesen der shopping list hinzufügen'''
    article = input("Bitte einen Artikel eingeben, der der Einkaufsliste hinzugefügt werden soll: ")
    append_article_to_list(article)




# shopping list ausgeben
def print_shopping_list():
    print("Inhalt der Einkaufsliste: ")
    for index, article in enumerate(shopping_list):
        print("[" + str(index + 1) + "]", article)

# Artikle aus Liste entfernen
# pop() nutzen, da Benutzer später nur Index angeben soll, nicht Namen des Artikels
def remove_article_from_list(index):
    shopping_list.pop(index)


# Funktionsaufrufe

# append_article_to_list("Gurken")
# append_article_to_list("Tomaten")
# append_article_to_list("Bier")

ask_user_for_article_to_append()

print_shopping_list()

remove_article_from_list(0)

print_shopping_list()


# - Gurken
# - Tomaten
# - Bier 
