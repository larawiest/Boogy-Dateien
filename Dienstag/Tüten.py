
t = 6 #Anzahl Tüten
sar = [100,3,40] #Anzahl der Spielzeugarten und Menge
tüten = [] #Tüten
i = 0 #Zähler/Stelle von Liste
j = 0 #Wiederholung von Spielzeug 
sp = 0 #Art von Spielzeug bei dem wir sind
o = 0
i = 0
elist = []
for i in sar:
    elist.append(0)
while o < t:
    tüten.append(elist[:])
    o = o + 1
i = 0
sp = 0
while sp < (len(sar)):
    j = 0
    if i > (len(tüten)-1):
       i = 0
    while j < sar[sp]:
        if i > (len(tüten)-1):
            i = 0
        tüten[i][sp] = tüten[i][sp] + 1
        i = i + 1
        j = j + 1
    sp = sp + 1
print(tüten)