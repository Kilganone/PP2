class Person1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person1("Emil", 36)
p2 = Person1("Tobias", 25)
p3 = Person1("Linus", 28)
print(p1.name, p1.age)
print(p2.name, p2.age)
print(p3.name, p3.age)

class Person2:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age

p1 = Person2("Anna")
p2 = Person2("Olga", 22)
print(p1.name, p1.age)
print(p2.name, p2.age)

class Person3:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

p1 = Person3("Linus", 30, "Oslo")
p2 = Person3("Emil", 35, "Bergen")
print(p1.name, p1.age, p1.city)
print(p2.name, p2.age, p2.city)

class Person4:
    def __init__(self, name, age, city, country):
        self.name = name
        self.age = age
        self.city = city
        self.country = country

p1 = Person4("Tobias", 25, "Stockholm", "Sweden")
p2 = Person4("Kate", 28, "Helsinki", "Finland")
print(p1.name, p1.age, p1.city, p1.country)
print(p2.name, p2.age, p2.city, p2.country)

class Person5:
    def __init__(self, name, age, hobbies=[]):
        self.name = name
        self.age = age
        self.hobbies = hobbies

p1 = Person5("Emil", 30, ["reading","cycling"])
p2 = Person5("Anna", 25, ["painting"])
print(p1.name, p1.age, p1.hobbies)
print(p2.name, p2.age, p2.hobbies)