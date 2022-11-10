while True:
    from_currency = input("Would you like to exchange from, GBP, USD or EUR? ").upper()
    to_currency = input("Would you like to exchange to, GBP, USD or EUR? ").upper()

    usd_to_gbp = 1.17
    gbp_to_usd = 0.85
    eur_to_gbp = 0.87
    gbp_to_eur = 1.15
    eur_to_usd = 1.02
    usd_to_eur = 0.98

    amount = float(input("How much would you like to convert: "))

    if from_currency == "USD" and to_currency == "GBP":
        print(f"{amount*usd_to_gbp}")
    elif from_currency == "USD" and to_currency == "EUR":
        print(f"{amount*usd_to_eur}")
    elif from_currency == "GBP" and to_currency == "USD":
        print(f"{amount*gbp_to_usd}")
    elif from_currency == "GBP" and to_currency == "EUR":
        print(f"{amount*gbp_to_eur}")
    elif from_currency == "EUR" and to_currency == "GBP":
        print(f"{amount*eur_to_gbp}")
    elif from_currency == "EUR" and to_currency == "USD":
        print(f"{amount*eur_to_usd}")
    else:
        print("Invalid option")