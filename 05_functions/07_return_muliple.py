# no return
def idle_chaiwala():
    pass # pass is a placeholder when a funtion return nothing, or do not have any logic yet
print(idle_chaiwala())

# single return
def sum(a, b):
    return a*b
result_sum = sum(3,4)
print(result_sum)


# multiple return 
def chai_report(sold, remaining, notPaid):
    return sold, remaining, notPaid

sold, remaining, notPaid = chai_report(14, 5, 1)
print(f"total sold chai is {sold} and total remaining chai is {remaining} and not paid is {notPaid}")


# multiple return (example two)
def chai_report2():
    return 50, 23, 6

sold, remaining, notPaid = chai_report2() 
print(f"total sold chai is {sold} and total remaining chai is {remaining} and not paid is {notPaid}")


