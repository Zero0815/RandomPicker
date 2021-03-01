from random import randint
import time

__author__ = "Dennis Ludolph"
__credits__ = ["Dennis 'Zero' Ludolph"]
__version__ = "1.0.1"
__maintainer__ = "Dennis Ludolph"
__email__ = "dennis.ludolph@gmx.de"
__status__ = "Production"
__name__ = 'Randompicker'
__date__ = '01.03.2021'

# Abfrage der Ziehung - Case Sensitive!
aktion = input('Was möchtest du machen?\n' +
               'name für Namepicker oder number für Numberpicker!\n')

# Möchte der Nutzer eine Namensziehung wird diese Aktion ausgeführt
if aktion == 'name':
    anzahl = input('Wieviele Namen?\n')  # Abfrage der Anzahl der Namen.
    zaehler = 0  # Zähler, damit sich die Schleife terminiert und nicht unendlich oft läuft.
    namen = []  # Liste in die die Namen eingetragen werden.

    # Solange der Zähler nicht die gewünschte Anzahl an Namen erreicht hat, läuft die Schleife weiter.
    while zaehler != int(anzahl):
        name = input('Name: ')  # Variablen erstellung mit Wertzuweisung (Namen) des Users.
        namen.append(name)  # Variable name wird der Liste hinzugefügt.
        zaehler += 1  # Zähler zählt um 1 hoch.

    """
    Zieht eine zufällige Zahl im Bereich vom ersten Eintrag (0 = 1, da bei 0 angefangen wird zu zählen)
    und der Anzahl der Namen (wurde oben erfragt) 
    """
    ziehung = randint(0, int(anzahl))

    # Gibt die Textmeldung aus.
    print('Ziehung erfolgt!\n' +
          'Bitte warten...')

    # Programm wartet für 5 Sekunden.
    time.sleep(5)

    # Gibt gezogenen Namen aus.
    print(namen[ziehung])

    # Programm wartet 10 Sekunden, damit man den Namen lesen kann.
    time.sleep(10)

# Möchte der Nutzer eine Nummernziehung wird diese Aktion ausgeführt
elif aktion == 'number':

    # Bereich der Zahlen von 1 bis x wird definiert
    anzahl = input('Wieviel Zahlen?\n')

    # Zieht eine Zahl von 1 bis zur gewünschten Anzahl
    ziehung = randint(1, int(anzahl))

    # Gibt Textmeldung aus
    print('Ziehung erfolgt!\n' +
          'Bitte warten...')

    # Programm wartet für 5 Sekunden
    time.sleep(5)

    # Gibt gezogene Zahl aus
    print(ziehung)

    # Programm wartet für 10 Sekunden, damit man die Zahl lesen kann.
    time.sleep(10)

# Fragt ob Wiederholungen gewünscht sind.
wiederholungen = input('Möchtest du noch weitere Ziehungen durchführen?\n' +
                       'Ja oder Nein: ')

# Sind Wiederholungen gewünscht wird diese Aktions ausgeführt.
if wiederholungen == 'Ja':

    # Abfrage nach Anzahl der Wiederholungen
    haeufigkeit = input('Wieviele Wiederholungen ?\n')

    # Zähler, damit keine Endlosschleife entsteht.
    zaehler_wdh = 0

    # Solange der Zähler noch nicht mit der gewünschten Anzahl übereinstimmt wird der Code ausgeführt.
    while zaehler_wdh != int(haeufigkeit):

        aktion = input('Was möchtest du machen?\n' +
                       'name für Namepicker oder number für Numberpicker!\n')

        if aktion == 'name':
            anzahl = input('Wieviele Namen?\n')
            zaehler = 0
            namen = []
            while zaehler != int(anzahl):
                name = [input('Name: ')]
                namen.append(name)
                zaehler += 1

            ziehung = randint(0, int(anzahl))

            print('Ziehung erfolgt!\n' +
                  'Bitte warten...')

            time.sleep(5)

            print(namen[ziehung])

            time.sleep(10)

            # Wiederholungszähler erhöt sich um 1
            zaehler_wdh += 1

        elif aktion == 'number':
            anzahl = input('Wieviel Zahlen?\n')

            ziehung = randint(1, int(anzahl))

            print('Ziehung erfolgt!\n' +
                  'Bitte warten...')

            time.sleep(5)

            print(ziehung)

            time.sleep(10)

            # Wiederholungszähler erhöt sich um 1
            zaehler_wdh += 1

        else:
            # User wird auf Eingabefehler hingewiesen. Zähler bleibt gleich.
            print('Eingabefehler!\n')

# Wünscht man keine Wiederholung wird diese Aktion ausgeführt
elif wiederholungen == 'Nein':

    # Informationstext für den User
    print('Alles klar, das Programm beendet sich in 5 Sekunden selbst!')

    # Programm wartet 5 Sekunden
    time.sleep(5)

    # Exitausgabe für die Konsole beim Schließen (bleibt bei python ./RandomPicker.py in der Konsole stehen)
    exit('Keine neuen Aktionen gewünscht.')