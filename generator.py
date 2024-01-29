 #Generatores: It is used to generate sequence of values
#Eg1:
def table(num):
    for i in range(1,11):
        print(num,'x',i,'=',num*i)
table(5)
#output:
#5 x 1 = 5
#5 x 2 = 10
#5 x 3 = 15
#5 x 4 = 20
#5 x 5 = 25
#5 x 6 = 30
#5 x 7 = 35
#5 x 8 = 40
#5 x 9 = 45
#5 x 10 = 50
#Without using generator i created a code now using return same code i will excuite 
def table(num):
    for i in range(1,11):
        return f'{num}x{i}={num*i}'
print(table(5))
#output:5x1=5
#i got only first row by using return keyword,because return keyword gives the values only once next time it wont repeat it will stop after excuting first line of code
#so in these sectivation i use generators

#so in case we use yield keyword insted of return keyword to generate the values in sequence
#Eg2:
def table(num):
    for i in range(1,11):
        yield f'{num}x{i}={num*i}'
print(table(5))
#output:<generator object table at 0x000001AC8A0F4E50>
#Now i got output like generator object,so it is telling that it is a generator object when we use yelid keyword inside the function
#So to get values we should print it by using for loop

#Eg3:These is call generator
def table(num):
    for i in range(1,11):
        yield f'{num}x{i}={num*i}'
v=table(5)
for x in v:
    print(x)
#output:
#5x1=5
#5x2=10
#5x3=15
#5x4=20
#5x5=25
#5x6=30
#5x7=35
#5x8=40
#5x9=45
#5x10=50

#Eg4:same programm i will do with return keyword it will come or not we will see
def table(num):
    for i in range(1,11):
        return f'{num}x{i}={num*i}'
v=table(5)
for x in v:
    print(x)
#output:
#5
#x
#1
#=
#5

#Eg5:By using return keyword i m not getting total 5table,now i will show you by using return keyword how to get total 5table
def table(num):
    tablelist=[]
    for i in range(1,11):
        tablelist.append(f'{num}x{i}={num*i}')
    return tablelist
v=table(5)
print(v)
#output:['5x1=5', '5x2=10', '5x3=15', '5x4=20', '5x5=25', '5x6=30', '5x7=35', '5x8=40', '5x9=45', '5x10=50']

#Eg6:
def table(num):
    tablelist=[]
    for i in range(1,11):
        tablelist.append(f'{num}x{i}={num*i}')
    return tablelist
v=table(5)
for x in v:
    print(x)
#output:
#5x1=5
#5x2=10
#5x3=15
#5x4=20
#5x5=25
#5x6=30
#5x7=35
#5x8=40
#5x9=45
#5x10=50

#So now both ways i got output then why i should i use generators:
#1.comparing both codes by using generator the code is less lines and it work faster then other code
#i will tell you how to check size of code
#first import sys
#size=sys.getsizeof(give function calling variable name,i.e 'v' for above example)
#then print('size:',size)

#Eg7:checking the size using return keyword
import sys
def table(num):
    tablelist=[]
    for i in range(1,11):
        tablelist.append(f'{num}x{i}={num*i}')
    return tablelist
v=table(5)
size=sys.getsizeof(v)
print('size:',size)
for x in v:
    print(x)
#output:
#size: 184
#5x1=5
#5x2=10
#5x3=15
#5x4=20
#5x5=25
#5x6=30
#5x7=35
#5x8=40
#5x9=45
#5x10=50

#Eg8:
t=(i for i in range(1,11))
print(t)
#output:<generator object <genexpr> at 0x000001E680C74880>

#Eg9:
t=(i for i in range(1,11))
for x in t:
    print(x)
#output:
#1
#2
#3
#4
#5
#6
#7
#8
#9
#10

#Eg10:
def arthamatic(a,b):
    if b>0:
        yield f'addition:{a+b}'
        yield f'substraction:{a-b}'
        yield f'division:{a/b}'
    else:
        print('b cant be zero')
res=arthamatic(10,2)
for x in res:
    print(x)
#output:
#addition:12
#substraction:8
#division:5.0

#Eg11:
t=(f'even:{i}' for i in range(1,11) if i%2==0)
for x in t:
    print(x)
#output:
#even:2
#even:4
#even:6
#even:8
#even:10

#Eg12:
t=(f'even:{i}' for i in range(1,11) if i%2==0)
print(next(t))
#output:even:2

#Eg13:
t=(f'even:{i}' for i in range(1,11) if i%2==0)
print(next(t))
print(next(t))
print(next(t))
print(next(t))
print(next(t))
#output:
#even:2
#even:4
#even:6
#even:8
#even:10