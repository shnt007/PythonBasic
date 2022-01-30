#Identity operator - operates value/variable of non iterable onject
# is
# is not

x1 = 1
y1 = 3
print(x1 is y1)
print(x1 is not y1)

x2 = 'hello'
y2 = 'hello'

print(x2 is y2)
print(x2 is not y2)

x3 = [1, 2, 3]
y3 = [1, 2, 3]

print(x3 is y3)
print(x3 is not y3)

#Membership operator

item_one = ['dharan', 'ktm']
item_two = ['dharan', 'ktm']

item_three = { 'name' : 'ktm', 'age' : 23}
print("membership output")
print("name" in item_three)

print("ktm" in item_three)

print("dharan" in item_two)

#bitwise
# AND &
# OR |
# XOR ^
# NOT ~
# Left Shift X >> Y
# Right Shift X << Y
