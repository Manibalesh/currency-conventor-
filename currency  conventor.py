def convert_currency(amount, from_currency, to_currency):
    # Example exchange rates (as of a certain date)
    rates = {
        'USD': 1.0,       # Base currency
        'EUR': 0.85,
        'INR': 83.1,
        'GBP': 0.75,
        'JPY': 110.0
    }

    if from_currency not in rates or to_currency not in rates:
        return "Currency not supported."

    # Convert amount to USD, then to target currency
    usd_amount = amount / rates[from_currency]
    converted_amount = usd_amount * rates[to_currency]

    return round(converted_amount, 2)

# Example usage
amount = float(input("Enter amount: "))
from_curr = input("From currency (e.g., USD, EUR, INR): ").upper()
to_curr = input("To currency (e.g., USD, EUR, INR): ").upper()

result = convert_currency(amount, from_curr, to_curr)
print(f"{amount} {from_curr} = {result} {to_curr}")