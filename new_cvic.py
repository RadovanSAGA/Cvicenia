"""Funkcie"""
def spočítaj(*čísla):
    return sum(čísla)

print(spočítaj(1, 2, 3, )) 

def zobraz_info(**info):
    for kľúč, hodnota in info.items():
        print(f'{kľúč}: {hodnota}')

zobraz_info(
    Meno = 'Radovan',
    Vek = 23,
    Mesto = 'Knm'
)


def vystupny_formular(**data):
    for pole, hodnota in data.items():
        print(f'{pole.capitalize()}: {hodnota}')

vystupny_formular(meno = 'Radovan', priezvisko = 'Sága', email = 'radovansaga@gmail.com')

def kombinovaná_funkcia(*args, **kwargs):
    print('Pozičné argumenty:', args)
    print('Kľúčové argumenty:', kwargs)

kombinovaná_funkcia(1, 2, 3, meno='Radovan', vek=30)