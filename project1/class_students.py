
class students:
    name = []
    surname = []
    age = []
    address = []
    #Constructor
    def __init__(self,name,surname,age,address):
        self.name.append(name)
        self.surname.append(surname)
        self.age.append(age)
        self.address.append(address)
    #Method to search for a student and print his data
    def search_student(self):
        search_student = str(input("Insert the name of the student you want to search for:"))
        try:
            i=self.name.index(search_student)
            print("\t\t~Student data:~")
            print("Name = %s" % self.name[i])
            print("Surame = %s" % self.surname[i])
            print("Age = %s" % self.age[i])
            print("Address = %s" % self.address[i])
        except:
            print("ERROR==>Item not found")
    #Method for printing 
    def print(self):
        l = len(self.name)
        for i in range(l):
            print("\t\t~List of students:~")
            print("Student number %s:" % (i+1))
            print("Name = %s" % self.name[i])
            print("Surame = %s" % self.surname[i])
            print("Age = %s" % self.age[i])
            print("Address = %s" % self.address[i])