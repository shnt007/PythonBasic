#insert
#index
#pop
#copy
#clear
#remove
#append
#extend
#count
#reverse
#sort

#trying out real world scenario - ecommerce cart system

#adding items to cart
final_cart = ["ODR1", "Item 1"]

#managing duplicate data and adding to cart
order_details = ["ODR1", "Heera", "heera@gmail.com", "9874545", "26 Nov 2021"]
print("Order details")
print(order_details)

order_item = ["Moblie Phone - Kids Toy"]
order_item.append("Doll for Kids")
order_item.append("Kinder Joy Chocos")
order_item.append("Gameboy")
print("Order item details")
print(order_item)

#using extend method to combine the items and order
order_details.extend(order_item)

#using copy method to push all order details to final cart
final_cart = order_details.copy()
print("Final Order cart to push to database")
print(final_cart)

#adding more items to cart
final_cart.append("Item 2")
final_cart.append("Item 5")
final_cart.append("Item 5")
final_cart.append("Item 5")

print("Cart Item List")
print(final_cart)

#using count method to count the number of item in the list
count_item = final_cart.count("Item 5")
print("Item 5 quantity")
print(count_item)

#using reverse method to reverse the items in the list
final_cart.reverse()
print("Item list after reversing")
print(final_cart)

#using sort method to sort the item in the list
final_cart.sort()
print("Item sorting from the list")
print(final_cart)

#finding the index number of cart
index_num = final_cart.index("Item 5")
print("Item 5 index number")
print(index_num)

#removing item from cart if the item is unnecessary
final_cart.pop(index_num)
print("Checking cart after removing one Item 5 from list")
print(final_cart)

#lets assume that the customer has checkout
#if checkout process is completed we clear all items from cart
print("After storing values clearing list and checking it")
final_cart.clear()
print(final_cart)

