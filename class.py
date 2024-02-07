#inner class

class student:
    def __init__(self):
        self.name="hemakumar"
        self.work="engineer"
    def show(self):
        print("name:",self.name)
        print("work:",self.work)

t=student()
t.show()
  
class color:
    def __init__(self):
        self.name="orange"
        self.lg=lightgreen()

    def show(self):
        print("name:",self.name)

class lightgreen:
    def __init__(self):
        self.name="lightgreen"
        self.code=  "024avc"
    def display(self):
        print("name:",self.name)
        print("code:",self.code)

o=color()       
o.show()
g=o.lg
g.display()

#multiple inner class

class doctors:
    def __init__(self):
        self.name="doctor"
        self.den=self.dentist()
        self.car=self.cardiologist()

    def show(self):
        print("in outer class")
        print("name:",self.name)

    class dentist:
        def __init__(self):
            self.name="hemakumar"
            self.degree="MBBS"
        def display(self):
            print("name:",self.name)
            print("degree:",self.degree)

    class cardiologist:
        def __init__(self):
            self.name="omkar"
            self.degree="DM"
        def display(self):
            print("name:",self.name)
            print("degree:" ,self.degree)

y=doctors()
y.show()
d1=y.den
d2=y.car
print()
d1.display()
print()
d2.display()

#multilevel inner class

class info:
    def __init__(self):
        self.inner=self.inner()
    def show(self):
        print("this is the outer class")
    
    class inner:
        def __init__(self):
            self.innerclass=self.innerclass()
        def show(self):
            print("this is the inner class ")
        class innerclass:
            def show(self):        
              print("this is an innerclass of inner class")

o=info()
o.show()
t1=o.inner
t1.show()
t2=o.inner.innerclass
t2.show()

#accessing members of one class inside another class

class employee:
    def __init__(self,eno,ename,esal):
        self.eno=eno
        self.ename=ename
        self.esal=esal
    
    def display(self):
        print("eno : ",self.eno)
        print("ename ",self.ename)
        print("esal : ",self.esal)

class Test:
    def modify(emp):
        emp.eno=emp.eno+1000
        print("printing name inside test class modify method ",emp.ename)
        emp.display()

e=employee(23,"aman",2000)
Test.modify(e)


class student:
    def __init__(self):
        self.name="kumar"
        self.subs=self.subjects()
        return
    def show(self):
        print("name:",self.name)
        self.subs.display()
    class subjects:
     def __init__(self):
        self.sub1="maths"
        self.sub2="english"
        return
     def display(self):
        print("subjects:",self.sub1,self.sub2)

s1=student()
s1.show()   


class A:
    def __init__(self,name ,age):
        self.name=name
        self.age=age

    def method_a(self,a,b):
        return a+b 

class D:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def method_b(self,a,b):
        return A(self.name,self.age).method_a(a,b)           

b1=D("hema",90 ) 
print(b1.method_b(10,15))          


class A:
    def __init__(self,name ,age):
        self.name=name
        self.age=age

    def method_a(self,a,b):
        return a+b 

class D:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def method_b(self,a,b):
        return A(self.name,self.age).method_a(a,b)   

class C:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def method_b(self,a,b):
        return A(self.name,self.age).method_a(a,b)                       

b1=D("hema",90 ) 
print(b1.method_b(10,15))
print(b1.method_b(20,80))          


class employee:
    def __init__(self,eno,ename,esal):
        self.eno=eno
        self.ename=ename
        self.esal=esal
    
    def display(self):
        print("eno : ",self.eno)
        print("ename ",self.ename)
        print("esal : ",self.esal)

class Test:
    def modify(emp):
        emp.eno=emp.eno+1000
        print("printing name inside test class modify method ",emp.ename)
        emp.display()


              

e=employee(23,"aman",2000)
Test.modify(e)

# python program to understand the 
# accessing of objects within objects 


class first: 
	 
	def __init__(self): 
		self.fst = second() 
		
	def first_method(self): 
		print("Inside first method") 

class second:  
	def __init__(self): 
		self.snd = "HK"
		
	def second_method(self): 
		print("Inside second method") 


obj1 = first() 
print(obj1) 

obj2 = obj1.fst 
print(obj2) 

print(obj2.snd) 

obj2.second_method() 

#
