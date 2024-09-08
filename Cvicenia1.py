"""Cvicenia"""
# Funkcie

def pozdrav(meno): # Definujem si funkciu ktorá sa pozdrav s kľučom meno neskôr môžem použit meno namiesto naozajstného mena lebo ho mám raz definované môžem ho použit v celom programe.
    print(f'Ahoj, {meno}!')

pozdrav('Radovan')

def spočítaj (a, b):
    print(a + b)

spočítaj(3,5)

def info(meno, vek):
    print(f'{meno} má {vek} rokov.')

info('Radovan', 23)

def info(meno, vek=23):
    print(f'{meno} má {vek} rokov.')

info('Radovan')
info('Radovan', 30)

def spočítaj(a, b):
    return a + b

vysledok = spočítaj(3, 5)
print(vysledok)

def operacia(a, b):
    súčet = a + b
    rozdiel = a - b 
    return súčet, rozdiel

výsledky = operacia(3, 5)
súčet, rozdiel = operacia(3, 5)

print(výsledky)
print(súčet)
print(rozdiel)

lambda argumenty: výraz

spočítaj = lambda a, b:a + b
print(spočítaj(3, 5))

zoznam = [1, 2, 3, 3, 4, 5]
zoznam2 = [list(map(lambda x: x*2, zoznam))]

print(zoznam)
print(zoznam2)

def pozdrav(meno):
    """
    Tato funkcia vypíše pozdrav s daným nemom
    """
    print(f'Ahoj, {meno}!')

pozdrav('Radovan')

def pozdrav():
    meno = 'Radovan' # lokálna premenná
    print(f'Ahoj, {meno}!')

#pozdrav()
#print(meno) # Toto spôsobí chybu,pretože 'meno' nieje defonované mimo funkciu.

meno = 'Radovan' # Globálna premenná

def pozdrav():
    print(f'Ahoj, {meno}!')

pozdrav()
print(meno) # Toto bude fungovať,pretože 'meno' je globálna premenná

x = 10 # Globálna premenná

def zmen_x():
    global x
    x = 5

print(x) # Výtup: 10
zmen_x()
print(x) # Výstup: 5

