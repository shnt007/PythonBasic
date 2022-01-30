# Example of append method
days = ["Sunday", "Monday", "Tuesday"]
days.append("Wednesday")
days.append("Thursday")
# print(days)

# Example of extend method
days_left = ["Friday", "Saturday"]
days.extend(days_left)
#print(days)

# Example of insert method
ordered_items = ["Masala", "Vegetable", "Fruits"]
ordered_items.insert(2, "Salad")
ordered_items.insert(-1, "Utensils")
print(ordered_items)

# Example of index method - returns the index of the list
print(ordered_items.index("Masala"))

# Example of copy method
ordered_items_final = ordered_items.copy()
print(ordered_items_final)

# Example of clear method
ordered_items_final.clear()
print(ordered_items_final)

# Example of pop method
ordered_items = ["Masala", "Vegetable", "Fruits"]
ordered_items.pop(1)
print(ordered_items)

# Example of remove method
ordered_items.remove("Fruits")
print(ordered_items)
