# set - unordered list, unchangable and unique items

x = {1, 2,2, 3, 4,5, 5}
print(x)
#output - {1, 2, 3,4, 5}

# add - adds new item in set
country = {"Nepal", "India", "Bhutan"}
country.add("Maldives")
country.add("Pakistan")
country.add("Afganistan")
country.add("Sri Lanka")
country.add("Bangladesh")
print(country)

# A. copy - replicates all item of primary set to new set
country_saarc = country.copy()
print(country_saarc)

# B. clear - removes all item from the set
#country.clear()
print(country)

# C. difference - compares the items in two set but
# gives priority to the primary set
country.add("China")
country.add("Vetnam")
country.add("Colombo")
country.add("Australia")

print(country)
print(country_saarc.difference(country))
print(country.difference(country_saarc))

# D. difference set - removes item from another set of primary set
print(country.difference_update(country_saarc))
#print(country_saarc.difference_update(country))
print(country)
print(country_saarc)

# E. discard - removes item from set if the item is available
# 1. case one - if available
print(country.discard("Australia"))
print(country)

# 2. case two - if not available - does nothing
print(country.discard("Brazil"))
print(country)

# F. remove - removes item from set if available but throws
# KeyError is the item is not available

# 1. Case one - if available
print(country.remove("Vetnam"))
print(country)

# 2. Case two - if not available
#print(country.remove("Brazil"))
print(country)

# G. pop - removes random set item from the primary set if
# the targeted items set is available otherwise and returns the removed item
# throws KeyError

# 1. Case one - if item available
print(country_saarc.pop())
print(country_saarc)

# 2. Case two - if item not available
#blank_set_to_test_pop = {}
#print(blank_set_to_test_pop.pop())

# \ - line continues

# H. symmetric_difference - returns new set of exactly available items from the difference of two compared set
virus = {"Covid19", "Swine Flu", "Swedish Flu"}
print("Virus", virus)

common_disease = {"Malaria", "Dengue", \
                  "Cold", "Fever", "Covid19"\
                  , "Swine Flu"}
print("Common Disease", common_disease)

# less item available set
#print("Less item set", virus.symmetric_difference(common_disease))

# more item available set
#print("More item set", common_disease.symmetric_difference(virus))

# symmetric_difference_update - updates self and another set
# less item available set
test_set = {1, 2, 5, 6}
test_set_i = {7, 3, 2, 4}

test_set_ii = { 9, 11, 15, 20}
result = test_set.symmetric_difference_update(test_set_i)
print(test_set)
print(result)
result = test_set_i.symmetric_difference_update(test_set_ii)
print(test_set_i)
print(test_set_ii)

virus.symmetric_difference_update(common_disease)
print(virus)
# more item available set
common_disease.symmetric_difference_update(virus)
print(common_disease)

# difference, difference_update, symmetric_difference
# symmetric_difference_update example revision

# difference equivalent to onlyA-B set theory
set_a = {1, 3, 5, 7, 9}
set_b = {1, 2, 3, 4, 5, 6, 7, 8 , 9, 0}
print("difference Example output")
print("Set A before", set_a)
print("Set B before", set_b)
print("Set A difference", set_a.difference(set_b))
print("Set B difference", set_b.difference(set_a))
print("Set A after", set_a)
print("Set B after", set_b)

# difference_update
set_a = {1, 3, 5, 7, 9}
set_a_copy = {1, 3, 5, 7, 9}
set_b = {1, 2, 3, 4, 5, 6, 7, 8 , 9, 0}
print("difference_update Example output")
print("Set A before", set_a)
print("Set B before", set_b)
print("Set A difference_update", set_a.difference_update(set_b))
print("Set B difference_update", set_b.difference_update(set_a_copy))
print("Set A after", set_a)
print("Set B after", set_b)

# symmetric_difference - equivalent to A - B set theory
set_a = {1, 3, 5, 7, 9, 11, 13, 15, 17}
set_b = {1, 2, 3, 4, 5, 6, 7, 8 , 9, 0}

print("symmetric_difference Example output")
print("Set A before", set_a)
print("Set B before", set_b)
print("Set A symmetric_difference", set_a.symmetric_difference(set_b))
print("Set B symmetric_difference", set_b.symmetric_difference(set_a))
print("Set A after", set_a)
print("Set B after", set_b)


# symmetric_difference_update - equivalent to A - B set theory
set_a = {1, 3, 5, 7, 9, 11, 13, 15, 17}
set_a_copy = {1, 3, 5, 7, 9, 11, 13, 15, 17}
set_b = {1, 2, 3, 4, 5, 6, 7, 8 , 9, 0}
print("symmetric_difference_update Example output")
print("Set A before", set_a)
print("Set B before", set_b)
print("Set A symmetric_difference_update", set_a.symmetric_difference_update(set_b))
print("Set B symmetric_difference_update", set_b.symmetric_difference_update(set_a_copy))
print("Set A after", set_a)
print("Set B after", set_b)


# I. intersection - equivalent to AnB in SET Theory
set_a = {1, 3, 5, 7, 9, 11, 13, 15, 17}
set_b = {1, 2, 3, 4, 5, 6, 7, 8 , 9, 0}
print("Intersection Example output")
print("Set A before", set_a)
print("Set B before", set_b)
print("Set A intersection", set_a.intersection(set_b))
print("Set B intersection", set_b.intersection(set_a))
print("Set A after", set_a)
print("Set B after", set_b)

# I. intersection_update - equivalent to AnB in SET Theory
set_a = {1, 3, 5, 7, 9, 11, 13, 15, 17}
set_a_copy = {1, 3, 5, 7, 9, 11, 13, 15, 17}
set_b = {1, 2, 3, 4, 5, 6, 7, 8 , 9, 0}
print("intersection_update Example output")
print("Set A before", set_a)
print("Set B before", set_b)
print("Set A intersection_update", set_a.intersection_update(set_b))
print("Set B intersection_update", set_b.intersection_update(set_a_copy))
print("Set A after", set_a)
print("Set B after", set_b)

# J. update - updates the set
set_a = {1, 3, 5, 7, 9, 11, 13, 15, 17}
new_set_item = { 19, 21, 23, 25}
print(set_a)
set_a.update(new_set_item)
print(set_a)

# K. union - A union B set theory - returns as a new set
set_a = {1, 3, 5, 7, 9, 11, 13, 15, 17}
set_b = {1, 2, 3, 4, 5, 6, 7, 8 , 9, 0}
print(set_a)
print(set_a.union(set_b))
print(set_a)

# L. issubset - checks whether the set is child set or not
set_a = {1, 3, 5, 7, 9, 11, 13, 15, 17}
subset_of_a = { 1, 3, 5}
print(subset_of_a.issubset(set_a)) #output - true

# M. issuperset - checks whether the set is parent set or not
set_a = {1, 3, 5, 7, 9, 11, 13, 15, 17}
subset_of_a = { 1, 3, 5}
print(set_a.issuperset(subset_of_a)) #output - true

# N. isdisjoint - checks whether the sets are intersect to each other or not 
set_a = {1, 3, 5, 7, 9}
set_b = { 7, 9, 11, 13, 15, 17}
print(set_a.isdisjoint(set_b)) # output false

set_a = {1, 3, 5, 7, 9}
set_b = { 11, 13, 15, 17}
print(set_a.isdisjoint(set_b)) # output true
