

liste = [7, 3, 10, 0, 5, 2, 8, 1, 4, 6, 9, 3]
gesucht = 12


def suche_element(daten, gesucht):
    for i in range(len(daten)):
        if daten[i] == gesucht:
            return daten[i]
    else:
        print("Der gesuchte Wert ist nicht in den Daten enthalten.")

    return None

def sort_liste(daten):
    for i in range(1, len(daten)): #ab 1, da stelle 0 von anfan "vorsortiert" ist
        wert = daten[i]
        j = i - 1 #index des linken Nachbarn

        while j >= 0 and daten[j] > wert:
            daten[j + 1] = daten[j]
            j -= 1
        
        daten[j + 1] = wert
    return daten



sortierung = sort_liste(liste.copy())
print(sortierung)


ergebnis = suche_element(liste, gesucht)
if ergebnis is not None:
   print(f"Die gesuchte Zahl {gesucht} ist in den Daten enthalten")