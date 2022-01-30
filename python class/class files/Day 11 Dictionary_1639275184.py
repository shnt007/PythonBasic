'''# Dictionary method

# example
items_list = {"name":"Kathmandu"\
              , "zip_code":"44600",\
              "country":"Nepal"}

print("Initial items list", items_list)

# copy method - replicate/copy all the items from the primary
# dict to the particular dict we want to copy

items_list_replica = items_list.copy()

print("Replicat items_list", items_list_replica)

# clear method - removes all the items from the dict
items_list_replica.clear()
print("Replica items after clear()", items_list_replica)

# items - returns all the items in the dict
print("Cleared dic", items_list_replica.items())
print("Initial items_list", items_list.items())

# pop - removes the specified key from the dict
# and return its value

print(items_list.pop("country"))
print(items_list)

# SELECT * FROM tbl_employee
# id emp_name emp_address created_at updated_at

result = { "id":2, "emp_name":"Mohan", "emp_address":"Baneshwor", "created_at":"2021-11-25",\
           "updated_at":"0000-00-00"}

# function and if else statement, for loop, range revision

# function syntax
# def <function_name> ():
#   expression

def get_result():
    print(result)

get_result()

num = 45
def power(param):
    print(param * param)

power(num)
power(45)

def is_prime_number(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                print("is not prime", num)
                break
        else:
            print("is prime", num)
    else:
        print("number must be greater than 1")

is_prime_number(5)
is_prime_number(9)
is_prime_number(13)
is_prime_number(33)'''

'''# get - returns the value from the dict of key
location = {"id":25, "title":"Masala Beeds", "location":"Thamel"}

print(location.get("title"))

# popitem - removes the last index key-value items from the dict
# and returns the key value in tuple

print(location.popitem())
print(location)

# keys - returns all the keys from the dict
print(location.keys())

# values - returns all the values of keys from the dict
print(location.values())

# setdefault - insert key values in the dict
# case one - if the key already exist in the dict
location.setdefault("id")
print(location)

# case two - new key
location.setdefault("address")
print(location)

# case three - new key value pair
location.setdefault("country", "Nepal")
print(location)

# case four - existing key with new value
location.setdefault("id", 100) # does nothing
print(location) 

# update - updates the values of key in the dict
# tuple
id_update = (("id",100),)

location.update(id_update)
print(location)

# dict
title_update = {"title":"Mandala Beeds"}
location.update(title_update)
print(location)

# fromkeys - creates new dict with key and values from different
# variable
#case one
keys1 = {1, 2, 3, 4}
values1 = "Hello"

print(dict.fromkeys(keys1, values1))

#case two
values2 = {33, 44, 55}
print(dict.fromkeys(keys1, values2))'''


# loop in dictionary
items_list = {"id":"12", "name":"Munna Thakur",\
              "address":"Bihar", "country":"India"}
for i in items_list:
    print(i)

for value in items_list.values():
    print(value)

for key in items_list.keys():
    print(key)

for key, value in items_list.items():
    print(key, value)

# input
try:
    x = int(input("Enter a number "))
    print(x)
except:
    print("please enter a integer value")

set_example = {}
#set_example.pop()

num1 = 100
num2 = 0
print(num1/num2)
    
