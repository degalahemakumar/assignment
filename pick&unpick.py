#emp detali
class Employee:
    def __init__(self,eno,ename,esal):
        self.eno=eno
        self.ename=ename
        self.esal=esal
a=Employee(101,'kumar',10000)
print(a.ename,a.esal)
print(a.eno,a.ename)  

class Employee:
    def __init__(self,eno,ename,esal):
        self.eno=eno
        self.ename=ename
        self.esal=esal
    def display(self):
     print(self.eno,"/t",self.ename,"/t",self.esal)
a=Employee(101,'kumar',10000)
b=Employee(102,'hema',20000)
a.display()
b.display()

#picking

import pickle

class Employee:
    def __init__(self,eno,ename,esal):
        self.eno=eno
        self.ename=ename
        self.esal=esal
    def display(self):
        print(self.eno,"/t",self.ename,"/t",self.esal)

with open("emp.data","wb") as f:
     e=Employee(233,"aman",10000)
     b=Employee(244,"raju",20000)   
     pickle.dump(e,f)
     pickle.dump(b,f)
     e.display()
     b.display()
     print("pickle of emp object is done ")

import pickle

class Employee:
    def __init__(self,eno,ename,esal):
        self.eno=eno
        self.ename=ename
        self.esal=esal
    def display(self):
        print(self.eno,"/t",self.ename,"/t",self.esal)

with open("emp.data","wb") as f:
     e=Employee(233,"aman",10000)
     b=Employee(244,"raju",20000)   
     pickle.dump(e,f)
     pickle.dump(b,f)
print("pickle of emp object is done ")     



import pickle
f=open("emp.data","wb")
n=int(input("enter the number of employees:"))
for i in range(n):
    eno=int(input("enter employee number:"))
    ename=input("enter employee name:")
    esal=int(input("enter employee salary:"))
    eaddr=input("enter employee address:")
    e=e.Employee(eno,ename,esal,eaddr)
    pickle.dump(e,f)
print("employee object pickle successfully")     


#unpickle

import pickle

class Employee:
    def __init__(self,eno,ename,esal):
        self.eno=eno
        self.ename=ename
        self.esal=esal
    def display(self):
        print(self.eno,"/t",self.ename,"/t",self.esal)


with open("emp.data","rb") as f:
    obj=pickle.load(f)
    print("emp info after the unpickling")
    obj.display()

    
import pickle
f=open("emp.data","rb")
print("employee details:")
while True:
    try:
        obj=pickle.load(f)
        obj.display()
    except EOFError:
        print("all employee completed")
        break
    f.close()

 #pickle&unpickle   
import pickle
class Employee:
    def __init__(self,eno,ename,esal):
        self.eno=eno
        self.ename=ename
        self.esal=esal
    def display(self):
        print(self.eno,"/t",self.ename,"/t",self.esal)

with open("emp.data","wb") as f:
     e=Employee(233,"aman",10000)
     b=Employee(244,"raju",20000)   
     pickle.dump(e,f)
     pickle.dump(b,f)
     print("pickle of emp object is done ")

with open("emp.data","rb") as f:
    obj=pickle.load(f)
    print("emp info after the unpickling")
    obj.display()

import pickle
class Student:
    def __init__(self,eroll,ename,emark):
        self.eroll=eroll
        self.ename=ename
        self.emark=emark
    def display(self):
     print(self.eroll,"/t",self.ename,"/t",self.emark)

with open("student.data","wb") as f:
     e=Student(101,"hema",80)
     b=Student(102,"kumar",67)   
     pickle.dump(e,f)
     pickle.dump(b,f)
     print("pickle of student object is done ")

with open("student.data","rb") as f:
    obj=pickle.load(f)
    print("student info after the unpickling")
    obj.display()

