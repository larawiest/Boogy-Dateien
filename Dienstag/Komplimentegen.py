import random
j = 0
Menschen = ['Lara','Sofie','Marie','Yvette','Linda','Zeynep','Lena','Josefine']
Komplimente = ['Großartigste','Beste','Schlauste','Inspirierendste','Lustigste','Kompetenteste','Loyalste','Lösungsorientierteste','Optimalste','Munterste','Netteste','Produktivste']
Begriffe = ['Schülerin','Freundin','Hamster Hektor Verehrerin','Freundin des Typescripts','Brotliebhaberin','Menschin','Lebewesin']
for i in Menschen:
    print(Menschen[j], 'du bist die', Komplimente[random.randint(0,len(Komplimente)-1)], Begriffe[random.randint(0,len(Begriffe)-1)])
    j = j + 1