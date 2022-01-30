# File Handling

# r - to read the file
# w - to write the file
# a - to append content in the file
# x - to create new file

# t - to save file as a text document - text, docx
# b - to save file as a binary document - image

# Note while creating or updating file
# 1. difference between w and a
# a - appends new content after existing content
# w - removes all content and adds new content

# 2. while creating file using x
# if the file already exist throws error

# 3. directory - must define the directory
# source - to read the file
# destination - to write the file

# example

# 1. open() - this method takes two parameter to open the file
# paramter one - source directory
# for source directory we must use double forward slash \\ or / single back slash
# param two - file reading keyword
# here f is a variable where we are saving the file
'''f = open("C:\\Users\\PC\\Documents\\9-10 File.txt", "r")
print(f.readline())
f.close()

# 2. close() - this method is use to close the file
# 3. readline() - this method is use to read the single line
# in the file
# a. if we want to read multiple line we have to use
# readline method multiple times

# 4. read() - this method reads all line in the file
f = open("C:\\Users\\PC\\Documents\\9-10 File.txt", "r")
print(f.read())
f.close()

# 5. write() - this method writes new content in the file
f = open("C:\\Users\\PC\\Documents\\9-10 File.txt", "w")
f.write("This is line one for testing file handling.\nThis is second line")
f.close()

f = open("C:\\Users\\PC\\Documents\\9-10 File.txt", "r")
print(f.read())
f.close()

print("\n") # \n - new line

f = open("C:\\Users\\PC\\Documents\\9-10 File.txt", "r")
#print(f.readline(5)) # here 5 is the size of line
#print(f.readline())
f.close()

# trying loop to read the content of the file
f = open("C:\\Users\\PC\\Documents\\9-10 File.txt", "r")
for i in f:
    print(i)
f.close()

# 6. a (append) - adds new line after the existing content
f = open("C:\\Users\\PC\\Documents\\9-10 File.txt", "a")
f.write(". This part is added by append.\nThis is new line using append")
f.close()

print("\n") # \n - new line
f = open("C:\\Users\\PC\\Documents\\9-10 File.txt", "r")
print(f.read())
f.close()

# using write again to check its impact
f = open("C:\\Users\\PC\\Documents\\9-10 File.txt", "w")
f.write("This is whole new content after wiping all data from previous content")
f.close()

print("\n") # \n - new line
f = open("C:\\Users\\PC\\Documents\\9-10 File.txt", "r")
print(f.read())
f.close()'''
# escape string - \//\\

# 7. readlines() - returns the list of line
f = open("C:/Users/PC/Documents/9-10 File.txt", "r")
print(f.readlines())
f.close()

# x - create file
f = open("C:/Users/PC/Documents/Binary_File_create.txt","x")
f.write("This is test")
f.close()

'''f = open("C:/Users/PC/Documents/9-10 File_create.txt","a")
f.write(".\nThis is test appended line.")
f.close()
'''
