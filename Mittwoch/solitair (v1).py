import sys

#Sonderstapel
Herz = [[0,'♥',0]]
Karo = [[0,'♦',0]]
Pik = [[0,'♠',0]]
Kreuz = [[0,'♣',0]]

#Hauptstapel
s1 = [[3,'♣',1]]
s2 = [[2,'♦',0],[9,'♦',1]]
s3 = [[13,'♣',0],[10,'♦',0],[12,'♣',1]]
s4 = [[2,'♥',0],[4,'♣',0],[8,'♦',0],[3,'♦',1]]
s5 = [[10,'♥',0],[6,'♠',0],[1,'♦',0],[1,'♣',0],[2,'♠',1]]
s6 = [[7,'♣',0],[4,'♠',0],[12,'♠',0],[3,'♥',0],[12,'♥',0],[5,'♥',1]]
s7 = [[9,'♠',0],[6,'♦',0],[13,'♥',0],[1,'♠',0],[2,'♣',0],[10,'♠',0],[11,'♦',1]]

#Zusatzkarten
Karten = [[4,'♥',1],[4,'♦',1],[6,'♥',1],[9,'♥',1],[7,'♠',1],[9,'♣',1],[11,'♣',1],[5,'♦',1],[11,'♥',1],[5,'♠',1],[8,'♣',1],[5,'♣',1],[7,'♦',1],[8,'♠',1],[12,'♦',1],[3,'♠',1],[11,'♠',1],[6,'♣',1],[1,'♥',1],[13,'♠',1],[7,'♥',1],[13,'♦',1],[10,'♣',1],[8,'♥',1]]

#Beender
w = 0

