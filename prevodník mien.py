"""CV"""

def prevodnik_mien(amount, from_currency, to_currency):
    # Výmenné kurzy voči euru
    kurzy_voci_euru = {
        "EUR": 1,        # Euro
        "USD": 1.18,     # Americký dolár
        "GBP": 0.85,     # Britská libra
        "CZK": 25.5,     # Česká koruna
        "JPY": 130.0,    # Japonský jen
        "AUD": 1.6       # Austrálsky dolár
    }

    # Skontrolujeme, či sú obe meny v slovníku výmenných kurzov
    if from_currency not in kurzy_voci_euru or to_currency not in kurzy_voci_euru:
        return "Jedna z mien nie je podporovaná."

    # Prevod z 'from_currency' do EUR
    amount_in_eur = amount / kurzy_voci_euru[from_currency]

    # Prevod z EUR do 'to_currency'
    converted_amount = amount_in_eur * kurzy_voci_euru[to_currency]

    return round(converted_amount, 2)

# Príklad použitia
amount = 100
from_currency = "EUR"
to_currency = "AUD"
result = prevodnik_mien(amount, from_currency, to_currency)
print(f"{amount} {from_currency} je {result} {to_currency}")

# Všetko