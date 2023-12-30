a=lambda n:n*n
print(a(3))
a=lambda a,b:a if a>b else b
print(a(3,8))
x=lambda a:a+10
print(x(7))
x=lambda a:a-5
print(x(10))
x=lambda a,b:a*b
print(x(5,6))
def func(x):
    return lambda a:a*x
x=func(2)
print(x(11))
s=lambda n:n*n
for i in range(1,12):
    print(i)
s=lambda n:n*n
for i in range(1,12):
    print("square of {} is {}:",format(s(i)))  
even=[lambda arg=x:arg*10 for x in range(1,5)]
for i in even:
    print(i())  