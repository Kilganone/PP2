mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit))
mytuple = (10, 20, 30, 40)
myit = iter(mytuple)
print(next(myit))
mytuple = (True, False, True)
myit = iter(mytuple)
print(next(myit))
mytuple = (1, "hello", 3.14, None)
myit = iter(mytuple)
print(next(myit))
mytuple = ("single",)
myit = iter(mytuple)
print(next(myit))

mystr = "banana"
myit = iter(mystr)
print(next(myit))
mystr = "Hello World"
myit = iter(mystr)
print(next(myit))
mystr = "12345"
myit = iter(mystr)
print(next(myit))
mystr = "!@#$%"
myit = iter(mystr)
print(next(myit))
mystr = "A"
myit = iter(mystr)
print(next(myit))

mytuple = ("apple", "banana", "cherry")
for x in mytuple: print(x)
mytuple = ("apple", "banana", "cherry")
for i, x in enumerate(mytuple): print(f"{i}: {x}")
mytuple = (1, 2, 3, 4, 5)
total = 0
for x in mytuple: total += x
print(total)
mytuple = (1, 2, 3, 4, 5, 6)
for x in mytuple:
    if x % 2 == 0: print(x)
mytuple = ("a", "b", "c")
new_list = []
for x in mytuple: new_list.append(x.upper())
print(new_list)

mystr = "banana"
for x in mystr: print(x)
mystr = "hello"
count = 0
for x in mystr:
    if x in "aeiou": count += 1
print(count)
mystr = "python"
for x in mystr: print(x.upper())
mystr = "programming"
for x in mystr:
    if x == "g": print("Found g!")
mystr = "abc"
reversed_str = ""
for x in mystr: reversed_str = x + reversed_str
print(reversed_str)

class CountUp:
    def __iter__(self): self.a = 1; return self
    def __next__(self): x = self.a; self.a += 1; return x
myclass = CountUp()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))

class CountDown:
    def __iter__(self): self.a = 10; return self
    def __next__(self): x = self.a; self.a -= 1; return x
myclass = CountDown()
myiter = iter(myclass)
print(next(myiter))

class PowersOfTwo:
    def __iter__(self): self.a = 1; return self
    def __next__(self): x = self.a; self.a *= 2; return x
myclass = PowersOfTwo()
myiter = iter(myclass)
print(next(myiter))

class Repeat:
    def __iter__(self): return self
    def __next__(self): return "Hello"
myclass = Repeat()
myiter = iter(myclass)
print(next(myiter))

class EvenNumbers:
    def __iter__(self): self.a = 0; return self
    def __next__(self): x = self.a; self.a += 2; return x
myclass = EvenNumbers()
myiter = iter(myclass)
print(next(myiter))

class StopAfter5:
    def __iter__(self): self.a = 1; return self
    def __next__(self):
        if self.a <= 5: x = self.a; self.a += 1; return x
        else: raise StopIteration
for x in StopAfter5(): print(x)

class StopAt50:
    def __iter__(self): self.a = 10; return self
    def __next__(self):
        if self.a <= 50: x = self.a; self.a += 10; return x
        else: raise StopIteration
for x in StopAt50(): print(x)

class CountDown3:
    def __iter__(self): self.a = 3; return self
    def __next__(self):
        if self.a > 0: x = self.a; self.a -= 1; return x
        else: raise StopIteration
for x in CountDown3(): print(x)

class ListIterator:
    def __iter__(self): self.index = 0; self.data = [1, 2, 3]; return self
    def __next__(self):
        if self.index < len(self.data): x = self.data[self.index]; self.index += 1; return x
        else: raise StopIteration
for x in ListIterator(): print(x)

class SquareLimit:
    def __iter__(self): self.a = 1; return self
    def __next__(self):
        if self.a * self.a <= 100: x = self.a * self.a; self.a += 1; return x
        else: raise StopIteration
for x in SquareLimit(): print(x)

def gen1(): yield 1; yield 2; yield 3
for v in gen1(): print(v)

def gen2(): yield "a"; yield "b"; yield "c"
for v in gen2(): print(v)

def gen3(): yield True; yield False
for v in gen3(): print(v)

def gen4(): yield 1.5; yield 2.5
for v in gen4(): print(v)

def gen5(): yield None; yield 0
for v in gen5(): print(v)

def count_up(n):
    c = 1
    while c <= n: yield c; c += 1
for num in count_up(5): print(num)

def count_down(n):
    while n > 0: yield n; n -= 1
for num in count_down(3): print(num)

def squares(n):
    for i in range(n): yield i * i
for num in squares(4): print(num)

def evens(n):
    for i in range(n):
        if i % 2 == 0: yield i
for num in evens(6): print(num)

def fib_gen(n):
    a, b = 0, 1
    for _ in range(n): yield a; a, b = b, a + b
for num in fib_gen(5): print(num)

def simple_gen(): yield "A"; yield "B"; yield "C"
gen = simple_gen()
print(next(gen))

def num_gen(): yield 10; yield 20
gen = num_gen()
print(next(gen))

def mix_gen(): yield 1; yield "x"
gen = mix_gen()
print(next(gen))

def bool_gen(): yield True
gen = bool_gen()
print(next(gen))

def float_gen(): yield 3.14
gen = float_gen()
print(next(gen))

gen_exp1 = (x for x in range(3))
print(list(gen_exp1))

gen_exp2 = (x * 2 for x in range(3))
print(list(gen_exp2))

gen_exp3 = (x for x in "abc")
print(list(gen_exp3))

gen_exp4 = (x + 1 for x in [1, 2, 3])
print(list(gen_exp4))

gen_exp5 = (x for x in range(5) if x > 2)
print(list(gen_exp5))

total1 = sum(x for x in range(5))
print(total1)

total2 = sum(x * x for x in range(3))
print(total2)

total3 = sum(x for x in [1, 2, 3])
print(total3)

total4 = sum(x for x in range(10) if x % 2 == 0)
print(total4)

total5 = sum(x + 1 for x in range(4))
print(total5)

def echo():
    while True:
        received = yield
        print("Received:", received)
gen = echo()
next(gen)
gen.send("Hi")

def echo2():
    while True:
        received = yield
        print("Got:", received)
gen = echo2()
next(gen)
gen.send("Hello")

def echo3():
    while True:
        received = yield
        print("Msg:", received)
gen = echo3()
next(gen)
gen.send("Test")

def my_gen():
    try: yield 1
    finally: print("Closed")
gen = my_gen()
print(next(gen))
gen.close()

def my_gen2():
    try: yield 2
    finally: print("Ended")
gen = my_gen2()
print(next(gen))
gen.close()

def my_gen3():
    try: yield 3
    finally: print("Done")
gen = my_gen3()
print(next(gen))
gen.close()

def my_gen4():
    try: yield 4
    finally: print("Finish")
gen = my_gen4()
print(next(gen))
gen.close()

def my_gen5():
    try: yield 5
    finally: print("Stop")
gen = my_gen5()
print(next(gen))
gen.close()