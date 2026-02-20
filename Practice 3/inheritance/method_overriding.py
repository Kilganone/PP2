class Person:
    def greet(self):
        print("Hello!")

class Student(Person):
    def greet(self):
        print("Hi, I am a student!")

s = Student()
s.greet()

class Teacher(Person):
    def greet(self):
        super().greet()
        print("I am also a teacher.")

t = Teacher()
t.greet()

class Employee(Person):
    def greet(self):
        print("Greetings from employee.")
        super().greet()

e = Employee()
e.greet()