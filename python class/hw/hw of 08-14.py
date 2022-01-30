# Example 1:
price = 50
quantity = 10
amount = price * quantity
if (amount > 100):
    if (amount > 500):
        print ("Amount is greater than 500.")
    else:
        if (amount < 500 and amount > 400):
            print("Amount is between 400 to 500.")
        elif(amount < 500 and amount > 300):
            print("Amount is between 300 to 500.")
        else:
            print("Amount is between 200 to 500")
elif(amount == 100):
        print("Amount is 100.")
else:
    print("Amount is less than 100.")

#Example 2
hot_day = False
cold_day = False
if (hot_day):
    print("Drink plenty of water")
elif(cold_day):
    print("Wear warm clothes")
else:
    print("It a great day")
