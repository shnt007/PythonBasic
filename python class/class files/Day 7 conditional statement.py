# Conditional statement - controls the flow of the program

# if statement
# if else statement
# if elif else statement
# nested if

# if statement syntax
# if condition :
#    expression

# int case
x = 25
if x > 0:
    print("Is greater")

if x > -1:
    print("Is smaller")

# string case
name = "Dharan"

s = str(x)
if s.isnumeric():
    print("Is numeric")

if name.isalpha():
    print("Is alphabetical value")

# float case
num = 4.5
if num > 4.51:
    print("Is smaller")
if num >= 4.49:
    print("Is equal")

# if else statment syntax
#   if condition:
#       expression
#   else:
#       expression

# int case
num = 10.99

if num < 20:
    print("Is smaller")
else:
    print("Is greater")

if num <= 11:
    print("Smaller or equals")
else:
    print("Greater")

if num != 10.99:
    print("is not valid")
else:
    print("is valid")

# if elif else statement syntax
#   if condition:
#       expression
#   elif condition:
#       expression
#   else:
#       expression

# string case
item_name = "Mango"
item_price = 1200.00

#example one
if item_name.isnumeric():
    print("Please input the correct name")
elif item_name.isalnum():
    print("Is a valid input")
else:
    print("Please enter a valid input")

#example two
str(item_price)
if str(item_price).isalpha():
    print("Please input the numeric value")
elif str(item_price).isnumeric():
    print("Valid input checking with isnumeric method")
elif str(item_price).isdecimal():
    print("Valid input with isdecimal method")
else:
    print("Is incorrect")

# Nested if syntax
#   if condition:
#       expression
#       if condition:
#           expression
#       elif condition:
#           expression
#       else:
#           expression
#   can be end upto here as well
#   but in some cases there can be multiple if 
#   conditions as well
#   if condition:
#       expression

# Example of nested if
item_price = 1500.00

if item_price <= 1500.00:
    #case one: single if 
    if str(item_price).isnumeric():
        print(item_price)
    
    # case two - if else
    if str(item_price).isalpha():
        print("Invalid input")
    else:
        print("Please enter valid input")

    #case three - if elif else

    if item_price != 1500.00:
        print("Item price is invalid")
    elif item_price < 1500.00:
        print("Item price is smaller")
    else:
        print("Item price is greater")
else:
    print("Please enter smaller values than 1500.00")
    
    

    


