class test:
    def __init__(self,name,section,rollno):
        self.name=name
        self.section=section
        self.rollno=rollno
    def info(self):
        print(self.name)
        print(self.section)
        print(self.rollno)

test=[test ("kumar","A",200)]
for i in test:

 i.info()
 class test:
    def __init__(self,name,section,rollno):
        self.name=name
        self.section=section
        self.rollno=rollno
    def info(self):
        print(self.name)
        print(self.section)
        print(self.rollno)

test=[test ("kumar","A",200),test("hema","D", 400)]
for i in test:

 i.info()

 class test:
    def __init__(self,name,section,rollno):
        self.name=name
        self.section=section
        self.rollno=rollno
    def info(self):
        print("name",self.name)
        print("section",self.section)
        print("rollno",self.rollno)

test=[test ("kumar","A",200)]
for i in test:

 i.info()


 class test:
     a=500
     def __init__(self):
         self.d=400

print(test.a)

class test:
    a=800
    def __init__(self):
        self.b=300

t=test()
print(t.b)

class test:
    a=800
    def __init__(self):
        self.b=410
    def hi(self):
        self.c=980

t=test()
print(t.a)
print(test.a)

class test:
    def __init__(self):
        self.b=100

t1=test()
t1.b=890
test.a=200
t2=test()
print(t1.a,t1.b)
print(t2.a,t2.b)

class test:
    def __init__(self):
        self.b=100

t1=test()
t1.b=890
test.a=200
t2=test()
print(t1.a,t1.b)

class test:
    
    a=900
    def __init__(self):
        self.b=880
    def hi(self):
        self.c=500
        self.d=600

t1=test()
t1.b=8000
t1.hi()
t2=test()
t2.a=134
t2.hi()
print(t1.a,t1.b,t1.c,t1.d)
print(t2.a,t2.b,t1.c,t2.d)
print(t1.__dict__)
print(t2.__dict__)

class test:

    def __init__(self):
        self.a=40
        self.b=30

    def m1(self):
        self.c=60

t=test()
t.m1() 
print (t.__dict__)  

class emp:
    def __init__(self):
        self.name="hema"
        self.empid=200
    def m1(self):
        self.b=80

e=emp()
e.m1()
print(e.__dict__)


class test:
    def __iniy__(self):
        self.a=40
        self.b=30

    def m1(self):
        self.c=60

t=test()
t.m1() 
print (t.__dict__) 

class test:
    def __init__(self):
        self.a=40
        self.b=30

    def m1(self):
        self.c=60

t=test()
t.m1() 
t.d=40
print (t.__dict__) 

class test:

    def __init__(self):
        self.a=10
        self.b=20
    def display(self):
        print(self.a)
        print(self.b)

t=test()
t.display()
print(t.a,t.b)

class test:
    def __init__(self):
        self.a=10
        self.b=20
        self.c=30
        self.d=40
    def m1(self):
        del self.d
t=test()
print(t.__dict__)
t.m1()
print(t.__dict__)
del t.c
print(t.__dict__)  

class test:
    def __init__(self):
        self.a=10
        self.b=20
        self.c=30
        self.d=40

t1=test()
t2=test()
del t1.a
print(t1.__dict__)
print(t2.__dict__)


class test:
    def __init__(self):
        self.a=10
        self.b=20

t1=test()
t1.a=777
t1.b=444
t2=test()
print("t1:",t1.a,t1.b)
print("t2:",t2.a,t2.b)   

class test:
    x=10
    def __init__(self):
        self.y=20

t1=test()
t2=test()
print("t1:",t1.x,t1.y)
print("t2:",t2.x,t2.y)
test.x=777
t1.y=999
print("t1:",t1.x,t1.y)
print("t2:",t2.x,t2.y)

class test:
    def __init__(self):
        self.a=10

t1=test()
t2=test()
print(t1.__dict__)
print(t2.__dict__)

class test:
    def __init__(self):
        self.a=10

t1=test()
t2=test()
del t1.a
print(t1.__dict__)
print(t2.__dict__)

class test:
    x=10
    def __init__(self):
        self.y=20

t1=test()
t2=test()
test.x=777
t1.y=999
print("t1:",t1.x,t1.y)
print("t2:",t2.x,t2.y)

class test:
    x=10
    def __init__(self):
        self.y=20
        self.z=40

t1=test()
t2=test()
print("t1:",t1.x,t1.y)
print("t2:",t2.x,t2.y)
test.x=777
test.z=400
t1.y=999
print("t1:",t1.x,t1.y,t1.z)
print("t2:",t2.x,t2.y,t2.z)


class test:
    
    a=900
    def __init__(self):
        self.b=880
    def hi(self):
        self.c=500
        self.d=600
        self.f=700

t1=test()
t1.b=8000
t1.hi()
t2=test()
t2.a=134
t2.hi()
print(t1.a,t1.b,t1.c,t1.d,t1.f)
print(t2.a,t2.b,t1.c,t2.d,t2.f)
class test:
    
    a=900
    def __init__(self):
        self.b=880
    def hi(self):
        self.c=500
        self.d=600
        

t1=test()
t1.b=8000
t1.hi()
t2=test()
t2.a=134
t2.b=450
t2.hi()
print(t1.a,t1.b,t1.c,t1.d,)
print(t2.a,t2.b,t1.c,t2.d)

class test:
    
    a=900
    def __init__(self):
        self.b=880
    def hi(self):
        self.c=500
        self.d=600
        self.f=560

t1=test()
t1.b=8000
t1.hi()
t2=test()
t2.a=134
t2.b=340
t1.f=450
t2.hi()
print(t1.a,t1.b,t1.c,t1.d,t1.f)
print(t2.a,t2.b,t1.c,t2.d,t2.f)