"""cvic"""

cislo = 15

if cislo > 10:
    print('Číslo je väčšie než 10')
else:
    print('Číslo nieje väčšie než 10')


i = 0 # Nejaká základná hodnota

while i < 6: # Tu si nastavim šmyčku na tu základu hodnotu aby nebola väčšia ako 5 ale mám tam 6 pretože to je pravidlo že tu 6tku už neráta
    print(i) 
    i += 1 # Vnútri šmyčki sa vytlačí hodnota i a potom sa zväčší o 1 pomocou i += 1


zoznam = [1, 2, 3, 4, 5]

for čísla in zoznam: # Pre čísla v zozname vytlač čísla v doslovnom preklade
    print(čísla)


def pozdrav (name): # Definujem funkciu pozdrav arguemntom name
    print('Ahoj,' + name + '!') #

pozdrav('Radovan')


def súčet(a, b): # Funkcia je definovaná 2 parametrami
    return a + b  # Funckia vypočíta a + b a pomocou kľúčového slova return vráti výsledok
 
výsledok = súčet(7, 3)
print(výsledok)


def je_prvočíslo(cislo): # Def funkcie s argumentom cislo
    if cislo <= 1: # Tento blok kontroluje či je číslo menšie alebo rovne 1.Prvočíslo je logicky väčšie ako 1.Preto ak je číslo menšie alebo sa rovná 1 funkcia okamžite vráti false.
        return False
    for i in range(2, cislo): # Smyčka for sa používa k iteraci cez čísla v určitom rozsahu.range(2, cislo) vytvorí sekvenciu čísel od 2 do čísla tesne menšieho než cislo,napr. ak je číslo 11 smyčka projde čísla 2,3,4,...,10.Smyčka postupne priradzuje číslo v tomto rozsahu premennej i.
        if cislo % i == 0: # Tento blok je vnútri smyčky for.Číslo % i vypočíta zbytok po delení cislo číslom i.Pokiaľ je tento zbytokrovný 0,znamená to že cislo je deliteľné číslom i.Ak funkcia zistí že číslo je deliteľné iným číslom ihned vráti False.
            return False
        return True
    
print(je_prvočíslo(11))
print(je_prvočíslo(10))

