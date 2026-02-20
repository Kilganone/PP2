class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

x = Person("John", "Doe")
x.printname()

class Student(Person):
    pass

y = Student("Mike", "Olsen")
y.printname()

class Teacher(Person):
    def __init__(self, fname, lname, subject):
        Person.__init__(self, fname, lname)
        self.subject = subject

t = Teacher("Anna", "Smith", "Math")
t.printname()
print(t.subject)

class Employee(Person):
    def __init__(self, fname, lname, company):
        super().__init__(fname, lname)
        self.company = company

e = Employee("Tom", "Brown", "Google")
e.printname()
print(e.company)