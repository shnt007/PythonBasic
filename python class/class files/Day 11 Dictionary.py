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
'''{ "id":"1", "std_name":"Sandesh", "std_address":"putalisadak", "std_grade":"2", \
  "created_at":"2021-11-26", "updated_at":"0000-00-00"}'''

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

