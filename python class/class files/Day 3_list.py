# List examples
list_of_alphanumbers = [1, "one", 2, "two", 3, "three", 4, "four"]

# Copy
list_of_alphanumbers_2 = list_of_alphanumbers.copy()

print(list_of_alphanumbers)
print(list_of_alphanumbers_2)

# Clear
list_of_alphanumbers_2.clear()
print(list_of_alphanumbers_2)

# Append
list_of_alphanumbers.append(5)
list_of_alphanumbers.append("five")
print(list_of_alphanumbers)

# Extend
list_of_alphanumbers.extend([6, "six"])
print(list_of_alphanumbers)

# Insert
# Insert item in the index provided
# If index is larger than size of list, then item will be appended in last position
list_of_alphanumbers.insert(0, "Seven")
list_of_alphanumbers.insert(0, 7)
print(list_of_alphanumbers)

# Remove
# Return value error if item not found
list_of_alphanumbers.remove(6)
list_of_alphanumbers.remove("six")
print(list_of_alphanumbers)

# Extending list to contain duplicate items
list_of_alphanumbers.extend([6, 9, 6, 7, 9, 8, 9])
print(list_of_alphanumbers)

# Count
# Counts the total number of repetition of item
print(list_of_alphanumbers.count(9))
print(list_of_alphanumbers.count(2))
print(list_of_alphanumbers.count(15))

# Index
# Return value error if item not found
print(list_of_alphanumbers.index("five"))

# Pop
# Return removed item
print(list_of_alphanumbers.pop())
print(list_of_alphanumbers)

# Reverse
# Reverse the order of the list
# Reverse is a inplace method
list_of_alphanumbers.reverse()
print(list_of_alphanumbers)

# Sort
# Sort is a inplace method, original list will be affected.
numbers = [1, 2, 3, 5, 6, 7, 8, 3, 2, 56, 8, 9,
           63, 3, 2, 6, 7, 8, 3, 267, 2, 632, 1, 6243]
print(numbers)
numbers.sort()
print(numbers)

# Get item at specific index
print(numbers[5])

# Len -> return the length of the list (numbers of item in list)
print(len(list_of_alphanumbers))

# Size of list in bytes
print(list_of_alphanumbers.__sizeof__())

# Create a list with 20 "a"
# * operator will multiply the item in list
list_of_a = ["a"] * 20
print(list_of_a)
