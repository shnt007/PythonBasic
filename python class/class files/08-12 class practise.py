Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Example of identity
x = 5
y=5

print(x=y)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(x=y)
TypeError: 'x' is an invalid keyword argument for print()
print(x is y)
True
print (x is not y)
False

#Example of membership

print (x in y)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print (x in y)
TypeError: argument of type 'int' is not iterable
x = [1,2,3]
y = [1,2,3]
print (x in y)
False
print (x not in y)
True
print (1 in x)
True
x in y
False
 item_1 = ['mango','apple']
 
SyntaxError: unexpected indent
item_1 = ['mango','apple']
item_2 = ['hellow','world']
item_3 = {'name':'sandesh','age':21}
item_3 = {'name':'ram','age':24}
item_1 in item_2
False
item_1 not in item_2
True
