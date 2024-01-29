class test:
    pass
    def m1(self):
     print("intansce variable")
    @ classmethod
    def m2(cls):
     print ("class method")
    @ staticmethod
    def m3():
     print("static method")

obj=test()   
obj.m1()
obj.m2()
obj.m3()     


class Test:
    a=10
    def __init__(self):
        Test.b=20
        
    def m1(self):
        Test.c=80
        self.u=499
    
    @classmethod
    def m2(cls):
        Test.d=700
        cls.e=200
        cls.y=90
    
    @staticmethod
    def m3():
        Test.f=500

t=test()
t.m1()
test.m2()
test.m3()
print(Test.__dict__)

class test:
   a=10
   def __init__(self):
      test.b=20
   def m1(self):
      test.c=30
   @ classmethod
   def m2(self):
      test.d=700
      test.e=800
   @ staticmethod
   def m3():
       test.f=900      

t=test()
t.m1()
test.m2()
test.m3()
print(test.__dict__)

class method:
   a=10
   def __init__(self):
      print(self.a)
      print(test.a)
   def m1(self):
      print(self.a)
      print(test.a)
   @ classmethod  
   def m2(self):
      print(self.a)
      print(test.a)  
   @ staticmethod
   def m3(self):
      print(self.a)
      print(test.a)   

print(test.a)
print(test.__dict__)

class Test:
    a=10
    def __init__(self):
        Test.b=20
        
    def m1(self):
        Test.c=80
        self.u=499
    
    @classmethod
    def m2(cls):
        Test.d=700
        cls.e=200
        cls.y=90
    
    @staticmethod
    def m3():
        Test.f=500

t=test()
t.m1()
test.m2()
test.m3()
print(Test.__dict__)

class test:
   a=10
   def __init__(self):
      test.b=20
   def m1(self):
      test.c=30
   @ classmethod
   def m2(self):
      test.d=700
      test.e=800
   @ staticmethod
   def m3():
       test.f=900      

t=test()
t.m1()
test.m2()
test.m3()
print(test.__dict__)


class Test:
    a=10
    def __init__(self):
        print(self.a)
        print(Test.a)
    
    def m1(self):
        print(self.a)
        print(Test.a)

    @classmethod
    def m2(self):
        print(self.a)
        print(Test.a)

    @staticmethod
    def m3():
        print(Test.a)

t=Test()
t.m1()
t.m2()
t.m3()
print(t.a)

class Test:
    a=10
    def __init__(self):
        print(self.a)
        print(Test.a)
    
    def m1(self):
        print(self.a)
        print(Test.a)

    @classmethod
    def m2(self):
        print(self.a)
        print(Test.a)

    @staticmethod
    def m3():
        print(Test.a)

print(Test.a)
print(Test.__dict__)

class test:
   a=10
   def __init__(self):
      test.b=20
   def m1(self):
        test.c=30
   @ classmethod
   def m2(cls):
        cls.d1=40
        test.d1=400
   @ staticmethod
   def m3():
      test.e=50

print(test.__dict__)
t=test()
print(test.__dict__)
t.m1()
test.m2()
test.m3()
print(test.__dict__)
test.f=90
print(test.__dict__)


class test:
   a=10
   @ classmethod
   def m1(cls):
      cls.a=888
   @ staticmethod
   def m2():
      test.a=999

print(test.a)
test.m1()
print(test.a)
test.m2()
print(test.a)

class merhod:
   a=10
   def __init__(self):
      test.b=20
      test.a
   def m1(self):
      test.c=30
      test.b
   @ classmethod
   def m2(cls):
      cls.d=40
      test.c                    
   @ staticmethod
   def m3():
      test.e=50
      test.d 

print(test.__dict__)
t.m1()
print(test.__dict__)
test.m2()
print(test.__dict__)
test.m3()
print(test.__dict__)
test.f=60
print(test.__dict__)    

class method:
   a=10
   def __init__(self):
      self.b=20
   @classmethod
   def m1(cls):
        cls.a=30
        cls.b=40

t1=test()
t2=test()
t1.m1()
print(t1.a,t1.b)
print(t2.a,t2.b)
print(test.a,test.b)