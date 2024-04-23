import random
import sys
robob = ['Schere','Stein','Papier']
rob = robob[random.randint(0,2)]
du = input('Schere,Stein,Papier?')
while du != robob[0] and du != robob[1] and du != robob[2]:
    print('Keine Option. Versuche es nochmal.')
    du = input('Schere,Stein,Papier?')
print('Du:', du)
print('Computer:', rob)
if rob == 'Schere' and du == 'Papier' or rob == 'Papier' and du == 'Stein' or rob == 'Stein' and du == 'Schere':
    print('Der Computer hat gewonnen.')
else:
    if du == rob:
        print('Gleichstand')
    print('Du hast gewonnen.')