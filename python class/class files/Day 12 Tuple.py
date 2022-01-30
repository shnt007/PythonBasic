# Tuple - sequence of ordered items but immutable

gender = ("male", "female", "others")

# count - counts the items in the tuple
print(gender.count("others"))

# index - returns the index of the items in the tuple
print(gender.index("male"))
print(gender[1])

print("male" in gender)
