seat_type = input("Enter the seat type (Economy, Fisrt Class, Business Class): ").lower()

print(f"seat type: {seat_type}")


match seat_type:
    case "economy":
        print("15$, no food")
    case "first class":
        print("40$, food included")
    case "business class":
        print ("60$, food and ac included")
    case _:
        print("invalid seat type")