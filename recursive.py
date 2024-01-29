#Lambda function:(nameless function)
#A function which doesnt have any name to function then it is said to be nameless function ,and lambda is keyword
#syntax:lambda variables(or)input:expression
#Eg1:
a=[1,2,3,4,5,6,7]
b=lambda a:a*2                   #this is not correct way to give lambda function
print(b)
#output:<function <lambda> at 0x000001D6BB0AA200>

#Eg2:
a=lambda a:a+a 
x=a(4)
print(x)
#output:8

#Eg3:
a=lambda a,b:a/b 
x=a(4,40)
print(x)
#output:0.1

#Eg4:
def fun(n):
    return lambda x:x//n 
z=fun(5)
print(z(10))
#output:2

#Eg5:
def fun(n):
    return lambda x:x//n 
z=fun(5)
z1=fun(10)
print(z(100))
print(z1(200))
#output:
#20
#20

#Eg6:
max=lambda a,b,c: a if a>b and a>c else b if b>c else c 
print(max(11,786,200))
#output:786

#Eg7:
y=lambda a: a%2==0 
print(y(22))
#output:True

#Eg8:
y=lambda a: a%2==0 
print(y(11))
#output:False

#Eg9:
y=lambda a,b:a%2==0
b%2==1
print(y(22,11))
#output:SyntaxError: invalid syntax

#Eg10:
y=lambda a,b,c,d: a%b%c%d==0 
print(y(10,20,30,41))
#output:False