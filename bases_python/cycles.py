print("FOR LOOP")
n = int(input("How many names do you want to enter?:"))
list_for = []
# Entering names
for i in range(n):
    name_for = (input("Insert name:"))
    list_for.insert(i, name_for)
# Printing of names
print("\t\tList of the names:")
for i in range(n):
    print("The name in position ", i, "is: ", list_for[i])

print("WHILE LOOP")
list_while = []
j = 0
# Entering names
while j < n:
    name_while = (input("Insert name:"))
    list_while.insert(j, name_while)
    j+= 1
j = 0
# Printing of names
print("\t\tList of the names:")
while j < n:
    print("The name in position ", j, "is: ", list_for[j])
    j+= 1