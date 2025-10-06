order_amount = int(input ("Enter the order amount: "))

# normal conditional 
# if order_amount > 300:
#     delivery_fee = 0


delivery_fee = 0 if order_amount > 300 else 30


# print(f"Order amount: {type(order_amount)}")
print(f"delivery fee: {delivery_fee}")
