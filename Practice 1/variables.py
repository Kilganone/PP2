#Python variables
a=25
b="John"
print(b)
print(a)
print(b, "is", a, "years old!")
x=5
x="Jordan" #use of the same variable will change the value
print(x)
a="Sara"
A="Lora"
print(a, A) # a and A are different variables
Apple=12
apple=25
print(int(Apple), float(apple))#float value has digits after .
a=20
print(str(a))#prints string
print(int(a))#prints integer
print(float(a))#prints float
c='15.5'
print(str(c))#prints string
print(float(c))#prints float
print(int(float(c)))#prints int
p=27.9
print(str(p))#prints string
print(int(p))#prints int
#variable names
#examples of defining the variable
_example=123
Example=245
EXAMPLE=12
example=123123
ex_ample=321
example1=1232
print(_example, Example, EXAMPLE, example, ex_ample, example1)
#assign multiple values
#this is also one more variant
exp1,EXP2,eXP3=1,2,3
print(exp1, EXP2, eXP3)
#one more
x1=x2=x3=5
print(x1,x2,x3)
#again
nums=[251, 15, 256]
num1,num2,num3=nums
print(num1, num2, num3)
#output variables
parts=["Conti", "nen", "tial"]
n1,n2,n3=parts
#concatenation
print(n1+n2+n3)
print(n1,n2,n3)
u1=24
u2="John"
print(u1,u2)
#global variables
var=25
print(var)
def func():
    x=26
    print(x)
func()
print(var)
def func2():
    global x     #global variable change the value out of the function
    x=256
func2()
print(x)



_name='John'
print(_name)
def change_name():
    global _name
    _name='Mike'
print(_name)
change_name()
print(_name)