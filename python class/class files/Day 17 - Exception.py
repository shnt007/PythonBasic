# Exception Example

# 1. Basic Exception
try:
    num = int(input("Enter a number: "))
    print(num)
except:
    print("Must be a numeric value")

# 2. Else - if no need to check for errors
try:
    name = str(input("Enter you name: "))
    print(name)
except:
    print("Check you name properly")
else:
    address = "Kathmandu"
    print(address)

# 3. finally
try:
    f = open("C:/Users/PC/Documents/5-6 File.txt", "r")
    print(f.read())
except:
    print("File not found")
finally:
    f.close()
    print("File closed")

# 4. specific exception
try:
    num = int(input("Enter a number: "))
    print(num)
except ValueError:
    print("ValueError: Must be a numeric value")

# 5. multiple exception

try:
    num = int(input("Enter a number: "))
    print(num)
    print(100/0)
except(ValueError, ZeroDivisionError):
    print("ValueError: Must be a numeric value")
    print("ZeorDivisionError: Number Can't be divide by zero")

# 6. with specific error message
try:
    num = int(input("Enter a number: "))
    print(num)
    print(100/0)
except(ValueError, ZeroDivisionError) as error:
    print(error)

# 7. with specific exception, error and extra errors
try:
    num = int(input("Enter a number: "))
    print(num)
    print(100/0)
except ZeroDivisionError as zde:
    print(zde)
except:
    print("Must be numeric value")


