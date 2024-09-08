"""Kalkulacka"""

 
def sčítanie(a, b) # Klauzula definície funkcie,,Názov funkcie používa sa aj na volanie funkcie,,Parametre funkcie a a b sú vstupné hodnoty,ktoré funkcia očakáva keď je volaná,,Dvojbodka označuje koniec hlavičky funkcie a začiatok tela funkcie.
    return a + b # Kľúčové slovo ktoré určuje čo funkcia vráti ako výsledok,,Výraz ktory sa vyhodnotí a jeho výsledok sa vráti.V tomto prípade sčíta hodnoty a a b.

def odčítanie(a, b)
    return a - b

def násobenie(a, b)
    return a * b

def delenie(a, b)
    if b != 0: #  Podmienka, ktorá kontroluje, či hodnota b nie je rovná nule. Ak podmienka platí (ak b nie je nula), vykoná sa blok kódu nasledujúci po tejto podmienke.
        return a / b # Ak je podmienka b != 0 splnená, funkcia vráti výsledok delenia a / b.
    else: # Alternatívna vetva podmienky if. Tento blok kódu sa vykoná, ak podmienka b != 0 nie je splnená (teda ak b je nula).
        return 'Delenie nulou nieje povolené!' # Ak je b rovné nule, funkcia vráti tento reťazec ako chybové hlásenie.
    