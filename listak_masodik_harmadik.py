#2. Hozz létre egy listát, mely az alábbi szövegből szavanként listát készít!

txt = "The end justifies the means"
szavak = txt.split()
print(szavak)
for x in szavak:
    print(x, end=", ")

#3. A 2. feladat listaelemei nagybetűvel kezdődjenek. Több megoldás legyen!
for i in range(len(szavak)):
    szavak[i] = szavak[i].capitalize()
    print(szavak)