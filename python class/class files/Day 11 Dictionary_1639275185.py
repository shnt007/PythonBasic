# Python Advance
# Dictionary methods

items_list = {"name": "Kathmandu", "zip_code":"44600"}

print("Items:", items_list)

# copy method - replicate/copy the primary dict items to the new dict
items_replica = items_list.copy()
print("Items replica:",items_replica)

# clear method - clears all items from the dict
items_replica.clear()
print("Items replica after clear method", items_replica)

# items method - shows all the items of dict
print("items of items_replica", items_replica.items())
print("items of items_list", items_list.items())

# pop method - removes the specified key and return its value
print(items_list.pop("zip_code"))
print(items_list)

#id std_name std_address std_grade created_at updated_at

#SELCT * FROM tbl_student
{ "id":"1", "std_name":"Sandesh", "std_address":"putalisadak", "std_grade":"2", \
  "created_at":"2021-11-26", "updated_at":"0000-00-00"}

# function and if else revision

def get_prime_number(start, end):
    if start < end:
        for num in range(start, end):
            if num > 1:
                for i in range(2, num):
                    if num % i == 0:
                        print("Not prime", num)
                        break
                else:
                    print("is prime", num)                    
    else:
        print("Start must be smaller than end")

get_prime_number(2, 15)
get_prime_number(15, 2)

# get - returns the value of key if the key is avaiable in the dict
print(items_list.get("name"))

# keys - returns all the keys avaiable in the dict
print(items_list.keys())

# popitem - returns key-value items in tuple when removed
print(items_list.popitem())


ordered_list = {"id":12, "title":"jug", "price":"1200"}
#print(ordered_list.popitem())
#print(ordered_list)

#print(items_list)

# setdefault - insert items in the dict
# case one - if the key already exist

ordered_list.setdefault("id")
print(ordered_list)

# case two - passing key only
ordered_list.setdefault("seller")
print(ordered_list)

# case three - passing key-value
ordered_list.setdefault("added_at", "2021-02-21")
print(ordered_list)

# case four - passing alreay existing key with new value
ordered_list.setdefault("id", 45) # does nothing
print(ordered_list)

# values - returns all the values of the items from the dict
print(ordered_list.values())

# update - udpates the items in the dict
#set_update = 
set_update_ii = (("id",45),)
ordered_list.update(set_update_ii)

print(ordered_list)


"""test = ("multi")
test_i = "multi", "item",

print(type(test))
print(type(test_i))
"""

# fromkeys - makes dict from the key values of different variable
keys1 = {1, 2, 3}
values1 = "hello"
print(dict.fromkeys(keys1, values1))

# case two - mutliple keys and multiple values
keys2 = (1, 2, 4, 5, 5)
values2 = (1212, 123123, 123123, 123123)
print(dict.fromkeys(keys2, values2))

