list = [5,4,7,8,1,6,9,0,2,3]
x = 0
y = 1
i = 0
xsicherung = 0
fehler =10000000000
while fehler > 0:
    fehler = 0
    i = 0
    x = 0
    y = 1
    while i < (len(list) - 1):
        if list[x] > list[y] :
            xsicherung = list[x]
            list[x] = list[y]
            list[y] = xsicherung
            fehler = fehler + 1
        x = x+1
        y = y+1
        i = i+1
print (list)