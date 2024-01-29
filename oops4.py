class Test:
    a=10
    def __init__(self):
        self.a=999
    
    def m1(self):
        Test.a=800
    @classmethod
    def m2(cls):
        cls.a=600
    @staticmethod
    def m3():
        Test.a=200
    
t=Test()
t.m1()
t.m2()
t.m3()
print(t.a)



class Test:
    a=10
    def __init__(self):
        self.b=999
    
    def m1(self):
        Test.a=800
    @classmethod
    def m2(cls):
        cls.a=600
    @staticmethod
    def m3():
        Test.a=200
    
t=Test()
t.m1()
t.m2()
t.m3()
t.a=489
print(t.a)
print(Test.a)


class Test:
    a=10
    def __init__(self):
        Test.b=20
        del Test.a
    def m1(self):
        Test.c=30
        del Test.b
    @classmethod
    def m2(cls):
        cls.d=677
        del Test.c
    @staticmethod
    def m3():
        Test.r=60
        

t=Test()
t.m1()
t.m3()
print(Test.__dict__)



class test:
    a=10
    def __init__(self):
        test.b=20
        del test.a
    def m1(self):
        test.c=30
        del test.b
    @classmethod
    def m2(cls):
        cls.d=40
        del test.c
    @staticmethod
    def m3():
        test.e=50
        del test.d
print(t.__dict__)
print(test.__dict__)
t=test()
print(test.__dict__)
t.m1()
print(test.__dict__)
test.m2()
print(test.__dict__)
test.m3()
print(test.__dict__)
test.f=60
print(test.__dict__)
del test.e
print(test.__dict__)

class test:
    a=10
    def __init__():
        self.b=20
    @classmethod
    def m1(cls):
        cls.a=555
        cls.b=666

test.m1()
print(test.__dict__)            


class test:
    a=10
    @classmethod
    def m1(cls):
        del cls.a
        

test.m1()
print(test.__dict__)        

class test:
    a=10
    @classmethod
    def m1(cls):
        pass
        del cls .a

test.m1()
print(test.__dict__)   

class marks:
  @staticmethod
  def math_num(a,b):
      return a+b
  
  @staticmethod
  def sci_num(a,b):
      return a+b
  
  @staticmethod
  def eng_num(a,b):
      return a+b
  
print("total marks in math",marks.math_num(67,40))
print("total marks in science",marks.sci_num(90,56))
print("total marks in english",marks.eng_num(78,90))

class test:
    @staticmethod
    def hi():
        print("hello world")

obj=test()
obj.hi()

class test:
    @staticmethod
    def Age(age):
      if(age<=18):
          print("the person is not eligible to vote")
      else:
          print("the person is eligible to vote")

test.Age(30) 
test.Age(14)               

class test:
    @staticmethod
    def add(x,y):
        return x+y

print("the sum is:",test.add(6,7))

class test:
    @staticmethod
    def static1():
        print("this is a static method called by the class method")

    @staticmethod
    def static2():
        test.static1()

    @classmethod
    def class_method(cls):
        cls.static2()

test.class_method()

class test:
    def __init__(self,name):
        self.name=name

    @staticmethod
    def get_tasks(name):
        tasks =["mail","bills","product"]
        return tasks

    def start(self):
        tasks =self.get_tasks(self.name)  
        for task in tasks:
            print(task)

l=test("checklist")
l.start()              