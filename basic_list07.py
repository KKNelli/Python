# Hozz létre egy programot, mely
# bekéri, hogy hány elemet szeretnél megadni, majd
# létrehoz egy listát és
# feltölti a iistát a felhasználó átal megadott értékekkel
# A lista elemeinek sorrendje fordítottja legyen a felhasználó által megadott értékek sorrendjének!

darab = int(input ("Add meg az elemek számát: "))
lista = []
for i in range(darab):
    szam = int(input("Kérek egy számot: "))
    lista.append(szam)
lista.reverse()
print(lista)