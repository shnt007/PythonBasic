# file handling
# r - to read the existing file
# w - to write the file ( it removes all content and
# adds new content to the file)
# a - to append new content in the file ( it adds content after existing content)
# x - to create new file ( it throws error if the file already exists )

# t - to save the file as text - text document
# b - to save the file as binary - image

# 1. open - this method opens the file from the given directory
# Note:- here f is a variable in which we are saving the file
f = open("C:\\Users\\PC\\Documents\\File handling.txt", "w")

# 2. write - this method writes the content we want to write in the file
f.write("Hello this is a test for file handling \nthis is second line")

# 3. close - this method closes the file once the operation is completed
# note - we must use close() method once we open the file 
f.close()

f = open("C:\\Users\\PC\\Documents\\File handling.txt", "r")

# 4. readline() - this method reads the particular line i.e first line in the file content
# to read the multiple line we have to call the function multiple time
#print(f.readline())
#print(f.readline())
f.close()

# 5. read - this method also read the content in the file but returns all content in the file
f = open("C:\\Users\\PC\\Documents\\File handling.txt", "r")
#print(f.read())
f.close()

# we can also use loop to print the content in the file
f = open("C:\\Users\\PC\\Documents\\File handling.txt", "r")
print("only i")
for i in f:
    print(i)
    
print("read") # does nothing
for i in f:
    print(f.read(i))
    
print("readline") # does nothing
for i in f:
    print(f.readline(i))

# 6.  a - append
# difference between a and w
# a - appends the new content without removing existing content in the file
# w - removes all content and adds new content in the file

# using append a - check by commenting the write example after append to check the output of a
f = open("C:\\Users\\PC\\Documents\\File handling.txt", "a")
f.write("\nThis is line third")
f.close()

f = open("C:\\Users\\PC\\Documents\\File handling.txt", "r")
print(f.read())
f.close()

# using write w again in the file
f = open("C:\\Users\\PC\\Documents\\File handling.txt", "w")
f.write("This is all new content that i updated using w")
f.close()

f = open("C:\\Users\\PC\\Documents\\File handling.txt", "r")
print(f.read())
f.close()
