list_p = [2,4,1,6,200,6,0,23,188]
i = 0
a = 1
amin = 10000000000
asicherung = 0
astellemin = 0
while i < (len(list_p)):
    amin = list_p[i]
    a = i
    while a < len(list_p) - 1:
        if list_p[a] < amin:
            amin = list_p[a]
            astellemin = a
        a = a + 1
    asicherung = list_p[astellemin]
    list_p[astellemin] = list_p[i]
    list_p[i] = asicherung
    i = i + 1
print(list_p)
