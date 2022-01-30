# function
# function syntax
# def <function_name> () :
#   expression

def say_hello():
    print("Hello World")

say_hello()

number_one = 45
number_two = 44

def add_two_num(num_one, num_two):
    print("The sum of two numbers is :", num_one + num_two)

add_two_num(number_one, number_two)
add_two_num(45, 55)
add_two_num(45.444, 78.8754)

# documentation of function

def get_address():
    """This function takes no parameter and prints address"""
    print("the address is baneswhor")
    
get_address()
print(get_address.__doc__)


# prime number

for i in range(1,20):
    if i > 1:
        for num in range(2, i):
            if i % num == 0:
                print("is not prime", i)
                break
        else:
            print("is a prime", i)

# task
# 1. factorial number
# 2. palindrome
# 3. loop in dictionary
  

        
        
    
