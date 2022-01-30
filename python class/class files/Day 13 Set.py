'''# Set - unordered collection, immutable and unique

x = { 1, 3, 7, 4, 2, 3, 4, 5}
print(x)
# output - {1, 2, 3, 4, 5, 7}

# 1. add - adds new item in the set
country = {"Nepal", "India", "Bhutan", "Maldives"}
print("Before adding", country)
country.add("Afganistan")
country.add("Pakistan")
country.add("Sri Lanka")
country.add("Bangladesh")
print("After adding", country)

# 2. copy - replicate/copy all items from primary set to new set
country_saarc = country.copy()
print("Saarc", country_saarc)

# 3. clear - removes all items from the set
#country.clear()
print(country)

# 4. difference - reutrns new set from the difference of two set
country.add("China")
country.add("USA")
country.add("Australia")
country.add("UK")

# case one - returns remaing items 
print("Difference - More item ", country.difference(country_saarc))
print("Before difference update", country)
print(country_saarc)

# case two - returns blank set
print("Less item", country_saarc.difference(country))

# 5. difference_update -  removes items from comparing set of primary set
print("Difference update", country.difference_update(country_saarc))
print("After difference update", country)
print(country_saarc)

# 6. symmetric_difference - returns new set of difference set
print("Symmetric - ",country.symmetric_difference(country_saarc))

# 7. symmetric_difference_update
country_after = country.symmetric_difference_update(country_saarc)
#print(country_after)
print(country)

country_saarc_after = country_saarc.symmetric_difference_update(country)
print(country_saarc)

test = {1, 23, 4, 5}
test1 = {1, 23, 4, 5}
test2 = {1, 2, 3, 23, 4, 77, 88}
print(test.symmetric_difference_update(test2))
print(test2.difference_update(test1))
print(test)
print(test2)'''

# difference, difference_update, symmetric_difference, symmetric_difference_update revision

# example

# 1. difference
set_a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
set_a_copy = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
set_b = {1, 3, 5, 7, 9, 11, 13, 15, 17}
set_c = {2, 4, 6, 8, 10, 12, 14, 16, 18}

print("\n")
print("difference Example")
print("SET A before", set_a)
print("SET A_copy before", set_a_copy)
print("SET B before", set_b)
print("SET C before", set_c)
print("SET A & SET B difference", set_a.difference(set_b)) # equivalent to A-B
print("SET A_copy & SET C difference", set_a_copy.difference(set_c)) # equivalent to A_copy-C
print("SET A after", set_a)
print("SET A_copy before", set_a_copy)
print("SET B after", set_b)
print("SET C after", set_c)

# 2. difference_update
set_a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
set_a_copy = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
set_b = {1, 3, 5, 7, 9, 11, 13, 15, 17}
set_c = {2, 4, 6, 8, 10, 12, 14, 16, 18}

print("\n")
print("difference_update Example")
print("SET A before", set_a)
print("SET A_copy before", set_a_copy)
print("SET B before", set_b)
print("SET C before", set_c)
# equivalent to A-B
print("SET A & SET B difference_update", set_a.difference_update(set_b))
# equivalent to B-A_copy
print("SET B & SET A_copy difference_update", set_b.difference_update(set_a_copy))
# equivalent to A_copy-C
print("SET A_copy & SET C difference_update", set_a_copy.difference_update(set_c))
print("SET A after", set_a)
print("SET A_copy before", set_a_copy)
print("SET B after", set_b)
print("SET C after", set_c)

# 3. symmetric_difference
set_a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
set_a_copy = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
set_b = {1, 3, 5, 7, 9, 11, 13, 15, 17}
set_c = {2, 4, 6, 8, 10, 12, 14, 16, 18}

print("\n")
print("symmetric_difference Example")
print("SET A before", set_a)
print("SET A_copy before", set_a_copy)
print("SET B before", set_b)
print("SET C before", set_c)
# equivalent to A-B
print("SET A & SET B symmetric_difference", set_a.symmetric_difference(set_b))
# equivalent to B-A_copy
print("SET B & SET A_copy symmetric_difference", set_b.symmetric_difference(set_a_copy))
# equivalent to A_copy-C
print("SET A_copy & SET C symmetric_difference", set_a_copy.symmetric_difference(set_c))
print("SET A after", set_a)
print("SET A_copy before", set_a_copy)
print("SET B after", set_b)
print("SET C after", set_c)

# 4. symmetric_difference_update
set_a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
set_a_copy = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
set_b = {1, 3, 5, 7, 9, 11, 13, 15, 17}
set_c = {2, 4, 6, 8, 10, 12, 14, 16, 18}

print("\n")
print("symmetric_difference_update Example")
print("SET A before", set_a)
print("SET A_copy before", set_a_copy)
print("SET B before", set_b)
print("SET C before", set_c)
# equivalent to A-B
print("SET A & SET B symmetric_difference_update", set_a.symmetric_difference_update(set_b))
# equivalent to B-A_copy
print("SET B & SET A_copy symmetric_difference_update", set_b.symmetric_difference_update(set_a_copy))
# equivalent to A_copy-C
print("SET A_copy & SET C symmetric_difference_update", set_a_copy.symmetric_difference_update(set_c))
print("SET A after", set_a)
print("SET A_copy before", set_a_copy)
print("SET B after", set_b)
print("SET C after", set_c)

