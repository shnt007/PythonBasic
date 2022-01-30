# Loop - certain iteration to obtain certain output

# for syntax
# for <variable_name> in (membership operator) <sequence_name>:
#    expression

# membership operator
list_item = ["sandesh", "madan", "sherpa", "Ming", "sajan"]


for item in list_item:
    print("Item list", item)


#range syntax
# range(start, end, set_size)
# start - defines the starting point
# end - stops the range value or end point
# set_size - differentiate the value between the range value

item = list(range(10))
item_i = list(range(0, 10))

print(item)
print(item_i)
print(*range(2, 15, 3))

for items in range(len(list_item)):
    print(items)
