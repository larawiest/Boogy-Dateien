import sys
r1 = ['-','-','-']
r2 = ['-','-','-']
r3 = ['-','-','-']
Reihen = [r1,r2,r3]
Reihe = 0
Stelle = 0
i = 0
k = 0
print(r1)
print(r2)
print(r3)
while 0 == 0:
    print('Spieler 1:')
    Reihe = input('Reihe:')
    Stelle = input('Stelle:')
    Stelle = int(Stelle)
    Reihe = int(Reihe)
    Reihe = Reihen[Reihe]
    print(Stelle)
    while Reihe[Stelle] != '-':
        print(Reihe[Stelle])
        print('Feld ist voll. Bitte wählen sie ein weiteres.')
        Reihe = input('Reihe:')
        Stelle = input('Stelle:')
        Stelle = int(Stelle)
        Reihe = int(Reihe)
        Reihe = Reihen[Reihe]
    Reihe[Stelle] = 0
    print(r1)
    print(r2)
    print(r3)
    i = i + 1

    while k < 3: #schaut wer gewonnen hat
        liste = Reihen[k]
        if liste[0] == liste[1] == liste[2] != '-':
            print('Spieler 1 hat gewonnen. Glückwunsch')
            sys.exit()
        if r1[k] == r2[k] == r3[k] != '-':
            print('Spieler 1 hat gewonnen. Glückwunsch')
            sys.exit()
        k = k + 1
        if r1[0] == r2[1] == r3[2] != '-':
            print('Spieler 1 hat gewonnen. Glückwunsch')
            sys.exit()
        if r1[2] == r2[1] == r3[0] != '-':
            print('Spieler 1 hat gewonnen. Glückwunsch')
            sys.exit()

    k = 0

    if i == 9:
        print('Gleichstand')
        sys.exit() 

    print('Spieler 2:')
    Reihe = input('Reihe:')
    Stelle = input('Stelle:')
    Stelle = int(Stelle)
    Reihe = int(Reihe)
    Reihe = Reihen[Reihe]
    print(Stelle)
    while Reihe[Stelle] != '-':
        print(Reihe[Stelle])
        print('Feld ist voll. Bitte wählen sie ein weiteres.')
        Reihe = input('Reihe:')
        Stelle = input('Stelle:')
        Stelle = int(Stelle)
        Reihe = int(Reihe)
        Reihe = Reihen[Reihe]
    Reihe[Stelle] = 1
    print(r1)
    print(r2)
    print(r3)
    i = i + 1

    while k < 3: #schaut wer gewonnen hat
        liste = Reihen[k]
        if liste[0] == liste[1] == liste[2] != '-':
            print('Spieler 2 hat gewonnen. Glückwunsch')
            sys.exit()
        if r1[k] == r2[k] == r3[k] != '-':
            print('Spieler 2 hat gewonnen. Glückwunsch')
            sys.exit()
        k = k + 1
        if r1[0] == r2[1] == r3[2] != '-':
            print('Spieler 2 hat gewonnen. Glückwunsch')
            sys.exit()
        if r1[2] == r2[1] == r3[0] != '-':
            print('Spieler 2 hat gewonnen. Glückwunsch')
            sys.exit()

    k = 0