device_temrature = "active"
temperature = 56

if device_temrature == "active":
    if temperature > 35:
        print("High temperature alert")
    else: 
        print("Temperature is normal")
else: 
    print("Device is offline")
