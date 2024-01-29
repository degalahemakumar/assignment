class myclass:
     def __init__(self,x,y):
         self.x=x
         self.y=y
        
     @classmethod
     def create_from_str(cls,string):
         x,y=map(int,string.split(",")) 
         return cls(x,y)
    
obj=myclass.create_from_str("4,6")   

class test:
    def __init__(self,a,b):
        self.a=30
        self.b=40

    @classmethod
    def info(cls,string):
        a,b=map(int,string.split(","))
        return cls(a,b)
    
obj=test.info("5,6")

class test:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    @classmethod
    def info(cls,string):
        a,b=map(str,string.split(","))
        return cls(a,b)
    
obj=test.info("hema,kumar") 

class test:
    def __init__(self,a):
        self.a=a
        
    def info(cls,string):
        a,b=map(int,self.a.split(","))
        print(a)
        print(b)
    
obj=test("4,6") 
obj.info()



