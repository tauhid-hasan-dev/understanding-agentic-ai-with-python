users = [
    {"id":1, "total": 100, "coupon": "P20"},
    {"id":2, "total":150, "coupon": "F10"},
    {"id":3, "total": 200, "coupon": "P50"},
]

discounts = {
    "P20": (0.2, 0),
    "F10": (0.3, 0),
    "P50": (0.4, 10)
}

for user in users:
    percent, fixed = discounts.get(user["coupon"])
    print(f"{percent} and {fixed}")
    discount = user["total"]* percent + fixed
    print(f"user {user['id']} paid {user['total']} and discount is:{discount}")