# 5. intersection
set_a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
set_a_copy = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
set_b = {1, 3, 5, 7, 9, 11, 13, 15, 17}
set_c = {2, 4, 6, 8, 10, 12, 14, 16, 18}

print("\n")
print("intersection Example")
print("SET A before", set_a)
print("SET A_copy before", set_a_copy)
print("SET B before", set_b)
print("SET C before", set_c)
# equivalent to A-B
print("SET A & SET B intersection", set_a.intersection(set_b))
# equivalent to B-A_copy
print("SET B & SET A_copy intersection", set_b.intersection(set_a_copy))
# equivalent to A_copy-C
print("SET A_copy & SET C intersection", set_a_copy.intersection(set_c))
print("SET A after", set_a)
print("SET A_copy before", set_a_copy)
print("SET B after", set_b)
print("SET C after", set_c)

# 5. intersection_update
set_a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
set_a_copy = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
set_b = {1, 3, 5, 7, 9, 11, 13, 15, 17}
set_c = {2, 4, 6, 8, 10, 12, 14, 16, 18}

print("\n")
print("intersection_update Example")
print("SET A before", set_a)
print("SET A_copy before", set_a_copy)
print("SET B before", set_b)
print("SET C before", set_c)
# equivalent to A-B
print("SET A & SET B intersection_update", set_a.intersection_update(set_b))
# equivalent to B-A_copy
print("SET B & SET A_copy intersection_update", set_b.intersection_update(set_a_copy))
# equivalent to A_copy-C
print("SET A_copy & SET C intersection_update", set_a_copy.intersection_update(set_c))
print("SET A after", set_a)
print("SET A_copy before", set_a_copy)
print("SET B after", set_b)
print("SET C after", set_c)

# 6. union
set_a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
set_a_copy = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
set_b = {1, 3, 5, 7, 9, 11, 13, 15, 17}
set_c = {2, 4, 6, 8, 10, 12, 14, 16, 18}

print("\n")
print("union Example")
print("SET A before", set_a)
print("SET A_copy before", set_a_copy)
print("SET B before", set_b)
print("SET C before", set_c)
# equivalent to A-B
print("SET A & SET B union", set_a.union(set_b))
# equivalent to B-A_copy
print("SET B & SET A_copy union", set_b.union(set_a_copy))
# equivalent to A_copy-C
print("SET A_copy & SET C union", set_a_copy.union(set_c))
print("SET A after", set_a)
print("SET A_copy before", set_a_copy)
print("SET B after", set_b)
print("SET C after", set_c)

# 7. isdisjoint - checks whether the two sets are intersect to each other or not
print("\n")
print("isdisjoint example")
set_a = {1, 2, 3, 4, 5}
set_b = {2, 4, 6, 8}
set_c = {9, 11, 13}
print(set_a.isdisjoint(set_b)) # output false
print(set_b.isdisjoint(set_c)) # output true

# 8. issubset - checks whether the set is child set or not
print("\n")
print("issubset example")
set_a = {1, 2, 3, 4, 5}
set_b = {2, 4}
print(set_a.issubset(set_b)) # output false
print(set_b.issubset(set_a)) # output true

# 9. issuperset - checks whether the set is parent set or not
print("\n")
print("issuperset example")
set_a = {1, 2, 3, 4, 5}
set_b = {2, 4}
print(set_a.issuperset(set_b)) # output true
print(set_b.issuperset(set_a)) # output false

# 10. discard - removes specific member from the set
#case one - if the member exist
print("\n")
print("discard example")
set_a = {1, 2, 3, 4, 5}
print(set_a)
set_a.discard(1)
print(set_a)

#case two - if the member doesnot exist - does nothing
print("\n")
print("discard empty set example")
set_a = {1, 2, 3, 4, 5}
print(set_a)
set_a.discard(9)
print(set_a)

# 11. remove - removes specific member from the set
#case one - if the member exist
print("\n")
print("remove example")
set_a = {1, 2, 3, 4, 5}
print(set_a)
set_a.remove(1)
print(set_a)

#case two - if the member doesnot exist - return KeyError
print("\n")
print("remove empty set example")
set_a = {1, 2, 3, 4, 5}
print(set_a)
#set_a.remove(9)
print(set_a)

# 12. pop - removes first member from the set
#case one - if the member exist
print("\n")
print("Pop example")
set_a = {1, 2, 3, 4, 5}
print(set_a)
set_a.pop()
print(set_a)

#case two - if the member doesnot exist - return KeyError
print("\n")
print("Pop empty set example")
set_a = {}
print(set_a)
#set_a.pop()
print(set_a)

# 13. update
print("\n")
print("update example")
set_a = {1, 2, 3, 4, 5}
new_set = {7, 8, 9}
print(set_a)
set_a.update(new_set)
print(set_a)
