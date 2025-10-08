# returning from a function and set it to a variable

def calcute_price(ammount, price_per_cup):
    return ammount * price_per_cup

result = calcute_price(5, 15)

print(f"Total price is {result}")


# another calculation with function 

def add_vat(price, vat_rate):
    return price * (100 + vat_rate)/100

prices = [200, 500, 1000]

for price in prices:
    price_with_vat = add_vat(price, 10)
    print(f"Original price is {price} and price with vat is {price_with_vat}")



