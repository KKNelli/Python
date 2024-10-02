# Távolítsd el a tömbökből az első elemet!
# 1. Az első tömbre használd a del parancsot
# 2. A második tömbre használd a pop() metódust és távolítsd el az utolsó elemet
# # 3. A harmadik tömbre használd a remove() metódust

erdemjegy = [1,2,3,4,5]
osztaly = ["9/ny", "9/a", "10/b", "11/c","12/b halado", "1/13b", "2/14b"]
adatok = ["Akos", "Denes", "Laci","Levente", "Nelli", "Regi"]
del erdemjegy[0]
print(erdemjegy)

print(osztaly)
osztaly.pop(-1)
print(osztaly)

print(adatok)
adatok.remove(adatok[0])
print(adatok)