Karten = []
Karte = []

Stapel = input('Von welchem Stapel willst du eine Karte entnehmen:')
if Stapel in globals():
    Stapel = globals()[Stapel]

if Stapel == Karten:
    while Karten == [] and Stapel == Karten:
        print('Karten sind leer. Versuche es erneut')
        Stapel = input('Von welchem Stapel willst du eine Karte entnehmen:')
        if Stapel in globals():
            Stapel = globals()[Stapel]
    if Stapel == Karten:
        Stellekarten = int(input('Welche Karten (gib Stelle an)):'))
        Karte.append(Karten[Stellekarten])

Endstapel = input('Auf welchen Stapel möchtest du sie legen:')
if Endstapel in globals():
    Endstapel = globals()[Endstapel]

while Endstapel == Karten:
    print('Du kannst hier keine Karten ablegen. versuche es erneut')
    Endstapel = input('Neuer Stapel:')
    if Endstapel in globals():
        Endstapel = globals()[Endstapel]