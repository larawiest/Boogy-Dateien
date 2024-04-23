import random
import sys
number = random.randint(1,100)
while 0 == 0:
    Schätzung = int(input('Deine Schätzung:'))
    if Schätzung == number:
        print('Glückwunsch')
        sys.exit()
    else:
        print ('Versuche es nochmal.')