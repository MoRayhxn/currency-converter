dictionary_of_currency = {
        "GBP" : 1,
        "USD" : 1.17,
        "EUR" : 1.15,
        "RUS" : 0.016,
        "TAK" : 100,
        "CAD" : 0.97
    }
list_of_currency = [*dictionary_of_currency.keys()]
string_of_currency = ", ".join(list_of_currency[0:-1]) + f" or {list_of_currency[-1]}"

while True:
    from_currency, to_currency = [input(f"Would you like to exchange {i} {string_of_currency}? ").upper() for i in ["from","to"]] 

    try:
        amount = float(input("How much would you like to convert: "))
        if from_currency in list_of_currency and to_currency in list_of_currency:
            from_currency_value = dictionary_of_currency[from_currency]
            to_currency_value = dictionary_of_currency[to_currency]
            print(f"{amount*(to_currency_value/from_currency_value):,.2f} {to_currency}")
        else:
            raise ValueError
    except: 
        print("Invalid option!")