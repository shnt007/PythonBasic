"""count = 0
while (count < 3):
    count = count + 1
    print ("Fine")
else:
    print("ok")"""

# primary number upto 20
"""num = 19
for i in range(1,20):
    if i > 1:
        if num % i == 0:
            print("IS Prime Number")
        else:
            print("Is not prime number")
        """

# Example of Palindrome
def isPalindrome(s):
    return s == s[::-1]

# Driver code
s = "malayalam"
ans = isPalindrome(s)

if ans:
    print("Yes")
else:
    print("No")


# Example of factorial number : 1
def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while (n > 1):
            fact *= n
            n -= 1
        return fact

num = 5;
print("Factorial of", num, "is", factorial(num))

# Example 2
def factorial(n):
    # single line to find factorial
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1);

num = 5;
print("Factorial of", num, "is",
      factorial(num))

# Example of loop in dictionary
myDict = {"A" : 2, "B" : 5, "C" : 6}
for i in myDict.values():
    print(i)