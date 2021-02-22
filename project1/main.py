# Exercise on the use of classes and modules
from class_students import students       
choice = 1
print("\t\t~Insertion of the first student:~")
name = str(input("Insert name:"))
surname = str(input("Insert surname:"))
age = float(input("Insert age:"))
address = str(input("Insert address:"))
st = students(name, surname, age, address)
while choice != 0:
    # ""Switch""
    print("""
    \t\t~Choice menu':~
    0-Exit,
    1-To insert a new student,
    2-To search a student,
    3-To print all students.
    """)
    choice = int(input("Choice:"))
    if choice == 1:
        name = str(input("Insert name:"))
        surname = str(input("Insert surname:"))
        age = float(input("Insert age:"))
        address = str(input("Insert address:"))
        students(name, surname, age, address)
    elif choice == 2:
        st.search_student
    elif choice == 3:
        st.print()
    else:
        print("ERROR==>Inserted option not available") 

