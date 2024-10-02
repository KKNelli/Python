# Adott az alábbi lista: [21, 32, 13, 44, 75] 
# 1. lépés: írjunk egy kódsort, amely megkérdezi a felhasználót, hogy melyik elemet mdosítsa a program.
# Az adott elemet módosítsd a felhasználó által megadott számra.
# 2. lépés: írjunk egy kódsort, amely eltávolítja az utolsó elemet a listából.
# 3. lépés: írjunk egy kódsort, amely kiírja a meglévő lista hosszát.
# 4. lépés: Írjunk kódot, mely kiírja sorban a lista elemeit. Soronként egye-egy elemet.

lista = [21, 32, 13, 44, 75]
szam = int(input("Mondj egy szamot:"))
melyiket = int(input("Melyik számra módosítsa?"))

#lista[melyiket - 1] = szam
index = melyiket -1
if index >= len(lista) or index < 0:
    print("Nincs ilyen elem")
else:
    lista[index] = szam
print(lista)

#Második feladat
lista.pop()
print(lista)

#Harmadik feldata
print(len(lista))

#negyedik feladat
for x in lista:
    print(x)