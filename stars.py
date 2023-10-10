# *******   7 Sterne
#  *****    5 Sterne
#   ***     3 Sterne
#    *      1 Stern

for laenge in range(0, 4):
    for breite in range(0, 7 - laenge):
        if breite < laenge:
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print()