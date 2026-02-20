class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

s1 = Student("Mike", "Olsen", 2019)
print(s1.firstname, s1.lastname, s1.graduationyear)

class Teacher(Person):
    def __init__(self, fname, lname, subject):
        super().__init__(fname, lname)
        self.subject = subject

t1 = Teacher("Anna", "Smith", "Math")
print(t1.firstname, t1.lastname, t1.subject)

class Employee(Person):
    def __init__(self, fname, lname, company):
        super().__init__(fname, lname)
        self.company = company

e1 = Employee("Tom", "Brown", "Google")
print(e1.firstname, e1.lastname, e1.company)