# Range with loop and list index

ethnic_groups = ["Gurung", "Tharu", "Maithli", "Magar"]

# printing the index of the list 
for i in range(len(ethnic_groups)):
    print(i)

# printing the value of list through index number
for i in range(len(ethnic_groups)):
    print(ethnic_groups[i])

# implementing conditional statement in for loop
# for with else
ethnic_name = "Tharu"

for name in ethnic_groups:
    if name is ethnic_name:
        print("Is in the list")
    else:
        print("Is not in the list")
else:
    print("No more item")


for i in range(len(ethnic_groups)):
    if ethnic_groups[i] is ethnic_name:
        print("is in the list")
    else:
        print("is not in the list")
else:
    print("No more item")

# while loop syntax
# while condition
#   expression

email = ["sandesh@gmail.com", "gg@gmail.com", "hello@gmail.com"]

while email[1] is "gg@gmail.com" :
    print("Email found")
    break

counter = int(0)
while email[counter] is "hello@gmail.com":
    print("Found")
    counter += 1
    break



