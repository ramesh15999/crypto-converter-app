# Conversion rates in relation to USD (These are mock rates, you can replace with real data)
conversion_rates = {
    'BTC': 50000,  # 1 Bitcoin = 50,000 USD
    'ETH': 3000,   # 1 Ethereum = 3,000 USD
    'LTC': 200,    # 1 Litecoin = 200 USD
    'USD': 1       # 1 USD = 1 USD
}

def convert_currency(amount, from_currency, to_currency):
    """Convert a given amount from one currency to another."""
    if from_currency not in conversion_rates or to_currency not in conversion_rates:
        return None

    # Conversion formula: (amount / from_rate) * to_rate
    converted_amount = (amount / conversion_rates[from_currency]) * conversion_rates[to_currency]
    return converted_amount

def main():
    print("Welcome to the Cryptocurrency Converter!")
    print("Available currencies: BTC (Bitcoin), ETH (Ethereum), LTC (Litecoin), USD (US Dollar)")

    # Get user input for conversion
    from_currency = input("Enter the currency you want to convert from (e.g., BTC): ").upper()
    to_currency = input("Enter the currency you want to convert to (e.g., ETH): ").upper()
    amount = float(input(f"Enter the amount of {from_currency} you want to convert: "))

    # Perform the conversion
    result = convert_currency(amount, from_currency, to_currency)

    if result is not None:
        print(f"{amount} {from_currency} is equal to {result:.4f} {to_currency}")
    else:
        print("Invalid currency input. Please try again.")

if __name__ == "__main__":
    main()