def args1(*nums): print("Args:", nums)
def args2(*nums): print("Sum:", sum(nums))
def args3(*nums): print("Max:", max(nums))
def args4(*nums): 
    for n in nums: print(n)
def args5(*nums): print("Count:", len(nums))

args1(1,2,3)
args2(10,20,30)
args3(5,9,2)
args4(7,8,9)
args5(1,2,3,4,5)

def args_reg1(greet, *names): 
    for n in names: print(greet, n)
def args_reg2(greet, *names): 
    print(greet, "and", names)
def args_reg3(msg, *nums): 
    print(msg, sum(nums))
def args_reg4(msg, *vals): 
    for v in vals: print(msg, v)
def args_reg5(title, *items): 
    print(title, items)

args_reg1("Hi", "A","B","C")
args_reg2("Hello", "X","Y")
args_reg3("Total:", 1,2,3)
args_reg4("Item:", 10,20)
args_reg5("Fruits", "apple","banana","cherry")

def kw1(**info): print(info)
def kw2(**info): print("Keys:", list(info.keys()))
def kw3(**info): print("Values:", list(info.values()))
def kw4(**info): 
    for k,v in info.items(): print(k,v)
def kw5(**info): print("Name:", info.get("name"))

kw1(a=1,b=2)
kw2(x=10,y=20)
kw3(name="Emil",age=25)
kw4(city="Oslo",country="Norway")
kw5(name="Tobias",lname="Refsnes")

def kw_reg1(user, **details): print(user, details)
def kw_reg2(user, **details): 
    for k,v in details.items(): print(k,v)
def kw_reg3(name, **info): print(name, info)
def kw_reg4(name, **info): print("User info:", info)
def kw_reg5(username, **data): print(username, data)

kw_reg1("emil123", age=25, city="Oslo")
kw_reg2("anna456", hobby="coding", country="Norway")
kw_reg3("linus", score=95, level=5)
kw_reg4("kate", skill="Python", xp=100)
kw_reg5("tom", height=180, weight=75)

def combo1(title, *args, **kwargs): print(title, args, kwargs)
def combo2(title, *args, **kwargs): 
    print(title); print("Args:", args); print("Kw:", kwargs)
def combo3(t,*a,**k): print(t,a,k)
def combo4(t,*a,**k): print("Title:", t, "Args:", a, "Kw:", k)
def combo5(t,*a,**k): print(t,sum(a),k)

combo1("Info","A","B",x=1,y=2)
combo2("Data",1,2,3,a=10,b=20)
combo3("Test","X","Y",foo=5,bar=6)
combo4("Hello",10,20,key="val")
combo5("Sum",5,10,15,m=1,n=2)