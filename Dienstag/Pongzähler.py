import sys
zähler = 0
while 0 == 0:
    j = input()
    if j == 'Ping':
        print('Pong')
        zähler = zähler + 1
        print(zähler)
    if j == 'exit':
        print(zähler)
        sys.exit()
        