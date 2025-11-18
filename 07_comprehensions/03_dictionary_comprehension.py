tea_prices = {
    "chai": 10,
    "coffee": 15,
    "tea": 12,
}
tea_prices_usd = {tea:price/80 for tea, price in tea_prices.items()}
print(tea_prices_usd)
