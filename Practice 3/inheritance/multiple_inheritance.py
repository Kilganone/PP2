class Father:
    def skills(self):
        print("Gardening, Carpentry")

class Mother:
    def skills(self):
        print("Cooking, Art")

class Child(Father, Mother):
    pass

c = Child()
c.skills()  # наследует первый родительский метод (Father)

class Child2(Father, Mother):
    def skills(self):
        super().skills()
        print("Also knows Coding")

c2 = Child2()
c2.skills()

class Parent1:
    def feature(self):
        print("Feature from Parent1")

class Parent2:
    def feature(self):
        print("Feature from Parent2")

class MultiChild(Parent1, Parent2):
    def feature(self):
        print("Overridden Feature")
        super().feature()

mc = MultiChild()
mc.feature()