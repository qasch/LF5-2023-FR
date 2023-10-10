# Variablen

operator_str = '''
Wie möchten sie rechnen?
1. Addition
2. Subtraktion
3. Multiplikation
4. Division
                       
0. Programm Beenden
Eingabe: '''

exit_str = """
Möchten sie das Skript beenden?
1. Ja
2. Nein
Eingabe: """

# Funktionsdeklarationen

def check_if_input_is_digit(message):
    while True:
        zahleins = input(message)
        if not zahleins.isdigit():
            print ("Bitte nur Zahlen eingeben!")
        else:
            return int(zahleins)

def addition(zahleins, zahlzwei):
    return zahleins + zahlzwei

def subtraktion(zahleins, zahlzwei):
    return zahleins - zahlzwei

def multiplikation(zahleins, zahlzwei):
    return zahleins * zahlzwei

def division(zahleins, zahlzwei):
    try:
        result =  zahleins / zahlzwei
    except ZeroDivisionError as e:
        # Dieser Block wird nur ausgegeben, wenn es im try-Block zu einem Fehler kommt
        # Genauer gesagt zu einem ZeroDivisionError
        print("Es ist folgender Fehler aufgetreten: " + e.args[0])
    else:
        # Dieser Block wird nur dann ausgeführt, wenn es zu keiner Excetption kam
        print("Division war erfolgreich.")
        return result
    finally:
        # Dieser Block wird immer ausgeführt, egal ob Exception oder nicht (in diesem Fall nicht wirkich sinnvoll...)
        print("Das war die Divsion, vielleicht ist ein Fehler passiert, vielleicht auch nicht...")


# Programmlogik

while True: 
  
    #-----> Isdigit-Abfrage für Zahl 1
    zahleins = check_if_input_is_digit("Bitte die erste Zahl eingeben: ")
    #-----> Isdigit-Abfrage für Zahl 2
    zahlzwei = check_if_input_is_digit("Bitte die zweite Zahl eingeben: ")
    #-----> Abfrage Tree 
    choice = check_if_input_is_digit(operator_str)

    #------> Ausgaben
    if choice == 1:
        print("Ergebniss: " + str(zahleins) + " + " + str(zahlzwei) + " = " + str(addition(zahleins, zahlzwei)))
    elif choice == 2:
        print("Ergebniss: " + str(zahleins) + " - " + str(zahlzwei) + " = " + str(subtraktion(zahleins, zahlzwei)))
    elif choice == 3:
        print("Ergebniss: " + str(zahleins) + " * " + str(zahlzwei) + " = " + str(multiplikation(zahleins, zahlzwei)))
    elif choice == 4:
        print("Ergebniss: " + str(zahleins) + " / " + str(zahlzwei) + " = " + str(division(zahleins, zahlzwei)))
    elif choice == 0:
        break
    else:
        print("Error")
    
    # Soll Skript erneut ausgeführt werden?
    cancel = check_if_input_is_digit(exit_str)
    
    if cancel == 2:
        continue
    else:
        break