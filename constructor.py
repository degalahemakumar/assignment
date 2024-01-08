#OOPS,
#Constructor


class student:
    "this is student class with required data"
print(student.__doc__)
help(student)

class student:
    sname="hema"
s=student()
print(s.sname)  

class student:
    sname="hema"
s=student()
print(s.sname)   
print(student.sname)


class student:
    def read(self):
        print("reading python")
s=student()
s.read()

class student:
    def read(self,empname,empphn):
        self.enmpname=empname
        self.empphn=empphn
        print("hemakumar")
s=student( "omkar",4789)
s.read() 

class student:
    def read(self,x,y):
        self.empname=x
        self.empphn=y
        print("reading python")
        def diplay(self):
            print(self.empname,self.empphn)
s=student()
s.read("kumar",2341)      

class student:
    def __init__(self,empname,empphn):
        self.empname=empname
        self.empphn=empphn
        print("reading python")
        def diplay(self):
         print(self.empname,"_____",self.empphn)
s=student()
s.read("kumar",2341)
s.display() 

class student:
    def __init__(self,x,y):
        self.empname=x
        self.empphn=y
        print("reading python")
        def diplay(self):
         print(self.empname,"_____",self.empphn)
s=student()
s.read("kumar",2341)
s.display()  


class Student:
    sname="marvel"
    def __init__(self,person_name,person_section,person_rollno):
        self.name=person_name
        self.section=person_section
        self.rollno=person_rollno
    def display(self):
        print(self.sname,"----",self.name,"----",self.section,"----",self.rollno)

    

s=Student("aman","c",21)
b=Student("raju","a",45)
c=Student("sairam","B",98)

s.display()
b.display()
c.display()

class student:
    def __init__(self):
       self.name="hema"
       self.age=24
       self.marks=80
    def hello(self):
       print("I am:",self.name)
       print("my age is:",self.age)
       print("my marks is:",self.marks)    

class Student:
    def __init__(self,name,age,marks):
       self.name=name
       self.age=age
       self.marks=marks
    def hello(self):
       print("I am:",self.name)
       print("my age is:",self.age)
       print("my marks is:",self.marks) 



s1=Student("hema",110,80)
s1.hello()

class test:

    def __init__(self):
        print("hemakumar")
    def m1(self):
        print("method execution...")

t1=test()
t2=test()
t3=test()
t1.m1()


class student:
    def __init__(self,x,y,z):
        self.name=x
        self.rollno=y
        self.marks=z
    def display(self):
        print("student name:{}\nRollno:{}\nMarks:{}".format(self.name,self.rollno,self.marks))

s1=student("hema",110,70)
s1.display() 
s2=student("kumar",120,89)
s2.display()  

class student:
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks
    def display(self):
        print("student name:{}\nRollno:{}\nMarks:{}".format(self.name,self.rollno,self.marks))

s1=student("hema",110,70)
s1.display() 
s2=student("chinni",130,80)
s2.display()

class test:
    def __init__(self):
        self.a=40
        self.b=30

    def m1(self):
        self.c=60

t=test()
t.m1() 
print (t.__dict__)      


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