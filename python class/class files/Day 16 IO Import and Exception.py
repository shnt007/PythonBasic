# input and import
# input() - method is used to take certain input from the user

# int
'''print("Welcome to MindRisers CLI App")
passcode = str(input("Enter your passcode :"))
if passcode == "5566":
    username = str(input("Enter your username: "))
    if username == "mindrisersandes":
        print("Welcome", username)
        print("Please fill up your KYC")
        print("KYC Details")
        # example for multiple input
        first_name = str(input("Enter first name: "))
        middle_name = str(input("Enter middle name: "))
        last_name = str(input("Enter last name: "))
        contact = str(input("Enter your phone number: "))
        email = str(input("Confirm your email address: "))
        details = "First Name: " + first_name + " " + \
                  "Middle Name: " + middle_name + " " + \
                  "Last Name: " + last_name + " " +  \
                  "Contact : " + contact + " " + \
                  "Email : " + email
        if email == "sandesh@gmail.com":
           print(details)
        else:
            print("You entered a wrong email address")
    else:
        print("Invalid username")
else:
    print("Please enter a valid passcode. Thank you :)")
'''
# import - this keyword is used to include certain built-in packages or libraries of python
import math
import sys
#print(math.pi)
#print(sys.path)

# Exception
# Error types
# 1. ZeroDivisionError
# 2. SyntaxWarning
# 3. KeyError
# 4. ValueError
# 5. IoError
# 6. SystemError
# 7. UnicodeTranslateError
# 8. UnicodeDecodeError
# 9. UnicodeEncodeError
# 10. TypeError
# 11. IndentationError
# 12. RuntimeError
# 13. OverflowError
# 14. MemoryError

# Syntax - 1
# try:
#   block of code
# except:
#   print("Message")

# Syntax - 2  Else
# try:
#   block of code
# except:
#   print("Message")
# else:
#   extra code not needed to check errors

# Syntax - 3 Finally - GUI, Network or Server response
# finally block will execute anyhow
# try:
#   block of code
# finally:
#   block of code

# input exception
# without exception handling
number = int(input("Enter a number: "))
print(number)

# with exception handling
try:
    num = int(input("Enter a number: "))
    print(num)
except:
    print("Must be numeric value")

#print(100/0)
try:
    print(100/0)
except:
    print("Cannot be divided by zero")