while w == 0:

    #Variablen
    Karte = []
    Stapel = 0
    Endstapel = 0
    Stelle = -1

    #Zähler
    i = 0
    j = 0
    l = 0
    e = 0
    a = 0
    r = 0
    t = 0
    f = 0
    z = 4
    p = 0

    #Überprüfen
    End1 = 0

    #Druck Variablen
    d_Herz = []
    d_Karo = []
    d_Pik = []
    d_Kreuz = []
    d_s1 = []
    d_s2 = []
    d_s3 = []
    d_s4 = []
    d_s5 = []
    d_s6 = []
    d_s7 = []
    d_Karten = []

    alleStapel = [Herz,Karo,Pik,Kreuz,s1,s2,s3,s4,s5,s6,s7,Karten]
    allestr = ['Herz','Karo','Pik','Kreuz','s1','s2','s3','s4','s5','s6','s7','Karten']
    alleDruck = [d_Herz,d_Karo,d_Pik,d_Kreuz,d_s1,d_s2,d_s3,d_s4,d_s5,d_s6,d_s7,d_Karten]

    #1: Ausdruck der Spielkarten
    
    while e < 12:
        l = 0
        while l < (len(alleStapel[e])):
            if alleStapel[e][l][2] == 0:
                alleDruck[e].append(['_'])
            else:
                alleDruck[e].append([])
                alleDruck[e][len(alleDruck[e])-1].append(alleStapel[e][l][0])
                alleDruck[e][len(alleDruck[e])-1].append(alleStapel[e][l][1])
            l = l + 1
        print(allestr[e],':',alleDruck[e])
        e = e + 1

    #2: Eingeben von Stapel

    Stapel = input('Von welchem Stapel willst du eine Karte entnehmen:')
    if Stapel in globals():
        Stapel = globals()[Stapel]

    #3: Überprüfen ob aus Stapel entnommen werden darf

    while (Stapel == Herz or Stapel == Karo or Stapel == Pik or Stapel == Kreuz) or (Karten == [] and Stapel == Karten):
        print('Du kannst aktuell keine Karte von diesem Stapel entnehmen')
        Stapel = input('Von welchem Stapel willst du eine Karte entnehmen:')
        if Stapel in globals():
            Stapel = globals()[Stapel]

    #4: Karte entnehmnen 

    while a == 0:
        if Stapel == Karten:
            Stelle = int(input('Welche Karten (gib Stelle an)):'))
            Karte.append(Stapel[Stelle])
            a = 1
        if (Stapel == s1 or Stapel == s2 or Stapel == s3 or Stapel == s4 or Stapel == s5 or Stapel == s6 or Stapel == s7):
            Stelle = int(input('Welche Karten (gib Stelle an)):'))
            while Stapel[Stelle][0] == 0:
                Stelle = int(input('Welche Karten (gib Stelle an)):'))
            j = Stelle 
            while j < len(Stapel):
                Karte.append(Stapel[j]) 
                j = j + 1 
            a = 1

    #5: Eingeben von Endstapel

    Endstapel = input('Auf welchen Stapel möchtest du sie legen:')
    if Endstapel in globals():
        Endstapel = globals()[Endstapel]

    #6: Karte ablegen + Bedingungen
    print(Karte)

    def Ablegen (Herz, Karo, Pik, Kreuz, s1, s2, s3, s4, s5, s6, s7, Karten, Karte, Stapel, Endstapel, Stelle, i, j, l, e, a ,r,f,p):

        if f != 0:
            return
        
        f = 0
        
        while (Endstapel == Herz or Endstapel == Karo or Endstapel == Pik or Endstapel == Kreuz) and (len(Karte) > 1):
            print('Du kannst hier nur eine Karte ablegen')
            Endstapel = input('Auf welchen Stapel möchtest du sie legen:')
            if Endstapel in globals():
                Endstapel = globals()[Endstapel]
            Ablegen(Herz, Karo, Pik, Kreuz, s1, s2, s3, s4, s5, s6, s7, Karten, Karte, Stapel, Endstapel, Stelle, i, j, l, e, a ,r,f,p)
            return

        if Endstapel == Herz or Endstapel == Karo or Endstapel == Pik or Endstapel == Kreuz:
            End1 = Endstapel
            if Karte[0][0] != (Endstapel[len(Endstapel)-1][0] + 1) or (Karte[0][1] != Endstapel[0][1]):
                while Endstapel == End1:
                    print('Die Karte kann nicht auf diesen Stapel gelegt werden')
                    Endstapel = input('Neuer Stapel:')
                    if Endstapel in globals():
                        Endstapel = globals()[Endstapel]
                    Ablegen(Herz, Karo, Pik, Kreuz, s1, s2, s3, s4, s5, s6, s7, Karten, Karte, Stapel, Endstapel, Stelle, i, j, l, e, a ,r,f,p)
                    return
            if Endstapel == Herz or Endstapel == Karo or Endstapel == Pik or Endstapel == Kreuz:
                Karte[0]
                Endstapel.append(Karte[0])
                f = 1

        if Endstapel == s1 or Endstapel == s2 or Endstapel == s3 or Endstapel == s4 or Endstapel == s5 or Endstapel == s6 or Endstapel == s7:
            if Endstapel == [] and Karte[0][0] == 13:
                if Stapel == Karten:
                    Endstapel.append(Karte[0])
                else:
                    while p < len(Karte):
                        Endstapel.append(Karte[p])
                        p = p + 1
                f = 1
                return
            if Karte[0][0] != (Endstapel[len(Endstapel)-1][0] - 1) or ((Karte[0][1] == '♥' or Karte[0][1] == '♦') and (Endstapel[len(Endstapel)-1][1] == '♥' or Endstapel[len(Endstapel)-1][1] == '♦')) or (((Karte[0][1] == '♠' or Karte[0][1] == '♣') and (Endstapel[len(Endstapel)-1][1] == '♠' or Endstapel[len(Endstapel)-1][1] == '♣'))):
                End1 = Endstapel
                while Endstapel == End1:
                    print('Du kannst die Karte hier nicht platzieren, da die gewählte Karte nicht zur vorherigen passt')
                    Endstapel = input('Neuer Stapel:')
                    if Endstapel in globals():
                        Endstapel = globals()[Endstapel]
                    Ablegen(Herz, Karo, Pik, Kreuz, s1, s2, s3, s4, s5, s6, s7, Karten, Karte, Stapel, Endstapel, Stelle, i, j, l, e, a ,r,f,p)
                    return
            if Endstapel in [s1,s2,s3,s4,s5,s6,s7]:
                while i < len(Karte):
                    Endstapel.append(Karte[i])
                    i = i + 1
                    f = 1

        while Endstapel == Karten:
            print('Du kannst hier keine Karte ablegen')
            Endstapel = input('Neuer Stapel:')
            if Endstapel in globals():
                Endstapel = globals()[Endstapel]
            Ablegen(Herz, Karo, Pik, Kreuz, s1, s2, s3, s4, s5, s6, s7, Karten, Karte, Stapel, Endstapel, Stelle, i, j, l, e, a ,r,f,p)
            return

    Ablegen(Herz, Karo, Pik, Kreuz, s1, s2, s3, s4, s5, s6, s7, Karten, Karte, Stapel, Endstapel, Stelle, i, j, l, e, a ,r,f,p)
    f = 1

    #8: Karten löschen

    if Stelle > -1:
        if Stapel != Karten:
            while r < len(Karte):
                del(Stapel[len(Stapel)-1])
                r = r + 1
        else:
            del(Stapel[Stelle])
    else:
        del(Stapel[len(Stapel)])

    #9: Gewonnen Bedingung

    if (len(Herz) == 14) and (len(Karo) == 14) and (len(Pik) == 14) and (len(Kreuz) == 14):
        print ('Glückwunsch')
        w = 1

    #10: Sichtbar machen

    while z < 11:
        if alleStapel[z] == []:
            z = z + 1
        else:
            alleStapel[z][len(alleStapel[z])-1][2] = 1
            z = z + 1