# Python Advance
# Dictionary
items_list = {"name":"Ktm","zip_code":"44600"}
print("Items",items_list)

# copy method
items_replica = items_list.copy()
print("Items replica:", items_replica)

# clear method - clear all the items
items_replica.clear()
print("Items_replica after clear method", items_replica)

# items method - show all the items if dict
print("Items of Items replica:", items_replica.items())
print("Items of Items list:", items_list.items())

# Pop method - removes the specified key and returns value
print(items_list.pop("zip_code"))
print(items_list)

def get_prime_number(start,end):
    if start < end :
        for num in range(start, end):
            if num > 1:
                for i  in range(num1,)