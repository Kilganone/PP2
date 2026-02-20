def f1(name): print("Hi", name)
def f2(name): print("Hello", name)
def f3(name): print("Hey", name)
def f4(name): print("Welcome", name)
def f5(name): print("Bye", name)

f1("A"); f2("B"); f3("C"); f4("D"); f5("E")


def full1(a,b): print(a,b)
def full2(a,b): print(b,a)
def full3(a,b): print(a+"-"+b)
def full4(a,b): print(a.upper(),b.upper())
def full5(a,b): print(a[0],b)

full1("A","B"); full2("C","D"); full3("E","F"); full4("g","h"); full5("I","J")


def d1(x="friend"): print(x)
def d2(x=10): print(x)
def d3(x="NY"): print(x)
def d4(x=True): print(x)
def d5(x=0): print(x)

d1(); d2(); d3(); d4(); d5()


def k1(a,b): print(a,b)
def k2(a,b): print(a+b)
def k3(a,b): print(a*b)
def k4(a,b): print(a,b)
def k5(a,b): print(a,b)

k1(a=1,b=2); k2(a=2,b=3); k3(a=3,b=4); k4(a=4,b=5); k5(a=5,b=6)


def m1(a,b,c): print(a,b,c)
def m2(a,b,c): print(a+b+c)
def m3(a,b,c): print(a*b*c)
def m4(a,b,c): print(a,b,c)
def m5(a,b,c): print(a,b,c)

m1(1,b=2,c=3); m2(2,b=3,c=4); m3(3,b=4,c=5); m4(4,b=5,c=6); m5(5,b=6,c=7)


def r1(a,b): return a+b
def r2(a,b): return a-b
def r3(a,b): return a*b
def r4(a,b): return a/b
def r5(a,b): return a**b

print(r1(1,2), r2(3,1), r3(2,3), r4(6,2), r5(2,3))


def pos1(a,/): print(a)
def pos2(a,/): print(a)
def pos3(a,/): print(a)
def pos4(a,/): print(a)
def pos5(a,/): print(a)

pos1(1); pos2(2); pos3(3); pos4(4); pos5(5)


def kw1(*,a): print(a)
def kw2(*,a): print(a)
def kw3(*,a): print(a)
def kw4(*,a): print(a)
def kw5(*,a): print(a)

kw1(a=1); kw2(a=2); kw3(a=3); kw4(a=4); kw5(a=5)


def c1(a,b,/,*,c): return a+b+c
def c2(a,b,/,*,c): return a*b+c
def c3(a,b,/,*,c): return a-b+c
def c4(a,b,/,*,c): return a+b-c
def c5(a,b,/,*,c): return a*b-c

print(c1(1,2,c=3), c2(2,3,c=4), c3(5,2,c=1), c4(4,1,c=2), c5(3,2,c=1))