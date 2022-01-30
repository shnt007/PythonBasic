boys_name = ["ram","shyam","hari","kiran"]
for i in range(len(boys_name)):
        print(i)

for i in range(len(boys_name)):
    print(boys_name[i])

girl_name = "hari"
for name in boys_name:
    if name is girl_name:
        print("Item is in list")
    else:
        print("NO more names")
else:
    print("Not in list")

for i in range(len(boys_name)):
    if boys_name[i] is girl_name:
        print("No need to search found")
    else:
        print("Is not in list")
else:
    print("The End ")


email = ["abc@gmail.com","aaa@gmail.com","bbb@gmail.com","ccc@gmail.com"]
while email[1] in "bbb@gmail.com":
    print("Email found")
    break
