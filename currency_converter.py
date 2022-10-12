def currency_converter():

    lei_amount = int(input("Enter the amount of lei: "))

    euro_rate = 0.20

    convert = lei_amount * euro_rate

    print(f"{lei_amount} lei converted in euro is: {convert} euro")



currency_converter()