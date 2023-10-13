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


shopping_list = []
path_to_file = "shoppinglist.txt"

# Funktionsdeklarationen

def append_article_to_list(article):
    '''Artkel zur Shopping Liste hinzufügen'''
    shopping_list.append(article)


def write_article_to_file(article):
    try:
        with open(path_to_file, "a") as f:
            f.write(article + "\n")
    except FileNotFoundError:
        print("ERROR: Datei konnte nicht gefunden werden")
    except Exception as e:
        print("ERROR: Folgender Fehler ist aufgetreten: ", e.args[0])


def ask_user_for_article_to_append():
    '''Benutzer nach Artikel fragen und diesen der shopping list hinzufügen'''
    article = input("Bitte einen Artikel eingeben, der der Einkaufsliste hinzugefügt werden soll: ")
    # append_article_to_list(article)
    write_article_to_file(article)


def read_shopping_list():
    try:
        with open(path_to_file, "r") as sl:
            article_list = sl.readlines()
        for article in article_list:
            print(article.strip('\n'))
    except FileNotFoundError:
        print("ERROR: Datei konnte nicht gefunden werden")
    except Exception as e:
        print("ERROR: Folgender Fehler ist aufgetreten: ", e.args[0])


def delete_article_from_file(article_name):
    with open(path_to_file, 'r') as sl:
        article_list = sl.readlines()

    if article_name + '\n' not in article_list:
        print("\n Fehler: Der angegebene Artikel konnte nicht in der Liste gefunden werden.")
        return

    with open(path_to_file, 'w') as sl:
        for article in article_list:
            if article.strip('\n') != article_name:
                sl.write(article)


def print_shopping_list():
    print("Inhalt der Einkaufsliste: \n")
    for index, article in enumerate(shopping_list):
        print("[" + str(index + 1) + "]", article)


# Artikle aus Liste entfernen
# pop() nutzen, da Benutzer später nur Index angeben soll, nicht Namen des Artikels
def remove_article_from_list(index):
    shopping_list.pop(index)


def ask_user_for_article_to_remove():
    '''Benutzer nach Artikel fragen und diesen aus der shopping list entfernen'''
    # article_index = input("Bitte den Index des Artikels eingeben, der aus der Einkaufsliste entfernt werden soll: ")
    article_name = input("Bitte den exakten Namen des Artikels eingeben, der aus der Einkaufsliste entfernt werden soll: ")
    try:
        # remove_article_from_list(int(article_index) - 1)
        delete_article_from_file(article_name)
    except IndexError:
        print("\nERROR: Unter dem angegebenen Index ist kein Artikel in der Liste zu finden")
    except ValueError:
        print("\nERROR: Bitte einen passenden Index als Ziffer angeben")
    except Exception as e:
        print("\nERROR: Folgender Fehler ist aufgetreten: " + e.args[0])


# Funktionsaufrufe - Logik unseres Skripts

# Benutzer nach Aktion fragen

print("--- Dies ist eine simple aber coole Einkaufsliste ---\n")

menu_txt = """
Was möchtest du machen:

      [1] Artikel hinzufügen
      [2] Shopping Liste anzeigen
      [3] Artikel entfernen
      ---------------------
      [4] Programm beenden

"""


while True:
    user_input = input(menu_txt + "\n")
    if user_input == '1':
        ask_user_for_article_to_append()
    elif user_input == '2':
        # print_shopping_list()
        read_shopping_list()
    elif user_input == '3':
        ask_user_for_article_to_remove()
    elif user_input == '4':
        exit(0)  # erfolgreich beendet
    else:
        print("Ungültige Eingabe")
        # exit(1)  # nicht erfolgreich beendet


