list_b = [3,7,2,6,3,9,1]
i = 0
x = len(list_b)
aktuellesx = 0
sicherung = 0
while i < len(list_b):
    aktuellesx = i
    x = i - 1
    while x > -1:
        if list_b[i] < list_b[x]:
            aktuellesx = x
        x = x-1
    sicherung = list_b[i]
    del list_b[i]
    list_b.insert(aktuellesx,sicherung)
    i = i + 1
print (list_b)

