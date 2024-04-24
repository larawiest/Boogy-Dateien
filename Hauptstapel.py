s1 = [[]]
s2 = [[],[]]
s3 = [[],[],[]]
s4 = [[],[],[],[]]
s5 = [[],[],[],[],[]]
s6 = [[],[],[3],[3],[3],[3]]
s7 = [[],[],[],[],[],[],[]]
Karte = []
i = 0
j = 0

Stapel = input('Von welchem Stapel willst du eine Karte entnehmen:')
if Stapel in globals():
    Stapel = globals()[Stapel]

if Stapel == s1 or Stapel == s2 or Stapel == s3 or Stapel == s4 or Stapel == s5 or Stapel == s6 or Stapel == s7:
    Stellekarten = int(input('Welche Karten (gib Stelle an)):'))
    j = Stellekarten 
    while j < len(Stapel):
        Karte.append(Stapel[j]) 
        j = j + 1
        print(Karte)                                                                                    

Endstapel = input('Auf welchen Stapel möchtest du sie legen:')
if Endstapel in globals():
    Endstapel = globals()[Endstapel]

if Endstapel == s1 or Endstapel == s2 or Endstapel == s3 or Endstapel == s4 or Endstapel == s5 or Endstapel == s6 or Endstapel == s7:
    while i < len(Karte):
        print(8)