Herz = [[0,'♥',0]]
Karo = [[0,'♦',0]]
Pik = [[0,'♠',0]]
Kreuz = [[0,'♣',0]]
Endstapel = 0
Stapel = 0
Karte = []
End1 = 0

Stapel = input('Von welchem Stapel willst du eine Karte entnehmen:')
if Stapel in globals():
    Stapel = globals()[Stapel]

while Stapel == (Herz or Stapel == Karo or Stapel == Pik or Stapel == Kreuz) and Stapel[len(Stapel)-1][0] == 0:
    print ('Versuche es erneut')
    Stapel = input('Von welchem Stapel willst du eine Karte entnehmen:')
    if Stapel in globals():
         Stapel = globals()[Stapel]

if Stapel == (Herz or Stapel == Karo or Stapel == Pik or Stapel == Kreuz) and Stapel[len(Stapel)-1][0] == 0:
    Karte.append(Stapel[len(Stapel)-1])

Karte = Stapel[len(Stapel)-1]

Endstapel = input('Auf welchen Stapel möchtest du sie legen:')
if Endstapel in globals():
    Endstapel = globals()[Endstapel]

if Endstapel == Herz or Endstapel == Karo or Endstapel == Pik or Endstapel == Kreuz:
    End1 = Endstapel
    if Karte[0] != (Endstapel[len(Endstapel)-1][0] + 1) or Karte[1] != Endstapel[0][1]:
        while Endstapel == End1:
            print('Die Karte kann nicht auf diesen Stapel gelegt werden')
            Endstapel = input('Neuer Stapel:')
            if Endstapel in globals():
                Endstapel = globals()[Endstapel]
                                                                        