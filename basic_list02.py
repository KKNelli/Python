# Az előző feladatban létrehozott tömbök harmadik elemét adjuk az adott tömb
# 1. az első elem értékéül
# 2. a második elem értékéül
# # 3. az utolsó elem értékéül

erdemjegy = [1,2,3,4,5]
osztaly = ["9/ny", "9/a", "10/b", "11/c","12/b halado", "1/13b", "2/14b"]
adatok = ["Akos", "Denes", "Laci","Levente", "Nelli", "Regi"]

erdemjegy[0] = erdemjegy[2]
print(erdemjegy)

osztaly[1] =erdemjegy[2]
print(osztaly)


#adatok[-1] = osztaly[2]
adatok[len(adatok)-1] = adatok[2]
print(adatok)