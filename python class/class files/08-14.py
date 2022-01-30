item_price = 1500.00
if item_price >= 1500.00:
    # Case 1 : Single if
    if str(item_price).isnumeric():
        print(item_price)

    # Case 2 : if else
    if str(item_price).isalpha():
        print("Invalid input")
    else:
        print("Please enter valid number")

    # Case 3 : if elif else
    if item_price != 1500.00:
        print("Item prince is invalid")
    elif item_price < 1500.00:
        print("Item prince is smaller")
    else:
        print("Item price is greater")
else:
    print("Please enter smaller values than 1500.00")
