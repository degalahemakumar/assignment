#Modules:
#import modulename
#import mod1,mod2,mod3
#import modul as m
#import mod1 as m,mod2 as m1,mod3 as m3

#from mod import member
#from mod import mem1,mem2,mem3
#from mod import mem1 as m1
#from mod import *

#Eg1:I have created there 3 files inside the package folder:

#test1.py
def division(a,b):
    if b>0:
        print('division:',a/b)
    else:
        print("b cannot be zero")

#test2.py
def addition(x,y):
    print('additon:',x+y)

#test3.py
import test1
import test2
test1.division(10,2)
test2.addition(100,100)

#output:
#division: 5.0
#additon: 200

#Eg2:
#test1.py
def division(a,b):
    if b>0:
        print('division:',a/b)
    else:
        print("b cannot be zero")

#test2.py
def addition(x,y):
    print('additon:',x+y)

#test3.py
import test1,test2
test1.division(10,2)
test2.addition(100,100)

#output:
#division: 5.0
#additon: 200

#Eg3:
#test1.py
def division(a,b):
    if b>0:
        print('division:',a/b)
    else:
        print("b cannot be zero")

#test2.py
def addition(x,y):
    print('additon:',x+y)

#test3.py
import test1 as t1
import test2 as t2
t1.division(10,2)
t2.addition(100,100)

#output:
#division: 5.0
#additon: 200

#Eg4:
#test1.py
def division(a,b):
    if b>0:
        print('division:',a/b)
    else:
        print("b cannot be zero")

#test2.py
def addition(x,y):
    print('additon:',x+y)

#test3.py
import test1 as t1,test2 as t2
t1.division(10,2)
t2.addition(100,100)

#output:
#division: 5.0
#additon: 200

#Packages:
#Inside package folder i will create a folder package1 and also we have three files inside the package folder 
#So i will connect package1 folder and those 3files  
#Eg5:
#folder name:package
#inside package there are file:test1.py,and there is folder also :package1
#so i have 1 file and 1 folder inside package folder
#inside package1 folder i created 3 files python1.py,python2.py,python3.py

#package folder:
 #package1 folder:
  #python1.py
  #python2.py
  #python3.py
#test1.py

#Eg5:
#package folder:
 #package1 folder:
  #python1.py
def addition(a,b):
    print('addition:',a+b)

  #python2.py
def sub(x,y):
    print('sub:',x-y)

  #python3.py
def floor_division(m,n):
    print('f-div:',m//n)

#test1.py
from package1 import python1
from package1 import python2
from package1 import python3
python1.addition(10,10)
python2.sub(200,100)
python3.floor_division(100,10)

#output:
#addition: 20
#sub: 100
#f-div: 10

#Eg6:
#package folder:
 #package1 folder:
  #python1.py
def addition(a,b):
    print('addition:',a+b)

  #python2.py
def sub(x,y):
    print('sub:',x-y)

  #python3.py
def floor_division(m,n):
    print('f-div:',m//n)

#test1.py
from package1 import python1,python2,python3
python1.addition(10,10)
python2.sub(200,100)
python3.floor_division(100,10)

#output:
#addition: 20
#sub: 100
#f-div: 10

#Eg7:
#package folder:
 #package1 folder:
  #python1.py
def addition(a,b):
    print('addition:',a+b)

  #python2.py
def sub(x,y):
    print('sub:',x-y)

  #python3.py
def floor_division(m,n):
    print('f-div:',m//n)

#test1.py
from package1 import python1 as p1,python2 as p2,python3 as p3
p1.addition(10,10)
p2.sub(200,100)
p3.floor_division(100,10)

#output:
#addition: 20
#sub: 100
#f-div: 10

#Eg8:
#test1.py
from test1 import *
x(10,10)
y(100,100)

#test2.py
from test1 import *
t(10,10)
v(100,100)

#output:
#10 10
#100 100

#Eg9:
#package1
 #python1.py
def t(x,y):
    print(x,y)
def t1(k,l):
    print(k,l)

 #python2.py
def t2(m,n):
    print(m,n)

#test1.py
from package1.python1 import *    
from package1.python1 import * 
t(10,10)
t1(20,20)
t2(30,30)

#output:
#10 10
#20 20
#30 30