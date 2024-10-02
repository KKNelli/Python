# Hozz létre egy programot, mely bekéri, hogy hány elemet szeretnél megadni, majd
# létrehoz egy listát és
# feltölti a tömböt a felhasználó által megadott értékekkel
# A lista elemeinek sorrendje egyezzen meg a felhasználó által megadott értékek sorrendjével!

darab = int(input ("Add meg az elemek számát: "))
lista = []
for i in range(darab):
    szam = int(input("Kérek egy számot: "))
    lista.append(szam)
print(lista)
