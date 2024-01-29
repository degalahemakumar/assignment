class child:
        def display(self):
                print("parent")
        def show(self):
                print("child")


c1=child()
c1.show()
c1.display()

class child:
    def display(self):
        print("parent")
    class child:
        print("parent")
    def show(self):
            print("child")


c1=child()
c1.show()
c1.display() 

class employee():
        def __init__(self,name,age,salary):
              self.name=name 
              self.age=age
              self.salary=salary
              

t=employee("hema",23,10000)
print(t)           
        
class emp():
      def __init__(self,name,age,salary,id):
            self.name=name
            self.age=age
            self.salary=salary
            self.id=id

i=emp("hema",23,10000,101)
print(i.age)
print(i.salary)    

'''class employee:
      id=10
      name="kumar"
      def display(self):
            print("id:"%d\n name:%s"%(self,id,self.name))
                  
emp=employee()
emp.display()                  '''

class student:
      rno=123
      name="abc"
      branch="ece"
      def read(self):
            print("reading")


abc=student()
print("rno",abc.rno)
print("name",abc.name)
print("branch",abc.branch)  
abc.read    

class student:
      rno=123
      name="abc"
      branch="ece"
      def read(self):
            print("reading")


abc=student()
print("rno",abc.rno)
print("name",abc.name)
print("branch",abc.branch)  
abc.read  ()


class student:
      rno=123
      name="abc"
      branch="ece"
      def read(self):
            print("rno",abc.rno)
            print("reading")


abc=student()
print("rno",abc.rno)
print("name",abc.name)
print("branch",abc.branch)  
abc.read  

class student:
      rno=123
      name="abc"
      branch="ece"
      def read(self):
            rno=456
            print("rno=",rno)
            print("reading")


abc=student()
print("rno=",abc.rno)
print("name=",abc.name)
print("branch=",abc.branch)  
abc.read

class student:
      rno=123
      name="abc"
      branch="ece"
      def read(self):
        rno=456
        print("variable=",self.rno)
        print("reading...")
        write(self):
        print('writing...')
            
abc=student()
obj=student()
print("rno",student.rno)
print("name",abc.name)
print('branch',abc.branch)
abc.read()
abc.write()            
        


abc=student()
print("rno",abc.rno)
print("name",abc.name)
print("branch",abc.branch)  
abc.read  
 