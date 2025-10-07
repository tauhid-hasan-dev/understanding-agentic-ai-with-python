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


# Traditional way using match-case (Python 3.10+)
print("=== Traditional Match-Case Way ===")
for user in users:
    match user["coupon"]:
        case "P20":
            percent, fixed = 0.2, 0
        case "F10":
            percent, fixed = 0.3, 0
        case "P50":
            percent, fixed = 0.4, 10
        case _:  # default case
            percent, fixed = 0, 0
    
    print(f"{percent} and {fixed}")
    discount = user["total"]* percent + fixed
    print(f"user {user['id']} paid {user['total']} and discount is:{discount}")

print("\n=== Dictionary Way (Modern Approach) ===")
for user in users:
    percent, fixed = discounts.get(user["coupon"], (0, 0)) #this is the replacement of tradition way by match case
    print(f"{percent} and {fixed}")
    discount = user["total"]* percent + fixed
    print(f"user {user['id']} paid {user['total']} and discount is:{discount}")


